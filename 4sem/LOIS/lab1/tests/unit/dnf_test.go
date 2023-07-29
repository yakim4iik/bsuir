package unittests

import (
	"lab/internal/app"
	"testing"
)

func TestIsDnf(t *testing.T) {
	formulas := []string{
		"((A/\\B)\\/(C\\/D))",
		"(A\\/B)",
		"((A\\/B)\\/(C/\\D))",
		"((A/\\B)\\/(C/\\D))",
		"(A/\\B)",
		"((A/\\B)\\/C)",
		"((A/\\B)\\/D)",
		"((A/\\B)/\\D)",
		"(B/\\((A/\\B)/\\D))",
		"(B\\/((A/\\B)/\\D))",
		"(!B)",
		"(A/\\(!B))",
	}
	for _, formula := range formulas {
		checker := app.NewDnfChecker(formula)
		lexerErrors, parserErrors := checker.Result()

		AssertEqual(t, len(lexerErrors), 0)
		AssertEqual(t, len(parserErrors), 0)
	}
}
