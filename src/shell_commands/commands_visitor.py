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

    def get_io_files(self, redirection):
        pass

    def visitCall(self, ctx: CommandParserGrammar.CallContext):
        arguments = self.visit(ctx.argument())
        input_file, output_file = None, None

        for redirection in ctx.redirections_list:
            input_file, output_file = self.get_io_files(redirection, input_file, output_file)


    def visitArgument(self, ctx: CommandParserGrammar.ArgumentContext):
        visited_elements = [self.visit(element) for element in ctx.arguments]
        globbed_elements = []


    def glob_expand(self, argument: str):
        files = glob.glob(argument)
        return files if files else [argument]

    def visitRedirection(self, ctx: CommandParserGrammar.RedirectionContext):
        files = self.visit(ctx.argument())
        if len(files)!=1:
            raise RedirectionError('wrong number of redirections')

        return files[0]

    def visitQuoted(self, ctx: CommandParserGrammar.QuotedContext):
        if ctx.backQuoted() is not None:
            return re.sub('[\t ]+', '\n', self.visit(ctx.backQuoted()).strip())
            #change this

        return self.visitChildren(ctx)

    def visitBackQuoted(self, ctx: CommandParserGrammar.BackQuotedContext):
        temp_deque = deque()
        CommandsVisitor.converter(ctx.BQ_MID().getText()).eval(None, temp_deque)
        return "".join(temp_deque).replace('\n', ' ')

    def visitSingleQuoted(self, ctx: CommandParserGrammar.SingleQuotedContext):
        return ctx.SQ_MID().getText()

    def visitDoubleQuoted(self, ctx: CommandParserGrammar.DoubleQuotedContext):
        return "".join(self.visit(element) for element in ctx.dq_elems)

    def visitDq_content(self, ctx: CommandParserGrammar.Dq_contentContext):
        return ctx.DQ_MID().getText()

