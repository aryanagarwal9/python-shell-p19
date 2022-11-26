parser grammar CommandParserGrammar;
options {tokenVocab=CommandLexerGrammar;}

cmdline: command? EOF;
command: pipe #pipe_cmd | call #call_cmd | left=command SEMICOLON right=command #seq_cmd;
pipe: left=call PIPE right=call #one_pipe | left=pipe PIPE right=call #nested_pipe;

call: WHITESPACE? (redirections_list+=redirection WHITESPACE)* argument (WHITESPACE atoms_list+=atom)* WHITESPACE?;
atom: redirection | argument;
argument: arguments+=argument_content;
argument_content: (quoted|UNQUOTED)+;
redirection: operator=LESS_THAN WHITESPACE? argument | operator=GREATER_THAN WHITESPACE? argument;

quoted: singleQuoted | doubleQuoted | backQuoted;
singleQuoted: SQ SQ_MID SQ;
backQuoted: BQ BQ_MID BQ;
doubleQuoted: DQ dq_elems+=doubleQuotedElement* DQ;
doubleQuotedElement: backQuoted #bq_in_dq | DQ_MID #dq_content;



