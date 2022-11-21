# Generated from src/Parser/CommandGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,44,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,4,9,41,8,9,11,9,12,9,42,
        0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,2,7,0,10,
        10,34,34,39,39,59,60,62,62,96,96,124,124,2,0,9,9,32,32,44,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,
        0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,29,1,0,0,0,11,31,1,0,
        0,0,13,33,1,0,0,0,15,35,1,0,0,0,17,37,1,0,0,0,19,40,1,0,0,0,21,22,
        8,0,0,0,22,2,1,0,0,0,23,24,5,34,0,0,24,4,1,0,0,0,25,26,5,39,0,0,
        26,6,1,0,0,0,27,28,5,59,0,0,28,8,1,0,0,0,29,30,5,62,0,0,30,10,1,
        0,0,0,31,32,5,60,0,0,32,12,1,0,0,0,33,34,5,10,0,0,34,14,1,0,0,0,
        35,36,5,96,0,0,36,16,1,0,0,0,37,38,5,124,0,0,38,18,1,0,0,0,39,41,
        7,1,0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,
        43,20,1,0,0,0,2,0,42,0
    ]

class CommandGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    UNQUOTED = 1
    DOUBLE_QUOTE = 2
    SINGLE_QUOTE = 3
    SEMICOLON = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    NEWLINE = 7
    BACKQUOTE = 8
    PIPE = 9
    WHITESPACE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'''", "';'", "'>'", "'<'", "'\\n'", "'`'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "UNQUOTED", "DOUBLE_QUOTE", "SINGLE_QUOTE", "SEMICOLON", "GREATER_THAN", 
            "LESS_THAN", "NEWLINE", "BACKQUOTE", "PIPE", "WHITESPACE" ]

    ruleNames = [ "UNQUOTED", "DOUBLE_QUOTE", "SINGLE_QUOTE", "SEMICOLON", 
                  "GREATER_THAN", "LESS_THAN", "NEWLINE", "BACKQUOTE", "PIPE", 
                  "WHITESPACE" ]

    grammarFileName = "CommandGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


