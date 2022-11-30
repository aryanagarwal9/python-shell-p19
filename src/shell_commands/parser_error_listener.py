from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ParserErrorListener(ErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f' Does not follow the grammar: line: {line}, column: {column}, msg: {msg}'
        raise ParseCancellationException(error_msg)


ParserErrorListener.INSTANCE = ParserErrorListener()
