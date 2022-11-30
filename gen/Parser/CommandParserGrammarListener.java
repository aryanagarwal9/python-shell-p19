// Generated from /Users/adityaparashar/UCL/Year2/COMP0010/CW/python-shell-p19/src/Parser/CommandParserGrammar.g4 by ANTLR 4.10.1
package Parser;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CommandParserGrammar}.
 */
public interface CommandParserGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(CommandParserGrammar.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(CommandParserGrammar.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#subCommand}.
	 * @param ctx the parse tree
	 */
	void enterSubCommand(CommandParserGrammar.SubCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#subCommand}.
	 * @param ctx the parse tree
	 */
	void exitSubCommand(CommandParserGrammar.SubCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(CommandParserGrammar.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(CommandParserGrammar.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(CommandParserGrammar.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(CommandParserGrammar.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(CommandParserGrammar.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(CommandParserGrammar.RedirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(CommandParserGrammar.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(CommandParserGrammar.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#quoted}.
	 * @param ctx the parse tree
	 */
	void enterQuoted(CommandParserGrammar.QuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#quoted}.
	 * @param ctx the parse tree
	 */
	void exitQuoted(CommandParserGrammar.QuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterSingleQuoted(CommandParserGrammar.SingleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#singleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitSingleQuoted(CommandParserGrammar.SingleQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#backQuoted}.
	 * @param ctx the parse tree
	 */
	void enterBackQuoted(CommandParserGrammar.BackQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#backQuoted}.
	 * @param ctx the parse tree
	 */
	void exitBackQuoted(CommandParserGrammar.BackQuotedContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParserGrammar#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void enterDoubleQuoted(CommandParserGrammar.DoubleQuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParserGrammar#doubleQuoted}.
	 * @param ctx the parse tree
	 */
	void exitDoubleQuoted(CommandParserGrammar.DoubleQuotedContext ctx);
}