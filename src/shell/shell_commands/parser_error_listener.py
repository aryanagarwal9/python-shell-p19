from antlr4.error.ErrorListener import ErrorListener


class ParserErrorListener(ErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("line " + str(line) + ":" + str(column) + " " + msg)


ParserErrorListener.INSTANCE = ParserErrorListener()
