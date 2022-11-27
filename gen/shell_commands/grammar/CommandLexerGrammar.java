// Generated from /Users/adityaparashar/UCL/Year2/COMP0010/CW/python-shell-p19/src/shell_commands/grammar/CommandLexerGrammar.g4 by ANTLR 4.10.1
package shell_commands.grammar;
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommandLexerGrammar extends Lexer {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SQ=1, DQ=2, BQ=3, UNQUOTED=4, SEMICOLON=5, GREATER_THAN=6, LESS_THAN=7, 
		NEWLINE=8, PIPE=9, WHITESPACE=10, SQ_MID=11, DQ_MID=12, BQ_MID=13, SQ_END=14, 
		DQ_END=15, BQ_END=16;
	public static final int
		SQ_MODE=1, DQ_MODE=2, BQ_MODE=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "SQ_MODE", "DQ_MODE", "BQ_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SINGLE_QUOTE", "DOUBLE_QUOTE", "BACKQUOTE", "UNQUOTED", "SEMICOLON", 
			"GREATER_THAN", "LESS_THAN", "NEWLINE", "PIPE", "WHITESPACE", "SQ_START", 
			"DQ_START", "BQ_START", "SQ_MID", "SQ_END", "DQ_MID", "ENTER_BQ", "DQ_END", 
			"BQ_MID", "BQ_END"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "';'", "'>'", "'<'", "'\\n'", "'|'", null, 
			null, null, null, "'''", "'\"'", "'`'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SQ", "DQ", "BQ", "UNQUOTED", "SEMICOLON", "GREATER_THAN", "LESS_THAN", 
			"NEWLINE", "PIPE", "WHITESPACE", "SQ_MID", "DQ_MID", "BQ_MID", "SQ_END", 
			"DQ_END", "BQ_END"
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


	public CommandLexerGrammar(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CommandLexerGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0010x\u0006\uffff\uffff\u0006\uffff\uffff\u0006\uffff\uffff"+
		"\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0004\u00034\b\u0003\u000b\u0003"+
		"\f\u00035\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0004\tC"+
		"\b\t\u000b\t\f\tD\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\r\u0004\rW\b\r\u000b\r\f\rX\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000fa\b"+
		"\u000f\u000b\u000f\f\u000fb\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0004\u0012p\b\u0012\u000b\u0012\f\u0012q\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0000\u0000\u0014\u0004"+
		"\u0000\u0006\u0000\b\u0000\n\u0004\f\u0005\u000e\u0006\u0010\u0007\u0012"+
		"\b\u0014\t\u0016\n\u0018\u0000\u001a\u0000\u001c\u0000\u001e\u000b \u000e"+
		"\"\f$\u0000&\u000f(\r*\u0010\u0004\u0000\u0001\u0002\u0003\u0005\b\u0000"+
		"\t\n  \"\"\'\';<>>``||\u0002\u0000\t\t  \u0002\u0000\n\n\'\'\u0003\u0000"+
		"\n\n\"\"``\u0002\u0000\n\n``v\u0000\n\u0001\u0000\u0000\u0000\u0000\f"+
		"\u0001\u0000\u0000\u0000\u0000\u000e\u0001\u0000\u0000\u0000\u0000\u0010"+
		"\u0001\u0000\u0000\u0000\u0000\u0012\u0001\u0000\u0000\u0000\u0000\u0014"+
		"\u0001\u0000\u0000\u0000\u0000\u0016\u0001\u0000\u0000\u0000\u0000\u0018"+
		"\u0001\u0000\u0000\u0000\u0000\u001a\u0001\u0000\u0000\u0000\u0000\u001c"+
		"\u0001\u0000\u0000\u0000\u0001\u001e\u0001\u0000\u0000\u0000\u0001 \u0001"+
		"\u0000\u0000\u0000\u0002\"\u0001\u0000\u0000\u0000\u0002$\u0001\u0000"+
		"\u0000\u0000\u0002&\u0001\u0000\u0000\u0000\u0003(\u0001\u0000\u0000\u0000"+
		"\u0003*\u0001\u0000\u0000\u0000\u0004,\u0001\u0000\u0000\u0000\u0006."+
		"\u0001\u0000\u0000\u0000\b0\u0001\u0000\u0000\u0000\n3\u0001\u0000\u0000"+
		"\u0000\f7\u0001\u0000\u0000\u0000\u000e9\u0001\u0000\u0000\u0000\u0010"+
		";\u0001\u0000\u0000\u0000\u0012=\u0001\u0000\u0000\u0000\u0014?\u0001"+
		"\u0000\u0000\u0000\u0016B\u0001\u0000\u0000\u0000\u0018F\u0001\u0000\u0000"+
		"\u0000\u001aK\u0001\u0000\u0000\u0000\u001cP\u0001\u0000\u0000\u0000\u001e"+
		"V\u0001\u0000\u0000\u0000 Z\u0001\u0000\u0000\u0000\"`\u0001\u0000\u0000"+
		"\u0000$d\u0001\u0000\u0000\u0000&i\u0001\u0000\u0000\u0000(o\u0001\u0000"+
		"\u0000\u0000*s\u0001\u0000\u0000\u0000,-\u0005\'\u0000\u0000-\u0005\u0001"+
		"\u0000\u0000\u0000./\u0005\"\u0000\u0000/\u0007\u0001\u0000\u0000\u0000"+
		"01\u0005`\u0000\u00001\t\u0001\u0000\u0000\u000024\b\u0000\u0000\u0000"+
		"32\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u000053\u0001\u0000\u0000"+
		"\u000056\u0001\u0000\u0000\u00006\u000b\u0001\u0000\u0000\u000078\u0005"+
		";\u0000\u00008\r\u0001\u0000\u0000\u00009:\u0005>\u0000\u0000:\u000f\u0001"+
		"\u0000\u0000\u0000;<\u0005<\u0000\u0000<\u0011\u0001\u0000\u0000\u0000"+
		"=>\u0005\n\u0000\u0000>\u0013\u0001\u0000\u0000\u0000?@\u0005|\u0000\u0000"+
		"@\u0015\u0001\u0000\u0000\u0000AC\u0007\u0001\u0000\u0000BA\u0001\u0000"+
		"\u0000\u0000CD\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000DE\u0001"+
		"\u0000\u0000\u0000E\u0017\u0001\u0000\u0000\u0000FG\u0003\u0004\u0000"+
		"\u0000GH\u0001\u0000\u0000\u0000HI\u0006\n\u0000\u0000IJ\u0006\n\u0001"+
		"\u0000J\u0019\u0001\u0000\u0000\u0000KL\u0003\u0006\u0001\u0000LM\u0001"+
		"\u0000\u0000\u0000MN\u0006\u000b\u0002\u0000NO\u0006\u000b\u0003\u0000"+
		"O\u001b\u0001\u0000\u0000\u0000PQ\u0003\b\u0002\u0000QR\u0001\u0000\u0000"+
		"\u0000RS\u0006\f\u0004\u0000ST\u0006\f\u0005\u0000T\u001d\u0001\u0000"+
		"\u0000\u0000UW\b\u0002\u0000\u0000VU\u0001\u0000\u0000\u0000WX\u0001\u0000"+
		"\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y\u001f"+
		"\u0001\u0000\u0000\u0000Z[\u0005\'\u0000\u0000[\\\u0001\u0000\u0000\u0000"+
		"\\]\u0006\u000e\u0000\u0000]^\u0006\u000e\u0006\u0000^!\u0001\u0000\u0000"+
		"\u0000_a\b\u0003\u0000\u0000`_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000"+
		"\u0000b`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000c#\u0001\u0000"+
		"\u0000\u0000de\u0003\b\u0002\u0000ef\u0001\u0000\u0000\u0000fg\u0006\u0010"+
		"\u0004\u0000gh\u0006\u0010\u0005\u0000h%\u0001\u0000\u0000\u0000ij\u0005"+
		"\"\u0000\u0000jk\u0001\u0000\u0000\u0000kl\u0006\u0011\u0002\u0000lm\u0006"+
		"\u0011\u0006\u0000m\'\u0001\u0000\u0000\u0000np\b\u0004\u0000\u0000on"+
		"\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000"+
		"\u0000qr\u0001\u0000\u0000\u0000r)\u0001\u0000\u0000\u0000st\u0005`\u0000"+
		"\u0000tu\u0001\u0000\u0000\u0000uv\u0006\u0013\u0004\u0000vw\u0006\u0013"+
		"\u0006\u0000w+\u0001\u0000\u0000\u0000\t\u0000\u0001\u0002\u00035DXbq"+
		"\u0007\u0007\u0001\u0000\u0005\u0001\u0000\u0007\u0002\u0000\u0005\u0002"+
		"\u0000\u0007\u0003\u0000\u0005\u0003\u0000\u0004\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}