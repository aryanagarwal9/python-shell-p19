from src.shell_commands.grammar.CommandParserGrammar import CommandParserGrammar
from src.shell_commands.grammar.CommandParserGrammarVisitor import CommandParserGrammarVisitor
from src.shell_commands.grammar.CommandLexerGrammar import CommandLexerGrammar
from src.shell_commands.commands.command import Command
from antlr4 import *
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

    def get_io_files(self, redirect_type):

    def visitCall(self, ctx:CommandParserGrammar.CallContext):


    def visitCmdline(self, ctx:CommandParserGrammar.CmdlineContext):
        return self.visit(ctx.command())

    def visitSeq_cmd(self, ctx:CommandParserGrammar.Seq_cmdContext):
        return Seq(self.visit(ctx.left), self.visit(ctx.right))

    def visitOne_pipe(self, ctx:CommandParserGrammar.One_pipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def visitNested_pipe(self, ctx:CommandParserGrammar.Nested_pipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def visitQuoted(self, ctx:CommandParserGrammar.QuotedContext):
        if ctx.backQuoted() is None:
            return self.visitChildren(ctx)
        return

    def visitSingleQuoted(self, ctx:CommandParserGrammar.SingleQuotedContext):
        return ctx.SQ_MID().getText()

    def visitDq_content(self, ctx:CommandParserGrammar.Dq_contentContext):
        return ctx.DQ_MID().getText()


