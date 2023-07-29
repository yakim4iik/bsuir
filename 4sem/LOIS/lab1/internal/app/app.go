package app

import (
	"lab/parser"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

type Checker interface {
	Result() string
}

type DnfChecker struct {
	formula string
}

func NewDnfChecker(formula string) *DnfChecker {
	return &DnfChecker{
		formula,
	}
}

func (ch *DnfChecker) Result() ([]*CustomSyntaxError, []*CustomSyntaxError) {
	lexerErrors := &CustomErrorListener{}

	input := antlr.NewInputStream(ch.formula)
	dnf_lexer := parser.NewdnfLexer(input)

	dnf_lexer.RemoveErrorListeners()
	dnf_lexer.AddErrorListener(lexerErrors)

	parserErrors := &CustomErrorListener{}

	stream := antlr.NewCommonTokenStream(dnf_lexer, 0)
	dnf_parser := parser.NewdnfParser(stream)

	dnf_parser.RemoveErrorListeners()
	dnf_parser.AddErrorListener(parserErrors)

	dnf_parser.Dnf()

	return lexerErrors.Errors, parserErrors.Errors
}
