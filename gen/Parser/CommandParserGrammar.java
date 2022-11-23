// Generated from /Users/adityaparashar/UCL/Year2/COMP0010/CW/python-shell-p19/src/Parser/CommandParserGrammar.g4 by ANTLR 4.10.1
package Parser;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommandParserGrammar extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SEMICOLON=1, PIPE=2, WHITESPACE=3, LESS_THAN=4, GREATER_THAN=5, UNQUOTED=6, 
		SINGLE_QUOTE=7, NEWLINE=8, BACKQUOTE=9, DOUBLE_QUOTE=10;
	public static final int
		RULE_command = 0, RULE_subCommand = 1, RULE_pipe = 2, RULE_call = 3, RULE_redirection = 4, 
		RULE_argument = 5, RULE_quoted = 6, RULE_singleQuoted = 7, RULE_backQuoted = 8, 
		RULE_doubleQuoted = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "subCommand", "pipe", "call", "redirection", "argument", "quoted", 
			"singleQuoted", "backQuoted", "doubleQuoted"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SEMICOLON", "PIPE", "WHITESPACE", "LESS_THAN", "GREATER_THAN", 
			"UNQUOTED", "SINGLE_QUOTE", "NEWLINE", "BACKQUOTE", "DOUBLE_QUOTE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CommandParserGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CommandParserGrammar(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class CommandContext extends ParserRuleContext {
		public List<SubCommandContext> subCommand() {
			return getRuleContexts(SubCommandContext.class);
		}
		public SubCommandContext subCommand(int i) {
			return getRuleContext(SubCommandContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CommandParserGrammar.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CommandParserGrammar.SEMICOLON, i);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitCommand(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitCommand(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_command);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			subCommand();
			setState(25);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(21);
					match(SEMICOLON);
					setState(22);
					subCommand();
					}
					} 
				}
				setState(27);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(28);
				match(SEMICOLON);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubCommandContext extends ParserRuleContext {
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public SubCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subCommand; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterSubCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitSubCommand(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitSubCommand(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SubCommandContext subCommand() throws RecognitionException {
		SubCommandContext _localctx = new SubCommandContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_subCommand);
		try {
			setState(33);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				pipe();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PipeContext extends ParserRuleContext {
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public TerminalNode PIPE() { return getToken(CommandParserGrammar.PIPE, 0); }
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public PipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipe; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterPipe(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitPipe(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitPipe(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PipeContext pipe() throws RecognitionException {
		PipeContext _localctx = new PipeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_pipe);
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(35);
				call();
				setState(36);
				match(PIPE);
				setState(37);
				call();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(39);
				call();
				setState(40);
				match(PIPE);
				setState(41);
				pipe();
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(CommandParserGrammar.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(CommandParserGrammar.WHITESPACE, i);
		}
		public List<RedirectionContext> redirection() {
			return getRuleContexts(RedirectionContext.class);
		}
		public RedirectionContext redirection(int i) {
			return getRuleContext(RedirectionContext.class,i);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitCall(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitCall(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_call);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHITESPACE) {
				{
				setState(45);
				match(WHITESPACE);
				}
			}

			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LESS_THAN || _la==GREATER_THAN) {
				{
				{
				setState(48);
				redirection();
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(49);
					match(WHITESPACE);
					}
				}

				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			argument();
			setState(64);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(59);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WHITESPACE) {
						{
						setState(58);
						match(WHITESPACE);
						}
					}

					setState(61);
					redirection();
					}
					} 
				}
				setState(66);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(73);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(68);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WHITESPACE) {
						{
						setState(67);
						match(WHITESPACE);
						}
					}

					setState(70);
					argument();
					}
					} 
				}
				setState(75);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHITESPACE) {
				{
				setState(76);
				match(WHITESPACE);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RedirectionContext extends ParserRuleContext {
		public TerminalNode LESS_THAN() { return getToken(CommandParserGrammar.LESS_THAN, 0); }
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public TerminalNode WHITESPACE() { return getToken(CommandParserGrammar.WHITESPACE, 0); }
		public TerminalNode GREATER_THAN() { return getToken(CommandParserGrammar.GREATER_THAN, 0); }
		public RedirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_redirection; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterRedirection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitRedirection(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitRedirection(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RedirectionContext redirection() throws RecognitionException {
		RedirectionContext _localctx = new RedirectionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_redirection);
		int _la;
		try {
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LESS_THAN:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(79);
				match(LESS_THAN);
				setState(81);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(80);
					match(WHITESPACE);
					}
				}

				setState(83);
				argument();
				}
				}
				break;
			case GREATER_THAN:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(84);
				match(GREATER_THAN);
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHITESPACE) {
					{
					setState(85);
					match(WHITESPACE);
					}
				}

				setState(88);
				argument();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentContext extends ParserRuleContext {
		public QuotedContext quoted() {
			return getRuleContext(QuotedContext.class,0);
		}
		public TerminalNode UNQUOTED() { return getToken(CommandParserGrammar.UNQUOTED, 0); }
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitArgument(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitArgument(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_argument);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINGLE_QUOTE:
			case BACKQUOTE:
			case DOUBLE_QUOTE:
				{
				setState(91);
				quoted();
				}
				break;
			case UNQUOTED:
				{
				setState(92);
				match(UNQUOTED);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QuotedContext extends ParserRuleContext {
		public SingleQuotedContext singleQuoted() {
			return getRuleContext(SingleQuotedContext.class,0);
		}
		public DoubleQuotedContext doubleQuoted() {
			return getRuleContext(DoubleQuotedContext.class,0);
		}
		public BackQuotedContext backQuoted() {
			return getRuleContext(BackQuotedContext.class,0);
		}
		public QuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final QuotedContext quoted() throws RecognitionException {
		QuotedContext _localctx = new QuotedContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_quoted);
		try {
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINGLE_QUOTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				singleQuoted();
				}
				break;
			case DOUBLE_QUOTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(96);
				doubleQuoted();
				}
				break;
			case BACKQUOTE:
				enterOuterAlt(_localctx, 3);
				{
				setState(97);
				backQuoted();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SingleQuotedContext extends ParserRuleContext {
		public List<TerminalNode> SINGLE_QUOTE() { return getTokens(CommandParserGrammar.SINGLE_QUOTE); }
		public TerminalNode SINGLE_QUOTE(int i) {
			return getToken(CommandParserGrammar.SINGLE_QUOTE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CommandParserGrammar.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CommandParserGrammar.NEWLINE, i);
		}
		public SingleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterSingleQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitSingleQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitSingleQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SingleQuotedContext singleQuoted() throws RecognitionException {
		SingleQuotedContext _localctx = new SingleQuotedContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_singleQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(SINGLE_QUOTE);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEMICOLON) | (1L << PIPE) | (1L << WHITESPACE) | (1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << UNQUOTED) | (1L << BACKQUOTE) | (1L << DOUBLE_QUOTE))) != 0)) {
				{
				{
				setState(101);
				_la = _input.LA(1);
				if ( _la <= 0 || (_la==SINGLE_QUOTE || _la==NEWLINE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(SINGLE_QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BackQuotedContext extends ParserRuleContext {
		public List<TerminalNode> BACKQUOTE() { return getTokens(CommandParserGrammar.BACKQUOTE); }
		public TerminalNode BACKQUOTE(int i) {
			return getToken(CommandParserGrammar.BACKQUOTE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CommandParserGrammar.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CommandParserGrammar.NEWLINE, i);
		}
		public BackQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_backQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterBackQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitBackQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitBackQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BackQuotedContext backQuoted() throws RecognitionException {
		BackQuotedContext _localctx = new BackQuotedContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_backQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(BACKQUOTE);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEMICOLON) | (1L << PIPE) | (1L << WHITESPACE) | (1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << UNQUOTED) | (1L << SINGLE_QUOTE) | (1L << DOUBLE_QUOTE))) != 0)) {
				{
				{
				setState(110);
				_la = _input.LA(1);
				if ( _la <= 0 || (_la==NEWLINE || _la==BACKQUOTE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(115);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(116);
			match(BACKQUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DoubleQuotedContext extends ParserRuleContext {
		public List<TerminalNode> DOUBLE_QUOTE() { return getTokens(CommandParserGrammar.DOUBLE_QUOTE); }
		public TerminalNode DOUBLE_QUOTE(int i) {
			return getToken(CommandParserGrammar.DOUBLE_QUOTE, i);
		}
		public List<BackQuotedContext> backQuoted() {
			return getRuleContexts(BackQuotedContext.class);
		}
		public BackQuotedContext backQuoted(int i) {
			return getRuleContext(BackQuotedContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CommandParserGrammar.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CommandParserGrammar.NEWLINE, i);
		}
		public List<TerminalNode> BACKQUOTE() { return getTokens(CommandParserGrammar.BACKQUOTE); }
		public TerminalNode BACKQUOTE(int i) {
			return getToken(CommandParserGrammar.BACKQUOTE, i);
		}
		public DoubleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doubleQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).enterDoubleQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandParserGrammarListener ) ((CommandParserGrammarListener)listener).exitDoubleQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CommandParserGrammarVisitor ) return ((CommandParserGrammarVisitor<? extends T>)visitor).visitDoubleQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DoubleQuotedContext doubleQuoted() throws RecognitionException {
		DoubleQuotedContext _localctx = new DoubleQuotedContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_doubleQuoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(DOUBLE_QUOTE);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEMICOLON) | (1L << PIPE) | (1L << WHITESPACE) | (1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << UNQUOTED) | (1L << SINGLE_QUOTE) | (1L << BACKQUOTE))) != 0)) {
				{
				setState(121);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BACKQUOTE:
					{
					setState(119);
					backQuoted();
					}
					break;
				case SEMICOLON:
				case PIPE:
				case WHITESPACE:
				case LESS_THAN:
				case GREATER_THAN:
				case UNQUOTED:
				case SINGLE_QUOTE:
					{
					setState(120);
					_la = _input.LA(1);
					if ( _la <= 0 || ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEWLINE) | (1L << BACKQUOTE) | (1L << DOUBLE_QUOTE))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(126);
			match(DOUBLE_QUOTE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\n\u0081\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000"+
		"\u0018\b\u0000\n\u0000\f\u0000\u001b\t\u0000\u0001\u0000\u0003\u0000\u001e"+
		"\b\u0000\u0001\u0001\u0001\u0001\u0003\u0001\"\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002,\b\u0002\u0001\u0003\u0003\u0003/\b\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u00033\b\u0003\u0005\u00035\b\u0003\n\u0003\f\u0003"+
		"8\t\u0003\u0001\u0003\u0001\u0003\u0003\u0003<\b\u0003\u0001\u0003\u0005"+
		"\u0003?\b\u0003\n\u0003\f\u0003B\t\u0003\u0001\u0003\u0003\u0003E\b\u0003"+
		"\u0001\u0003\u0005\u0003H\b\u0003\n\u0003\f\u0003K\t\u0003\u0001\u0003"+
		"\u0003\u0003N\b\u0003\u0001\u0004\u0001\u0004\u0003\u0004R\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004W\b\u0004\u0001\u0004\u0003"+
		"\u0004Z\b\u0004\u0001\u0005\u0001\u0005\u0003\u0005^\b\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006c\b\u0006\u0001\u0007\u0001\u0007"+
		"\u0005\u0007g\b\u0007\n\u0007\f\u0007j\t\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0005\bp\b\b\n\b\f\bs\t\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0005\tz\b\t\n\t\f\t}\t\t\u0001\t\u0001\t\u0001\t\u0000\u0000"+
		"\n\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0000\u0003\u0001\u0000"+
		"\u0007\b\u0001\u0000\b\t\u0001\u0000\b\n\u008c\u0000\u0014\u0001\u0000"+
		"\u0000\u0000\u0002!\u0001\u0000\u0000\u0000\u0004+\u0001\u0000\u0000\u0000"+
		"\u0006.\u0001\u0000\u0000\u0000\bY\u0001\u0000\u0000\u0000\n]\u0001\u0000"+
		"\u0000\u0000\fb\u0001\u0000\u0000\u0000\u000ed\u0001\u0000\u0000\u0000"+
		"\u0010m\u0001\u0000\u0000\u0000\u0012v\u0001\u0000\u0000\u0000\u0014\u0019"+
		"\u0003\u0002\u0001\u0000\u0015\u0016\u0005\u0001\u0000\u0000\u0016\u0018"+
		"\u0003\u0002\u0001\u0000\u0017\u0015\u0001\u0000\u0000\u0000\u0018\u001b"+
		"\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u0019\u001a"+
		"\u0001\u0000\u0000\u0000\u001a\u001d\u0001\u0000\u0000\u0000\u001b\u0019"+
		"\u0001\u0000\u0000\u0000\u001c\u001e\u0005\u0001\u0000\u0000\u001d\u001c"+
		"\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000\u001e\u0001"+
		"\u0001\u0000\u0000\u0000\u001f\"\u0003\u0004\u0002\u0000 \"\u0003\u0006"+
		"\u0003\u0000!\u001f\u0001\u0000\u0000\u0000! \u0001\u0000\u0000\u0000"+
		"\"\u0003\u0001\u0000\u0000\u0000#$\u0003\u0006\u0003\u0000$%\u0005\u0002"+
		"\u0000\u0000%&\u0003\u0006\u0003\u0000&,\u0001\u0000\u0000\u0000\'(\u0003"+
		"\u0006\u0003\u0000()\u0005\u0002\u0000\u0000)*\u0003\u0004\u0002\u0000"+
		"*,\u0001\u0000\u0000\u0000+#\u0001\u0000\u0000\u0000+\'\u0001\u0000\u0000"+
		"\u0000,\u0005\u0001\u0000\u0000\u0000-/\u0005\u0003\u0000\u0000.-\u0001"+
		"\u0000\u0000\u0000./\u0001\u0000\u0000\u0000/6\u0001\u0000\u0000\u0000"+
		"02\u0003\b\u0004\u000013\u0005\u0003\u0000\u000021\u0001\u0000\u0000\u0000"+
		"23\u0001\u0000\u0000\u000035\u0001\u0000\u0000\u000040\u0001\u0000\u0000"+
		"\u000058\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000067\u0001\u0000"+
		"\u0000\u000079\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u00009@\u0003"+
		"\n\u0005\u0000:<\u0005\u0003\u0000\u0000;:\u0001\u0000\u0000\u0000;<\u0001"+
		"\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=?\u0003\b\u0004\u0000>;\u0001"+
		"\u0000\u0000\u0000?B\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000"+
		"@A\u0001\u0000\u0000\u0000AI\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000"+
		"\u0000CE\u0005\u0003\u0000\u0000DC\u0001\u0000\u0000\u0000DE\u0001\u0000"+
		"\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0003\n\u0005\u0000GD\u0001\u0000"+
		"\u0000\u0000HK\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001"+
		"\u0000\u0000\u0000JM\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000"+
		"LN\u0005\u0003\u0000\u0000ML\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000N\u0007\u0001\u0000\u0000\u0000OQ\u0005\u0004\u0000\u0000PR\u0005"+
		"\u0003\u0000\u0000QP\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000SZ\u0003\n\u0005\u0000TV\u0005\u0005\u0000\u0000"+
		"UW\u0005\u0003\u0000\u0000VU\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000"+
		"\u0000WX\u0001\u0000\u0000\u0000XZ\u0003\n\u0005\u0000YO\u0001\u0000\u0000"+
		"\u0000YT\u0001\u0000\u0000\u0000Z\t\u0001\u0000\u0000\u0000[^\u0003\f"+
		"\u0006\u0000\\^\u0005\u0006\u0000\u0000][\u0001\u0000\u0000\u0000]\\\u0001"+
		"\u0000\u0000\u0000^\u000b\u0001\u0000\u0000\u0000_c\u0003\u000e\u0007"+
		"\u0000`c\u0003\u0012\t\u0000ac\u0003\u0010\b\u0000b_\u0001\u0000\u0000"+
		"\u0000b`\u0001\u0000\u0000\u0000ba\u0001\u0000\u0000\u0000c\r\u0001\u0000"+
		"\u0000\u0000dh\u0005\u0007\u0000\u0000eg\b\u0000\u0000\u0000fe\u0001\u0000"+
		"\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001"+
		"\u0000\u0000\u0000ik\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000"+
		"kl\u0005\u0007\u0000\u0000l\u000f\u0001\u0000\u0000\u0000mq\u0005\t\u0000"+
		"\u0000np\b\u0001\u0000\u0000on\u0001\u0000\u0000\u0000ps\u0001\u0000\u0000"+
		"\u0000qo\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rt\u0001\u0000"+
		"\u0000\u0000sq\u0001\u0000\u0000\u0000tu\u0005\t\u0000\u0000u\u0011\u0001"+
		"\u0000\u0000\u0000v{\u0005\n\u0000\u0000wz\u0003\u0010\b\u0000xz\b\u0002"+
		"\u0000\u0000yw\u0001\u0000\u0000\u0000yx\u0001\u0000\u0000\u0000z}\u0001"+
		"\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000"+
		"|~\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000~\u007f\u0005\n\u0000"+
		"\u0000\u007f\u0013\u0001\u0000\u0000\u0000\u0015\u0019\u001d!+.26;@DI"+
		"MQVY]bhqy{";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}