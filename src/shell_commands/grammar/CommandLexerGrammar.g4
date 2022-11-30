lexer grammar CommandLexerGrammar;
tokens {SQ, DQ, BQ}

/*
 * Lexer Rules
 */

fragment SINGLE_QUOTE: '\'';
fragment DOUBLE_QUOTE: '"';
fragment BACKQUOTE: '`';

UNQUOTED: ~[\n'"`<>;|\t ]+;
SEMICOLON: ';';
GREATER_THAN: '>';
LESS_THAN: '<';
NEWLINE: '\n';
PIPE: '|';
WHITESPACE: [\t ]+;

SQ_START: SINGLE_QUOTE->type(SQ), pushMode(SQ_MODE);
DQ_START: DOUBLE_QUOTE->type(DQ), pushMode(DQ_MODE);
BQ_START: BACKQUOTE->type(BQ), pushMode(BQ_MODE);

mode SQ_MODE;
SQ_MID: ~[\n']+;
SQ_END: '\'' ->type(SQ), popMode;

mode DQ_MODE;
DQ_MID: ~[\n"`]+;
ENTER_BQ: BACKQUOTE->type(BQ), pushMode(BQ_MODE);
DQ_END: '"'->type(DQ), popMode;

mode BQ_MODE;
BQ_MID: ~[\n`]+;
BQ_END: '`'->type(BQ), popMode;


