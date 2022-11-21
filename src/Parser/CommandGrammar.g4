grammar CommandGrammar;

/*
 * Parser Rules
 */

command: subCommand (SEMICOLON subCommand)* SEMICOLON?;
subCommand: pipe | call;
pipe: (call PIPE call) | (call PIPE pipe);

call: WHITESPACE? (redirection WHITESPACE?)* argument (WHITESPACE? redirection)* (WHITESPACE? argument)* WHITESPACE?;
redirection: (LESS_THAN WHITESPACE? argument) | (GREATER_THAN WHITESPACE? argument);
argument: (quoted | UNQUOTED);

quoted: singleQuoted | doubleQuoted | backQuoted;
singleQuoted: SINGLE_QUOTE ~(NEWLINE | SINGLE_QUOTE)* SINGLE_QUOTE;
backQuoted: BACKQUOTE ~(NEWLINE | BACKQUOTE)* BACKQUOTE;
doubleQuoted: DOUBLE_QUOTE (backQuoted | ~(NEWLINE | BACKQUOTE | DOUBLE_QUOTE))* DOUBLE_QUOTE;




/*
 * Lexer Rules
 */

UNQUOTED: ~[\n'"`<>;|];
DOUBLE_QUOTE: '"';
SINGLE_QUOTE: '\'';
SEMICOLON: ';';
GREATER_THAN: '>';
LESS_THAN: '<';
NEWLINE: '\n';
BACKQUOTE: '`';
PIPE: '|';
WHITESPACE: [\t ]+;
