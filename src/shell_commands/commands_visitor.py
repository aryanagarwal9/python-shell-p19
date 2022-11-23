from src.shell_commands.grammar.CommandParserGrammar import CommandParserGrammar
from src.shell_commands.grammar.CommandParserGrammarVisitor import CommandParserGrammarVisitor
from src.shell_commands.grammar.CommandLexerGrammar import CommandLexerGrammar
from src.shell_commands.commands.command import Command

class CommandsVisitor(CommandParserGrammarVisitor):
    @classmethod
    def converter(cls, cmdline: str) -> Command:
