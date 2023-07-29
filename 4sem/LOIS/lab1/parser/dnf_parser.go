// Code generated from dnf.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser // dnf
import (
	"fmt"
	"strconv"
	"sync"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

// Suppress unused import errors
var _ = fmt.Printf
var _ = strconv.Itoa
var _ = sync.Once{}

type dnfParser struct {
	*antlr.BaseParser
}

var dnfParserStaticData struct {
	once                   sync.Once
	serializedATN          []int32
	literalNames           []string
	symbolicNames          []string
	ruleNames              []string
	predictionContextCache *antlr.PredictionContextCache
	atn                    *antlr.ATN
	decisionToDFA          []*antlr.DFA
}

func dnfParserInit() {
	staticData := &dnfParserStaticData
	staticData.literalNames = []string{
		"", "", "", "'\\/'", "'/\\'", "'!'", "'('", "')'",
	}
	staticData.symbolicNames = []string{
		"", "LITERAL", "VAR", "OR", "AND", "NOT", "OPB", "CLB",
	}
	staticData.ruleNames = []string{
		"dnf", "normal_disjunct", "conjuct",
	}
	staticData.predictionContextCache = antlr.NewPredictionContextCache()
	staticData.serializedATN = []int32{
		4, 1, 7, 46, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 1, 0, 1, 0, 1, 0, 1, 1,
		1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
		1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 29, 8, 1, 1, 2, 1, 2, 1, 2, 1,
		2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 44, 8, 2,
		1, 2, 0, 0, 3, 0, 2, 4, 0, 0, 47, 0, 6, 1, 0, 0, 0, 2, 28, 1, 0, 0, 0,
		4, 43, 1, 0, 0, 0, 6, 7, 3, 2, 1, 0, 7, 8, 5, 0, 0, 1, 8, 1, 1, 0, 0, 0,
		9, 29, 3, 4, 2, 0, 10, 11, 5, 6, 0, 0, 11, 12, 3, 4, 2, 0, 12, 13, 5, 3,
		0, 0, 13, 14, 3, 2, 1, 0, 14, 15, 5, 7, 0, 0, 15, 29, 1, 0, 0, 0, 16, 17,
		5, 6, 0, 0, 17, 18, 3, 2, 1, 0, 18, 19, 5, 3, 0, 0, 19, 20, 3, 4, 2, 0,
		20, 21, 5, 7, 0, 0, 21, 29, 1, 0, 0, 0, 22, 23, 5, 6, 0, 0, 23, 24, 3,
		4, 2, 0, 24, 25, 5, 3, 0, 0, 25, 26, 3, 4, 2, 0, 26, 27, 5, 7, 0, 0, 27,
		29, 1, 0, 0, 0, 28, 9, 1, 0, 0, 0, 28, 10, 1, 0, 0, 0, 28, 16, 1, 0, 0,
		0, 28, 22, 1, 0, 0, 0, 29, 3, 1, 0, 0, 0, 30, 44, 5, 1, 0, 0, 31, 32, 5,
		6, 0, 0, 32, 33, 3, 4, 2, 0, 33, 34, 5, 4, 0, 0, 34, 35, 5, 1, 0, 0, 35,
		36, 5, 7, 0, 0, 36, 44, 1, 0, 0, 0, 37, 38, 5, 6, 0, 0, 38, 39, 5, 1, 0,
		0, 39, 40, 5, 4, 0, 0, 40, 41, 3, 4, 2, 0, 41, 42, 5, 7, 0, 0, 42, 44,
		1, 0, 0, 0, 43, 30, 1, 0, 0, 0, 43, 31, 1, 0, 0, 0, 43, 37, 1, 0, 0, 0,
		44, 5, 1, 0, 0, 0, 2, 28, 43,
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

// dnfParserInit initializes any static state used to implement dnfParser. By default the
// static state used to implement the parser is lazily initialized during the first call to
// NewdnfParser(). You can call this function if you wish to initialize the static state ahead
// of time.
func DnfParserInit() {
	staticData := &dnfParserStaticData
	staticData.once.Do(dnfParserInit)
}

// NewdnfParser produces a new parser instance for the optional input antlr.TokenStream.
func NewdnfParser(input antlr.TokenStream) *dnfParser {
	DnfParserInit()
	this := new(dnfParser)
	this.BaseParser = antlr.NewBaseParser(input)
	staticData := &dnfParserStaticData
	this.Interpreter = antlr.NewParserATNSimulator(this, staticData.atn, staticData.decisionToDFA, staticData.predictionContextCache)
	this.RuleNames = staticData.ruleNames
	this.LiteralNames = staticData.literalNames
	this.SymbolicNames = staticData.symbolicNames
	this.GrammarFileName = "dnf.g4"

	return this
}

// dnfParser tokens.
const (
	dnfParserEOF     = antlr.TokenEOF
	dnfParserLITERAL = 1
	dnfParserVAR     = 2
	dnfParserOR      = 3
	dnfParserAND     = 4
	dnfParserNOT     = 5
	dnfParserOPB     = 6
	dnfParserCLB     = 7
)

// dnfParser rules.
const (
	dnfParserRULE_dnf             = 0
	dnfParserRULE_normal_disjunct = 1
	dnfParserRULE_conjuct         = 2
)

// IDnfContext is an interface to support dynamic dispatch.
type IDnfContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Normal_disjunct() INormal_disjunctContext
	EOF() antlr.TerminalNode

	// IsDnfContext differentiates from other interfaces.
	IsDnfContext()
}

type DnfContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyDnfContext() *DnfContext {
	var p = new(DnfContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = dnfParserRULE_dnf
	return p
}

func (*DnfContext) IsDnfContext() {}

func NewDnfContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *DnfContext {
	var p = new(DnfContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = dnfParserRULE_dnf

	return p
}

func (s *DnfContext) GetParser() antlr.Parser { return s.parser }

func (s *DnfContext) Normal_disjunct() INormal_disjunctContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(INormal_disjunctContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(INormal_disjunctContext)
}

func (s *DnfContext) EOF() antlr.TerminalNode {
	return s.GetToken(dnfParserEOF, 0)
}

func (s *DnfContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DnfContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *DnfContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(dnfListener); ok {
		listenerT.EnterDnf(s)
	}
}

func (s *DnfContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(dnfListener); ok {
		listenerT.ExitDnf(s)
	}
}

func (p *dnfParser) Dnf() (localctx IDnfContext) {
	this := p
	_ = this

	localctx = NewDnfContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 0, dnfParserRULE_dnf)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(6)
		p.Normal_disjunct()
	}
	{
		p.SetState(7)
		p.Match(dnfParserEOF)
	}

	return localctx
}

// INormal_disjunctContext is an interface to support dynamic dispatch.
type INormal_disjunctContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	AllConjuct() []IConjuctContext
	Conjuct(i int) IConjuctContext
	OPB() antlr.TerminalNode
	OR() antlr.TerminalNode
	Normal_disjunct() INormal_disjunctContext
	CLB() antlr.TerminalNode

	// IsNormal_disjunctContext differentiates from other interfaces.
	IsNormal_disjunctContext()
}

type Normal_disjunctContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyNormal_disjunctContext() *Normal_disjunctContext {
	var p = new(Normal_disjunctContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = dnfParserRULE_normal_disjunct
	return p
}

func (*Normal_disjunctContext) IsNormal_disjunctContext() {}

func NewNormal_disjunctContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Normal_disjunctContext {
	var p = new(Normal_disjunctContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = dnfParserRULE_normal_disjunct

	return p
}

func (s *Normal_disjunctContext) GetParser() antlr.Parser { return s.parser }

func (s *Normal_disjunctContext) AllConjuct() []IConjuctContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IConjuctContext); ok {
			len++
		}
	}

	tst := make([]IConjuctContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IConjuctContext); ok {
			tst[i] = t.(IConjuctContext)
			i++
		}
	}

	return tst
}

func (s *Normal_disjunctContext) Conjuct(i int) IConjuctContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IConjuctContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IConjuctContext)
}

func (s *Normal_disjunctContext) OPB() antlr.TerminalNode {
	return s.GetToken(dnfParserOPB, 0)
}

func (s *Normal_disjunctContext) OR() antlr.TerminalNode {
	return s.GetToken(dnfParserOR, 0)
}

func (s *Normal_disjunctContext) Normal_disjunct() INormal_disjunctContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(INormal_disjunctContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(INormal_disjunctContext)
}

func (s *Normal_disjunctContext) CLB() antlr.TerminalNode {
	return s.GetToken(dnfParserCLB, 0)
}

func (s *Normal_disjunctContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Normal_disjunctContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *Normal_disjunctContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(dnfListener); ok {
		listenerT.EnterNormal_disjunct(s)
	}
}

func (s *Normal_disjunctContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(dnfListener); ok {
		listenerT.ExitNormal_disjunct(s)
	}
}

func (p *dnfParser) Normal_disjunct() (localctx INormal_disjunctContext) {
	this := p
	_ = this

	localctx = NewNormal_disjunctContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 2, dnfParserRULE_normal_disjunct)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	p.SetState(28)
	p.GetErrorHandler().Sync(p)
	switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 0, p.GetParserRuleContext()) {
	case 1:
		{
			p.SetState(9)
			p.Conjuct()
		}

	case 2:
		{
			p.SetState(10)
			p.Match(dnfParserOPB)
		}
		{
			p.SetState(11)
			p.Conjuct()
		}
		{
			p.SetState(12)
			p.Match(dnfParserOR)
		}
		{
			p.SetState(13)
			p.Normal_disjunct()
		}
		{
			p.SetState(14)
			p.Match(dnfParserCLB)
		}

	case 3:
		{
			p.SetState(16)
			p.Match(dnfParserOPB)
		}
		{
			p.SetState(17)
			p.Normal_disjunct()
		}
		{
			p.SetState(18)
			p.Match(dnfParserOR)
		}
		{
			p.SetState(19)
			p.Conjuct()
		}
		{
			p.SetState(20)
			p.Match(dnfParserCLB)
		}

	case 4:
		{
			p.SetState(22)
			p.Match(dnfParserOPB)
		}
		{
			p.SetState(23)
			p.Conjuct()
		}
		{
			p.SetState(24)
			p.Match(dnfParserOR)
		}
		{
			p.SetState(25)
			p.Conjuct()
		}
		{
			p.SetState(26)
			p.Match(dnfParserCLB)
		}

	}

	return localctx
}

// IConjuctContext is an interface to support dynamic dispatch.
type IConjuctContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	LITERAL() antlr.TerminalNode
	OPB() antlr.TerminalNode
	Conjuct() IConjuctContext
	AND() antlr.TerminalNode
	CLB() antlr.TerminalNode

	// IsConjuctContext differentiates from other interfaces.
	IsConjuctContext()
}

type ConjuctContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyConjuctContext() *ConjuctContext {
	var p = new(ConjuctContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = dnfParserRULE_conjuct
	return p
}

func (*ConjuctContext) IsConjuctContext() {}

func NewConjuctContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ConjuctContext {
	var p = new(ConjuctContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = dnfParserRULE_conjuct

	return p
}

func (s *ConjuctContext) GetParser() antlr.Parser { return s.parser }

func (s *ConjuctContext) LITERAL() antlr.TerminalNode {
	return s.GetToken(dnfParserLITERAL, 0)
}

func (s *ConjuctContext) OPB() antlr.TerminalNode {
	return s.GetToken(dnfParserOPB, 0)
}

func (s *ConjuctContext) Conjuct() IConjuctContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IConjuctContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IConjuctContext)
}

func (s *ConjuctContext) AND() antlr.TerminalNode {
	return s.GetToken(dnfParserAND, 0)
}

func (s *ConjuctContext) CLB() antlr.TerminalNode {
	return s.GetToken(dnfParserCLB, 0)
}

func (s *ConjuctContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ConjuctContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ConjuctContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(dnfListener); ok {
		listenerT.EnterConjuct(s)
	}
}

func (s *ConjuctContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(dnfListener); ok {
		listenerT.ExitConjuct(s)
	}
}

func (p *dnfParser) Conjuct() (localctx IConjuctContext) {
	this := p
	_ = this

	localctx = NewConjuctContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, dnfParserRULE_conjuct)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.SetState(43)
	p.GetErrorHandler().Sync(p)
	switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 1, p.GetParserRuleContext()) {
	case 1:
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(30)
			p.Match(dnfParserLITERAL)
		}

	case 2:
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(31)
			p.Match(dnfParserOPB)
		}
		{
			p.SetState(32)
			p.Conjuct()
		}
		{
			p.SetState(33)
			p.Match(dnfParserAND)
		}
		{
			p.SetState(34)
			p.Match(dnfParserLITERAL)
		}
		{
			p.SetState(35)
			p.Match(dnfParserCLB)
		}

	case 3:
		p.EnterOuterAlt(localctx, 3)
		{
			p.SetState(37)
			p.Match(dnfParserOPB)
		}
		{
			p.SetState(38)
			p.Match(dnfParserLITERAL)
		}
		{
			p.SetState(39)
			p.Match(dnfParserAND)
		}
		{
			p.SetState(40)
			p.Conjuct()
		}
		{
			p.SetState(41)
			p.Match(dnfParserCLB)
		}

	}

	return localctx
}
