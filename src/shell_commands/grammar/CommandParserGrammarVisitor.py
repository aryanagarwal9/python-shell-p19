# Generated from src/shell_commands/CommandParserGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandParserGrammar import CommandParserGrammar
else:
    from CommandParserGrammar import CommandParserGrammar

# This class defines a complete generic visitor for a parse tree produced by CommandParserGrammar.

class CommandParserGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandParserGrammar#cmdline.
    def visitCmdline(self, ctx:CommandParserGrammar.CmdlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#seq_cmd.
    def visitSeq_cmd(self, ctx:CommandParserGrammar.Seq_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#call_cmd.
    def visitCall_cmd(self, ctx:CommandParserGrammar.Call_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#pipe_cmd.
    def visitPipe_cmd(self, ctx:CommandParserGrammar.Pipe_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#nested_pipe.
    def visitNested_pipe(self, ctx:CommandParserGrammar.Nested_pipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#one_pipe.
    def visitOne_pipe(self, ctx:CommandParserGrammar.One_pipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#call.
    def visitCall(self, ctx:CommandParserGrammar.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#atom.
    def visitAtom(self, ctx:CommandParserGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#argument.
    def visitArgument(self, ctx:CommandParserGrammar.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#redirection.
    def visitRedirection(self, ctx:CommandParserGrammar.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#quoted.
    def visitQuoted(self, ctx:CommandParserGrammar.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#singleQuoted.
    def visitSingleQuoted(self, ctx:CommandParserGrammar.SingleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#backQuoted.
    def visitBackQuoted(self, ctx:CommandParserGrammar.BackQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#doubleQuoted.
    def visitDoubleQuoted(self, ctx:CommandParserGrammar.DoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#bq_in_dq.
    def visitBq_in_dq(self, ctx:CommandParserGrammar.Bq_in_dqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParserGrammar#dq_content.
    def visitDq_content(self, ctx:CommandParserGrammar.Dq_contentContext):
        return self.visitChildren(ctx)


del CommandParserGrammar