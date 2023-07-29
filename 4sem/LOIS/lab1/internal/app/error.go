package app

import (
	"fmt"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

type CustomSyntaxError struct {
	line, column int
	msg          string
}

func (e *CustomSyntaxError) Error() string {
	return fmt.Sprintf("%v:%v %s", e.line, e.column, e.msg)
}

type CustomErrorListener struct {
	*antlr.DefaultErrorListener // Embed default which ensures we fit the interface
	Errors                      []*CustomSyntaxError
}

func (c *CustomErrorListener) SyntaxError(recognizer antlr.Recognizer, offendingSymbol interface{}, line, column int, msg string, e antlr.RecognitionException) {
	c.Errors = append(c.Errors, &CustomSyntaxError{
		line:   line,
		column: column,
		msg:    msg,
	})
}
