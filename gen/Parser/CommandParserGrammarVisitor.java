// Generated from /Users/adityaparashar/UCL/Year2/COMP0010/CW/python-shell-p19/src/Parser/CommandParserGrammar.g4 by ANTLR 4.10.1
package Parser;
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CommandParserGrammar}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CommandParserGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommand(CommandParserGrammar.CommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#subCommand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubCommand(CommandParserGrammar.SubCommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#pipe}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPipe(CommandParserGrammar.PipeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall(CommandParserGrammar.CallContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#redirection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRedirection(CommandParserGrammar.RedirectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(CommandParserGrammar.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#quoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuoted(CommandParserGrammar.QuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#singleQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSingleQuoted(CommandParserGrammar.SingleQuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#backQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBackQuoted(CommandParserGrammar.BackQuotedContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParserGrammar#doubleQuoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDoubleQuoted(CommandParserGrammar.DoubleQuotedContext ctx);
}