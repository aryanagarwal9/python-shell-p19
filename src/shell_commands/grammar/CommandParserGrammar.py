# Generated from src/shell_commands/grammar/CommandParserGrammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,3,0,
        28,8,0,1,0,1,0,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,53,8,2,10,2,12,
        2,56,9,2,1,3,3,3,59,8,3,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,
        1,3,1,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,3,3,78,8,3,1,4,1,4,3,
        4,82,8,4,1,5,4,5,85,8,5,11,5,12,5,86,1,6,1,6,3,6,91,8,6,1,7,1,7,
        3,7,95,8,7,1,7,1,7,1,7,3,7,100,8,7,1,7,3,7,103,8,7,1,8,1,8,1,8,3,
        8,108,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,5,11,120,
        8,11,10,11,12,11,123,9,11,1,11,1,11,1,12,1,12,3,12,129,8,12,1,12,
        0,2,2,4,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,135,0,27,1,0,0,
        0,2,34,1,0,0,0,4,44,1,0,0,0,6,58,1,0,0,0,8,81,1,0,0,0,10,84,1,0,
        0,0,12,90,1,0,0,0,14,102,1,0,0,0,16,107,1,0,0,0,18,109,1,0,0,0,20,
        113,1,0,0,0,22,117,1,0,0,0,24,128,1,0,0,0,26,28,3,2,1,0,27,26,1,
        0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,
        32,6,1,-1,0,32,35,3,4,2,0,33,35,3,6,3,0,34,31,1,0,0,0,34,33,1,0,
        0,0,35,41,1,0,0,0,36,37,10,1,0,0,37,38,5,5,0,0,38,40,3,2,1,2,39,
        36,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,
        0,43,41,1,0,0,0,44,45,6,2,-1,0,45,46,3,6,3,0,46,47,5,9,0,0,47,48,
        3,6,3,0,48,54,1,0,0,0,49,50,10,1,0,0,50,51,5,9,0,0,51,53,3,6,3,0,
        52,49,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,5,1,0,
        0,0,56,54,1,0,0,0,57,59,5,10,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,
        65,1,0,0,0,60,61,3,14,7,0,61,62,5,10,0,0,62,64,1,0,0,0,63,60,1,0,
        0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,
        1,0,0,0,68,73,3,10,5,0,69,70,5,10,0,0,70,72,3,8,4,0,71,69,1,0,0,
        0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,77,1,0,0,0,75,73,
        1,0,0,0,76,78,5,10,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,0,
        79,82,3,14,7,0,80,82,3,10,5,0,81,79,1,0,0,0,81,80,1,0,0,0,82,9,1,
        0,0,0,83,85,3,12,6,0,84,83,1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,
        87,1,0,0,0,87,11,1,0,0,0,88,91,3,16,8,0,89,91,5,4,0,0,90,88,1,0,
        0,0,90,89,1,0,0,0,91,13,1,0,0,0,92,94,5,7,0,0,93,95,5,10,0,0,94,
        93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,103,3,10,5,0,97,99,5,6,
        0,0,98,100,5,10,0,0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,
        101,103,3,10,5,0,102,92,1,0,0,0,102,97,1,0,0,0,103,15,1,0,0,0,104,
        108,3,18,9,0,105,108,3,22,11,0,106,108,3,20,10,0,107,104,1,0,0,0,
        107,105,1,0,0,0,107,106,1,0,0,0,108,17,1,0,0,0,109,110,5,1,0,0,110,
        111,5,11,0,0,111,112,5,1,0,0,112,19,1,0,0,0,113,114,5,3,0,0,114,
        115,5,13,0,0,115,116,5,3,0,0,116,21,1,0,0,0,117,121,5,2,0,0,118,
        120,3,24,12,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,5,2,0,0,125,
        23,1,0,0,0,126,129,3,20,10,0,127,129,5,12,0,0,128,126,1,0,0,0,128,
        127,1,0,0,0,129,25,1,0,0,0,17,27,34,41,54,58,65,73,77,81,86,90,94,
        99,102,107,121,128
    ]

class CommandParserGrammar ( Parser ):

    grammarFileName = "CommandParserGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "'>'", "'<'", "'\\n'", "'|'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'''", "'\"'", 
                     "'`'" ]

    symbolicNames = [ "<INVALID>", "SQ", "DQ", "BQ", "UNQUOTED", "SEMICOLON", 
                      "GREATER_THAN", "LESS_THAN", "NEWLINE", "PIPE", "WHITESPACE", 
                      "SQ_MID", "DQ_MID", "BQ_MID", "SQ_END", "DQ_END", 
                      "BQ_END" ]

    RULE_cmdline = 0
    RULE_command = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_atom = 4
    RULE_argument = 5
    RULE_argument_content = 6
    RULE_redirection = 7
    RULE_quoted = 8
    RULE_singleQuoted = 9
    RULE_backQuoted = 10
    RULE_doubleQuoted = 11
    RULE_doubleQuotedElement = 12

    ruleNames =  [ "cmdline", "command", "pipe", "call", "atom", "argument", 
                   "argument_content", "redirection", "quoted", "singleQuoted", 
                   "backQuoted", "doubleQuoted", "doubleQuotedElement" ]

    EOF = Token.EOF
    SQ=1
    DQ=2
    BQ=3
    UNQUOTED=4
    SEMICOLON=5
    GREATER_THAN=6
    LESS_THAN=7
    NEWLINE=8
    PIPE=9
    WHITESPACE=10
    SQ_MID=11
    DQ_MID=12
    BQ_MID=13
    SQ_END=14
    DQ_END=15
    BQ_END=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CmdlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandParserGrammar.EOF, 0)

        def command(self):
            return self.getTypedRuleContext(CommandParserGrammar.CommandContext,0)


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_cmdline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdline" ):
                return visitor.visitCmdline(self)
            else:
                return visitor.visitChildren(self)




    def cmdline(self):

        localctx = CommandParserGrammar.CmdlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cmdline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1246) != 0:
                self.state = 26
                self.command(0)


            self.state = 29
            self.match(CommandParserGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Seq_cmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.CommandContext
            super().__init__(parser)
            self.left = None # CommandContext
            self.right = None # CommandContext
            self.copyFrom(ctx)

        def SEMICOLON(self):
            return self.getToken(CommandParserGrammar.SEMICOLON, 0)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParserGrammar.CommandContext)
            else:
                return self.getTypedRuleContext(CommandParserGrammar.CommandContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq_cmd" ):
                return visitor.visitSeq_cmd(self)
            else:
                return visitor.visitChildren(self)


    class Call_cmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def call(self):
            return self.getTypedRuleContext(CommandParserGrammar.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_cmd" ):
                return visitor.visitCall_cmd(self)
            else:
                return visitor.visitChildren(self)


    class Pipe_cmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pipe(self):
            return self.getTypedRuleContext(CommandParserGrammar.PipeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe_cmd" ):
                return visitor.visitPipe_cmd(self)
            else:
                return visitor.visitChildren(self)



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CommandParserGrammar.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CommandParserGrammar.Pipe_cmdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 32
                self.pipe(0)
                pass

            elif la_ == 2:
                localctx = CommandParserGrammar.Call_cmdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CommandParserGrammar.Seq_cmdContext(self, CommandParserGrammar.CommandContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 36
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 37
                    self.match(CommandParserGrammar.SEMICOLON)
                    self.state = 38
                    localctx.right = self.command(2) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_pipe

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Nested_pipeContext(PipeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.PipeContext
            super().__init__(parser)
            self.left = None # PipeContext
            self.right = None # CallContext
            self.copyFrom(ctx)

        def PIPE(self):
            return self.getToken(CommandParserGrammar.PIPE, 0)
        def pipe(self):
            return self.getTypedRuleContext(CommandParserGrammar.PipeContext,0)

        def call(self):
            return self.getTypedRuleContext(CommandParserGrammar.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested_pipe" ):
                return visitor.visitNested_pipe(self)
            else:
                return visitor.visitChildren(self)


    class One_pipeContext(PipeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.PipeContext
            super().__init__(parser)
            self.left = None # CallContext
            self.right = None # CallContext
            self.copyFrom(ctx)

        def PIPE(self):
            return self.getToken(CommandParserGrammar.PIPE, 0)
        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParserGrammar.CallContext)
            else:
                return self.getTypedRuleContext(CommandParserGrammar.CallContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_pipe" ):
                return visitor.visitOne_pipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CommandParserGrammar.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CommandParserGrammar.One_pipeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 45
            localctx.left = self.call()
            self.state = 46
            self.match(CommandParserGrammar.PIPE)
            self.state = 47
            localctx.right = self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CommandParserGrammar.Nested_pipeContext(self, CommandParserGrammar.PipeContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 49
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 50
                    self.match(CommandParserGrammar.PIPE)
                    self.state = 51
                    localctx.right = self.call() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(CommandParserGrammar.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParserGrammar.WHITESPACE)
            else:
                return self.getToken(CommandParserGrammar.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParserGrammar.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandParserGrammar.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParserGrammar.AtomContext)
            else:
                return self.getTypedRuleContext(CommandParserGrammar.AtomContext,i)


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = CommandParserGrammar.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 57
                self.match(CommandParserGrammar.WHITESPACE)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 60
                self.redirection()
                self.state = 61
                self.match(CommandParserGrammar.WHITESPACE)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.argument()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.match(CommandParserGrammar.WHITESPACE)
                    self.state = 70
                    self.atom() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(CommandParserGrammar.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(CommandParserGrammar.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(CommandParserGrammar.ArgumentContext,0)


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CommandParserGrammar.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.redirection()
                pass
            elif token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParserGrammar.Argument_contentContext)
            else:
                return self.getTypedRuleContext(CommandParserGrammar.Argument_contentContext,i)


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = CommandParserGrammar.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 83
                    self.argument_content()

                else:
                    raise NoViableAltException(self)
                self.state = 86 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_argument_content

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Quoted_argContext(Argument_contentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.Argument_contentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def quoted(self):
            return self.getTypedRuleContext(CommandParserGrammar.QuotedContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted_arg" ):
                return visitor.visitQuoted_arg(self)
            else:
                return visitor.visitChildren(self)


    class UnquotedContext(Argument_contentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.Argument_contentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNQUOTED(self):
            return self.getToken(CommandParserGrammar.UNQUOTED, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnquoted" ):
                return visitor.visitUnquoted(self)
            else:
                return visitor.visitChildren(self)



    def argument_content(self):

        localctx = CommandParserGrammar.Argument_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argument_content)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3]:
                localctx = CommandParserGrammar.Quoted_argContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.quoted()
                pass
            elif token in [4]:
                localctx = CommandParserGrammar.UnquotedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(CommandParserGrammar.UNQUOTED)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.operator = None # Token

        def argument(self):
            return self.getTypedRuleContext(CommandParserGrammar.ArgumentContext,0)


        def LESS_THAN(self):
            return self.getToken(CommandParserGrammar.LESS_THAN, 0)

        def WHITESPACE(self):
            return self.getToken(CommandParserGrammar.WHITESPACE, 0)

        def GREATER_THAN(self):
            return self.getToken(CommandParserGrammar.GREATER_THAN, 0)

        def getRuleIndex(self):
            return CommandParserGrammar.RULE_redirection

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = CommandParserGrammar.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                localctx.operator = self.match(CommandParserGrammar.LESS_THAN)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 93
                    self.match(CommandParserGrammar.WHITESPACE)


                self.state = 96
                self.argument()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                localctx.operator = self.match(CommandParserGrammar.GREATER_THAN)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 98
                    self.match(CommandParserGrammar.WHITESPACE)


                self.state = 101
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(CommandParserGrammar.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(CommandParserGrammar.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(CommandParserGrammar.BackQuotedContext,0)


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = CommandParserGrammar.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_quoted)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.singleQuoted()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.doubleQuoted()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.backQuoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParserGrammar.SQ)
            else:
                return self.getToken(CommandParserGrammar.SQ, i)

        def SQ_MID(self):
            return self.getToken(CommandParserGrammar.SQ_MID, 0)

        def getRuleIndex(self):
            return CommandParserGrammar.RULE_singleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleQuoted" ):
                return visitor.visitSingleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def singleQuoted(self):

        localctx = CommandParserGrammar.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_singleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(CommandParserGrammar.SQ)
            self.state = 110
            self.match(CommandParserGrammar.SQ_MID)
            self.state = 111
            self.match(CommandParserGrammar.SQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BQ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParserGrammar.BQ)
            else:
                return self.getToken(CommandParserGrammar.BQ, i)

        def BQ_MID(self):
            return self.getToken(CommandParserGrammar.BQ_MID, 0)

        def getRuleIndex(self):
            return CommandParserGrammar.RULE_backQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackQuoted" ):
                return visitor.visitBackQuoted(self)
            else:
                return visitor.visitChildren(self)




    def backQuoted(self):

        localctx = CommandParserGrammar.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_backQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CommandParserGrammar.BQ)
            self.state = 114
            self.match(CommandParserGrammar.BQ_MID)
            self.state = 115
            self.match(CommandParserGrammar.BQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParserGrammar.DQ)
            else:
                return self.getToken(CommandParserGrammar.DQ, i)

        def doubleQuotedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParserGrammar.DoubleQuotedElementContext)
            else:
                return self.getTypedRuleContext(CommandParserGrammar.DoubleQuotedElementContext,i)


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_doubleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoubleQuoted" ):
                return visitor.visitDoubleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def doubleQuoted(self):

        localctx = CommandParserGrammar.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(CommandParserGrammar.DQ)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==12:
                self.state = 118
                self.doubleQuotedElement()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(CommandParserGrammar.DQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParserGrammar.RULE_doubleQuotedElement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Dq_contentContext(DoubleQuotedElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.DoubleQuotedElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DQ_MID(self):
            return self.getToken(CommandParserGrammar.DQ_MID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDq_content" ):
                return visitor.visitDq_content(self)
            else:
                return visitor.visitChildren(self)


    class Bq_in_dqContext(DoubleQuotedElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParserGrammar.DoubleQuotedElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def backQuoted(self):
            return self.getTypedRuleContext(CommandParserGrammar.BackQuotedContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBq_in_dq" ):
                return visitor.visitBq_in_dq(self)
            else:
                return visitor.visitChildren(self)



    def doubleQuotedElement(self):

        localctx = CommandParserGrammar.DoubleQuotedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_doubleQuotedElement)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = CommandParserGrammar.Bq_in_dqContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.backQuoted()
                pass
            elif token in [12]:
                localctx = CommandParserGrammar.Dq_contentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(CommandParserGrammar.DQ_MID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.command_sempred
        self._predicates[2] = self.pipe_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




