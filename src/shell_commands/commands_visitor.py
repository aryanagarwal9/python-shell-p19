import glob
import re
from collections import deque
from src.shell_commands.grammar.CommandParserGrammar import CommandParserGrammar
from src.shell_commands.grammar.CommandParserGrammarVisitor import CommandParserGrammarVisitor
from src.shell_commands.grammar.CommandLexerGrammar import CommandLexerGrammar
from src.shell_commands.commands.command import Command
from antlr4 import InputStream, CommonTokenStream
from src.shell_commands.commands.pipe import Pipe
from src.shell_commands.commands.call import Call
from src.shell_commands.commands.seq import Seq


class CommandsVisitor(CommandParserGrammarVisitor):
    @classmethod
    def converter(cls, cmdline: str) -> Command:
        input_stream = InputStream(cmdline)
        lexer = CommandLexerGrammar(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CommandParserGrammar(stream)
        tree = parser.cmdline()
        command = tree.accept(cls())
        return command

    def visitCmdline(self, ctx: CommandParserGrammar.CmdlineContext):
        return self.visit(ctx.command())

    def visitSeq_cmd(self, ctx: CommandParserGrammar.Seq_cmdContext):
        return Seq(self.visit(ctx.left), self.visit(ctx.right))

    def visitOne_pipe(self, ctx: CommandParserGrammar.One_pipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def visitNested_pipe(self, ctx: CommandParserGrammar.Nested_pipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def get_io_files(self, redirection, input_file, output_file):
        return self.get_output_file(redirection, input_file, output_file) if redirection.operator.text == '>' else self.get_input_file(redirection, input_file, output_file)

    def get_input_file(self, redirection, input_file, output_file):
        if input_file is None:
            return self.visit(redirection), output_file
        raise ValueError('unnecessary input redirections')

    def get_output_file(self, redirection, input_file, output_file):
        if output_file is None:
            return input_file, self.visit(redirection)
        raise ValueError('unnecessary output redirections')

    def visitCall(self, ctx: CommandParserGrammar.CallContext):
        arguments = self.visit(ctx.argument())
        input_file, output_file = None, None

        for redirection in ctx.redirection():
            input_file, output_file = self.get_io_files(redirection, input_file, output_file)

        for atom in ctx.atom():
            if atom.redirection() is not None:
                redirection = atom.redirection()
                input_file, output_file = self.get_io_files(redirection, input_file, output_file)
            else:
                arguments.extend(self.visit(atom.argument()))

        return Call(arguments[0], arguments[1:], input_file, output_file)

    def visitArgument(self, ctx: CommandParserGrammar.ArgumentContext):
        visited_args = [self.visit(arg) for arg in ctx.argument_content()]
        final_globbed_args = []
        split_args = "".join(visited_args).split('\n')
        glob_indices = self.get_glob_indices(ctx.argument_content(), visited_args, split_args)

        for index in range(len(split_args)):
            split_arg = split_args[index]
            if glob_indices[index]:
                final_globbed_args.extend(self.glob_expand(split_arg))
            else:
                final_globbed_args.append(split_arg)
        return final_globbed_args

    @staticmethod
    def get_glob_indices(argument_content: CommandParserGrammar.argument_content, visited_args: list, split_args: list):
        glob_indices = [False for i in range(len(split_args))]
        splitting_index = 0
        for arg, visited_arg in zip(argument_content, visited_args):
            if hasattr(arg, 'UNQUOTED') and '*' in visited_arg:
                glob_indices[splitting_index] = True
            else:
                splitting_index += visited_arg.count('\n')
        return glob_indices

    @staticmethod
    def glob_expand(argument: str):
        files = glob.glob(argument)
        return files if files else [argument]

    def visitRedirection(self, ctx: CommandParserGrammar.RedirectionContext):
        files = self.visit(ctx.argument())
        if len(files) != 1:
            raise ValueError('wrong number of redirections')
        return files[0]

    def visitQuoted(self, ctx: CommandParserGrammar.QuotedContext):
        if ctx.backQuoted() is not None:
            return re.sub('[\t ]+', '\n', self.visit(ctx.backQuoted()).strip())
        return self.visitChildren(ctx)

    def visitBackQuoted(self, ctx: CommandParserGrammar.BackQuotedContext):
        temp_deque = deque()
        CommandsVisitor.converter(ctx.BQ_MID().getText()).eval(None, temp_deque)
        return "".join(temp_deque).replace('\n', ' ')

    def visitSingleQuoted(self, ctx: CommandParserGrammar.SingleQuotedContext):
        return ctx.SQ_MID().getText()

    def visitDoubleQuoted(self, ctx: CommandParserGrammar.DoubleQuotedContext):
        return "".join(self.visit(element) for element in ctx.doubleQuotedElement())

    def visitDq_content(self, ctx: CommandParserGrammar.Dq_contentContext):
        return ctx.DQ_MID().getText()

    def visitUnquoted(self, ctx:CommandParserGrammar.UnquotedContext):
        return ctx.getText()