// Code generated from dnf.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser // dnf
import "github.com/antlr/antlr4/runtime/Go/antlr/v4"

// BasednfListener is a complete listener for a parse tree produced by dnfParser.
type BasednfListener struct{}

var _ dnfListener = &BasednfListener{}

// VisitTerminal is called when a terminal node is visited.
func (s *BasednfListener) VisitTerminal(node antlr.TerminalNode) {}

// VisitErrorNode is called when an error node is visited.
func (s *BasednfListener) VisitErrorNode(node antlr.ErrorNode) {}

// EnterEveryRule is called when any rule is entered.
func (s *BasednfListener) EnterEveryRule(ctx antlr.ParserRuleContext) {}

// ExitEveryRule is called when any rule is exited.
func (s *BasednfListener) ExitEveryRule(ctx antlr.ParserRuleContext) {}

// EnterDnf is called when production dnf is entered.
func (s *BasednfListener) EnterDnf(ctx *DnfContext) {}

// ExitDnf is called when production dnf is exited.
func (s *BasednfListener) ExitDnf(ctx *DnfContext) {}

// EnterNormal_disjunct is called when production normal_disjunct is entered.
func (s *BasednfListener) EnterNormal_disjunct(ctx *Normal_disjunctContext) {}

// ExitNormal_disjunct is called when production normal_disjunct is exited.
func (s *BasednfListener) ExitNormal_disjunct(ctx *Normal_disjunctContext) {}

// EnterConjuct is called when production conjuct is entered.
func (s *BasednfListener) EnterConjuct(ctx *ConjuctContext) {}

// ExitConjuct is called when production conjuct is exited.
func (s *BasednfListener) ExitConjuct(ctx *ConjuctContext) {}
