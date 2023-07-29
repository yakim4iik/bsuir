// Code generated from dnf.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser // dnf
import "github.com/antlr/antlr4/runtime/Go/antlr/v4"

// dnfListener is a complete listener for a parse tree produced by dnfParser.
type dnfListener interface {
	antlr.ParseTreeListener

	// EnterDnf is called when entering the dnf production.
	EnterDnf(c *DnfContext)

	// EnterNormal_disjunct is called when entering the normal_disjunct production.
	EnterNormal_disjunct(c *Normal_disjunctContext)

	// EnterConjuct is called when entering the conjuct production.
	EnterConjuct(c *ConjuctContext)

	// ExitDnf is called when exiting the dnf production.
	ExitDnf(c *DnfContext)

	// ExitNormal_disjunct is called when exiting the normal_disjunct production.
	ExitNormal_disjunct(c *Normal_disjunctContext)

	// ExitConjuct is called when exiting the conjuct production.
	ExitConjuct(c *ConjuctContext)
}
