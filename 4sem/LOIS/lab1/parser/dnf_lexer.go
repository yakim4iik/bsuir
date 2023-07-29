// Code generated from dnf.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser

import (
	"fmt"
	"sync"
	"unicode"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

// Suppress unused import error
var _ = fmt.Printf
var _ = sync.Once{}
var _ = unicode.IsLetter

type dnfLexer struct {
	*antlr.BaseLexer
	channelNames []string
	modeNames    []string
	// TODO: EOF string
}

var dnflexerLexerStaticData struct {
	once                   sync.Once
	serializedATN          []int32
	channelNames           []string
	modeNames              []string
	literalNames           []string
	symbolicNames          []string
	ruleNames              []string
	predictionContextCache *antlr.PredictionContextCache
	atn                    *antlr.ATN
	decisionToDFA          []*antlr.DFA
}

func dnflexerLexerInit() {
	staticData := &dnflexerLexerStaticData
	staticData.channelNames = []string{
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN",
	}
	staticData.modeNames = []string{
		"DEFAULT_MODE",
	}
	staticData.literalNames = []string{
		"", "", "", "'\\/'", "'/\\'", "'!'", "'('", "')'",
	}
	staticData.symbolicNames = []string{
		"", "LITERAL", "VAR", "OR", "AND", "NOT", "OPB", "CLB",
	}
	staticData.ruleNames = []string{
		"LITERAL", "VAR", "OR", "AND", "NOT", "OPB", "CLB",
	}
	staticData.predictionContextCache = antlr.NewPredictionContextCache()
	staticData.serializedATN = []int32{
		4, 0, 7, 37, 6, -1, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2,
		4, 7, 4, 2, 5, 7, 5, 2, 6, 7, 6, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3,
		0, 22, 8, 0, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4,
		1, 5, 1, 5, 1, 6, 1, 6, 0, 0, 7, 1, 1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13,
		7, 1, 0, 1, 1, 0, 65, 90, 37, 0, 1, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 5,
		1, 0, 0, 0, 0, 7, 1, 0, 0, 0, 0, 9, 1, 0, 0, 0, 0, 11, 1, 0, 0, 0, 0, 13,
		1, 0, 0, 0, 1, 21, 1, 0, 0, 0, 3, 23, 1, 0, 0, 0, 5, 25, 1, 0, 0, 0, 7,
		28, 1, 0, 0, 0, 9, 31, 1, 0, 0, 0, 11, 33, 1, 0, 0, 0, 13, 35, 1, 0, 0,
		0, 15, 22, 3, 3, 1, 0, 16, 17, 3, 11, 5, 0, 17, 18, 3, 9, 4, 0, 18, 19,
		3, 3, 1, 0, 19, 20, 3, 13, 6, 0, 20, 22, 1, 0, 0, 0, 21, 15, 1, 0, 0, 0,
		21, 16, 1, 0, 0, 0, 22, 2, 1, 0, 0, 0, 23, 24, 7, 0, 0, 0, 24, 4, 1, 0,
		0, 0, 25, 26, 5, 92, 0, 0, 26, 27, 5, 47, 0, 0, 27, 6, 1, 0, 0, 0, 28,
		29, 5, 47, 0, 0, 29, 30, 5, 92, 0, 0, 30, 8, 1, 0, 0, 0, 31, 32, 5, 33,
		0, 0, 32, 10, 1, 0, 0, 0, 33, 34, 5, 40, 0, 0, 34, 12, 1, 0, 0, 0, 35,
		36, 5, 41, 0, 0, 36, 14, 1, 0, 0, 0, 2, 0, 21, 0,
	}
	deserializer := antlr.NewATNDeserializer(nil)
	staticData.atn = deserializer.Deserialize(staticData.serializedATN)
	atn := staticData.atn
	staticData.decisionToDFA = make([]*antlr.DFA, len(atn.DecisionToState))
	decisionToDFA := staticData.decisionToDFA
	for index, state := range atn.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(state, index)
	}
}

// dnfLexerInit initializes any static state used to implement dnfLexer. By default the
// static state used to implement the lexer is lazily initialized during the first call to
// NewdnfLexer(). You can call this function if you wish to initialize the static state ahead
// of time.
func DnfLexerInit() {
	staticData := &dnflexerLexerStaticData
	staticData.once.Do(dnflexerLexerInit)
}

// NewdnfLexer produces a new lexer instance for the optional input antlr.CharStream.
func NewdnfLexer(input antlr.CharStream) *dnfLexer {
	DnfLexerInit()
	l := new(dnfLexer)
	l.BaseLexer = antlr.NewBaseLexer(input)
	staticData := &dnflexerLexerStaticData
	l.Interpreter = antlr.NewLexerATNSimulator(l, staticData.atn, staticData.decisionToDFA, staticData.predictionContextCache)
	l.channelNames = staticData.channelNames
	l.modeNames = staticData.modeNames
	l.RuleNames = staticData.ruleNames
	l.LiteralNames = staticData.literalNames
	l.SymbolicNames = staticData.symbolicNames
	l.GrammarFileName = "dnf.g4"
	// TODO: l.EOF = antlr.TokenEOF

	return l
}

// dnfLexer tokens.
const (
	dnfLexerLITERAL = 1
	dnfLexerVAR     = 2
	dnfLexerOR      = 3
	dnfLexerAND     = 4
	dnfLexerNOT     = 5
	dnfLexerOPB     = 6
	dnfLexerCLB     = 7
)
