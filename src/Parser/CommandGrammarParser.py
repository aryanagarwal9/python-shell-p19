# Generated from src/Parser/CommandGrammar.g4 by ANTLR 4.11.1
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
        4,1,10,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,0,3,0,30,8,0,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,44,8,2,1,3,3,3,47,8,3,1,3,1,3,3,3,51,8,3,5,3,53,8,3,10,3,
        12,3,56,9,3,1,3,1,3,3,3,60,8,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,1,
        3,3,3,69,8,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,3,3,78,8,3,1,4,
        1,4,3,4,82,8,4,1,4,1,4,1,4,3,4,87,8,4,1,4,3,4,90,8,4,1,5,1,5,3,5,
        94,8,5,1,6,1,6,1,6,3,6,99,8,6,1,7,1,7,5,7,103,8,7,10,7,12,7,106,
        9,7,1,7,1,7,1,8,1,8,5,8,112,8,8,10,8,12,8,115,9,8,1,8,1,8,1,9,1,
        9,1,9,5,9,122,8,9,10,9,12,9,125,9,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,
        10,12,14,16,18,0,3,2,0,3,3,7,7,1,0,7,8,2,0,2,2,7,8,140,0,20,1,0,
        0,0,2,33,1,0,0,0,4,43,1,0,0,0,6,46,1,0,0,0,8,89,1,0,0,0,10,93,1,
        0,0,0,12,98,1,0,0,0,14,100,1,0,0,0,16,109,1,0,0,0,18,118,1,0,0,0,
        20,25,3,2,1,0,21,22,5,4,0,0,22,24,3,2,1,0,23,21,1,0,0,0,24,27,1,
        0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,28,
        30,5,4,0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,34,3,4,2,
        0,32,34,3,6,3,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,3,
        6,3,0,36,37,5,9,0,0,37,38,3,6,3,0,38,44,1,0,0,0,39,40,3,6,3,0,40,
        41,5,9,0,0,41,42,3,4,2,0,42,44,1,0,0,0,43,35,1,0,0,0,43,39,1,0,0,
        0,44,5,1,0,0,0,45,47,5,10,0,0,46,45,1,0,0,0,46,47,1,0,0,0,47,54,
        1,0,0,0,48,50,3,8,4,0,49,51,5,10,0,0,50,49,1,0,0,0,50,51,1,0,0,0,
        51,53,1,0,0,0,52,48,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,
        0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,64,3,10,5,0,58,60,5,10,0,0,
        59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,63,3,8,4,0,62,59,1,
        0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,73,1,0,0,0,66,
        64,1,0,0,0,67,69,5,10,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,
        0,0,70,72,3,10,5,0,71,68,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,
        74,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,76,78,5,10,0,0,77,76,1,0,
        0,0,77,78,1,0,0,0,78,7,1,0,0,0,79,81,5,6,0,0,80,82,5,10,0,0,81,80,
        1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,90,3,10,5,0,84,86,5,5,0,0,
        85,87,5,10,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,90,3,
        10,5,0,89,79,1,0,0,0,89,84,1,0,0,0,90,9,1,0,0,0,91,94,3,12,6,0,92,
        94,5,1,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,11,1,0,0,0,95,99,3,14,
        7,0,96,99,3,18,9,0,97,99,3,16,8,0,98,95,1,0,0,0,98,96,1,0,0,0,98,
        97,1,0,0,0,99,13,1,0,0,0,100,104,5,3,0,0,101,103,8,0,0,0,102,101,
        1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,
        1,0,0,0,106,104,1,0,0,0,107,108,5,3,0,0,108,15,1,0,0,0,109,113,5,
        8,0,0,110,112,8,1,0,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,
        0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,5,
        8,0,0,117,17,1,0,0,0,118,123,5,2,0,0,119,122,3,16,8,0,120,122,8,
        2,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,
        0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,
        2,0,0,127,19,1,0,0,0,21,25,29,33,43,46,50,54,59,64,68,73,77,81,86,
        89,93,98,104,113,121,123
    ]

class CommandGrammarParser ( Parser ):

    grammarFileName = "CommandGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\"'", "'''", "';'", "'>'", 
                     "'<'", "'\\n'", "'`'", "'|'" ]

    symbolicNames = [ "<INVALID>", "UNQUOTED", "DOUBLE_QUOTE", "SINGLE_QUOTE", 
                      "SEMICOLON", "GREATER_THAN", "LESS_THAN", "NEWLINE", 
                      "BACKQUOTE", "PIPE", "WHITESPACE" ]

    RULE_command = 0
    RULE_subCommand = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_redirection = 4
    RULE_argument = 5
    RULE_quoted = 6
    RULE_singleQuoted = 7
    RULE_backQuoted = 8
    RULE_doubleQuoted = 9

    ruleNames =  [ "command", "subCommand", "pipe", "call", "redirection", 
                   "argument", "quoted", "singleQuoted", "backQuoted", "doubleQuoted" ]

    EOF = Token.EOF
    UNQUOTED=1
    DOUBLE_QUOTE=2
    SINGLE_QUOTE=3
    SEMICOLON=4
    GREATER_THAN=5
    LESS_THAN=6
    NEWLINE=7
    BACKQUOTE=8
    PIPE=9
    WHITESPACE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.SubCommandContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.SubCommandContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.SEMICOLON)
            else:
                return self.getToken(CommandGrammarParser.SEMICOLON, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = CommandGrammarParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.subCommand()
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self.match(CommandGrammarParser.SEMICOLON)
                    self.state = 22
                    self.subCommand() 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 28
                self.match(CommandGrammarParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(CommandGrammarParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(CommandGrammarParser.CallContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_subCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubCommand" ):
                listener.enterSubCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubCommand" ):
                listener.exitSubCommand(self)




    def subCommand(self):

        localctx = CommandGrammarParser.SubCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subCommand)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.CallContext,i)


        def PIPE(self):
            return self.getToken(CommandGrammarParser.PIPE, 0)

        def pipe(self):
            return self.getTypedRuleContext(CommandGrammarParser.PipeContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)




    def pipe(self):

        localctx = CommandGrammarParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pipe)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.call()
                self.state = 36
                self.match(CommandGrammarParser.PIPE)
                self.state = 37
                self.call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.call()
                self.state = 40
                self.match(CommandGrammarParser.PIPE)
                self.state = 41
                self.pipe()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.ArgumentContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.WHITESPACE)
            else:
                return self.getToken(CommandGrammarParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.RedirectionContext,i)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = CommandGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 45
                self.match(CommandGrammarParser.WHITESPACE)


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 48
                self.redirection()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 49
                    self.match(CommandGrammarParser.WHITESPACE)


                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.argument()
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 58
                        self.match(CommandGrammarParser.WHITESPACE)


                    self.state = 61
                    self.redirection() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 67
                        self.match(CommandGrammarParser.WHITESPACE)


                    self.state = 70
                    self.argument() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 76
                self.match(CommandGrammarParser.WHITESPACE)


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

        def LESS_THAN(self):
            return self.getToken(CommandGrammarParser.LESS_THAN, 0)

        def argument(self):
            return self.getTypedRuleContext(CommandGrammarParser.ArgumentContext,0)


        def WHITESPACE(self):
            return self.getToken(CommandGrammarParser.WHITESPACE, 0)

        def GREATER_THAN(self):
            return self.getToken(CommandGrammarParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)




    def redirection(self):

        localctx = CommandGrammarParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(CommandGrammarParser.LESS_THAN)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 80
                    self.match(CommandGrammarParser.WHITESPACE)


                self.state = 83
                self.argument()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(CommandGrammarParser.GREATER_THAN)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 85
                    self.match(CommandGrammarParser.WHITESPACE)


                self.state = 88
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

        def quoted(self):
            return self.getTypedRuleContext(CommandGrammarParser.QuotedContext,0)


        def UNQUOTED(self):
            return self.getToken(CommandGrammarParser.UNQUOTED, 0)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CommandGrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 8]:
                self.state = 91
                self.quoted()
                pass
            elif token in [1]:
                self.state = 92
                self.match(CommandGrammarParser.UNQUOTED)
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
            return self.getTypedRuleContext(CommandGrammarParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(CommandGrammarParser.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(CommandGrammarParser.BackQuotedContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = CommandGrammarParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quoted)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.singleQuoted()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.doubleQuoted()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
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

        def SINGLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.SINGLE_QUOTE)
            else:
                return self.getToken(CommandGrammarParser.SINGLE_QUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.NEWLINE)
            else:
                return self.getToken(CommandGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_singleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleQuoted" ):
                listener.enterSingleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleQuoted" ):
                listener.exitSingleQuoted(self)




    def singleQuoted(self):

        localctx = CommandGrammarParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(CommandGrammarParser.SINGLE_QUOTE)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1910) != 0:
                self.state = 101
                _la = self._input.LA(1)
                if _la <= 0 or _la==3 or _la==7:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(CommandGrammarParser.SINGLE_QUOTE)
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

        def BACKQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.BACKQUOTE)
            else:
                return self.getToken(CommandGrammarParser.BACKQUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.NEWLINE)
            else:
                return self.getToken(CommandGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_backQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackQuoted" ):
                listener.enterBackQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackQuoted" ):
                listener.exitBackQuoted(self)




    def backQuoted(self):

        localctx = CommandGrammarParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_backQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(CommandGrammarParser.BACKQUOTE)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1662) != 0:
                self.state = 110
                _la = self._input.LA(1)
                if _la <= 0 or _la==7 or _la==8:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(CommandGrammarParser.BACKQUOTE)
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

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.DOUBLE_QUOTE)
            else:
                return self.getToken(CommandGrammarParser.DOUBLE_QUOTE, i)

        def backQuoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.BackQuotedContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.BackQuotedContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.NEWLINE)
            else:
                return self.getToken(CommandGrammarParser.NEWLINE, i)

        def BACKQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.BACKQUOTE)
            else:
                return self.getToken(CommandGrammarParser.BACKQUOTE, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_doubleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleQuoted" ):
                listener.enterDoubleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleQuoted" ):
                listener.exitDoubleQuoted(self)




    def doubleQuoted(self):

        localctx = CommandGrammarParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(CommandGrammarParser.DOUBLE_QUOTE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1914) != 0:
                self.state = 121
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 119
                    self.backQuoted()
                    pass
                elif token in [1, 3, 4, 5, 6, 9, 10]:
                    self.state = 120
                    _la = self._input.LA(1)
                    if _la <= 0 or ((_la) & ~0x3f) == 0 and ((1 << _la) & 388) != 0:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(CommandGrammarParser.DOUBLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





