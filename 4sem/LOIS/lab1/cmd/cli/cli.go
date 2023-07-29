package cli

import (
	"fmt"

	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"

	"lab/internal/app"
)

var formula string

var rootCmd = &cobra.Command{
	Use:   "check-dnf",
	Short: "Formula checker app for dnf",
	Long: `Formula checker app for dnf base on antlr4 framework. The work was performed by students
		- Yakimovich Ilya <>
		- Rutkovskiy Aleksandr <>
	`,
	Run: func(cmd *cobra.Command, args []string) {
		checker := app.NewDnfChecker(formula)
		lexerErrors, parserErrors := checker.Result()
		checkIsDnf(lexerErrors, parserErrors)
	},
}

func checkIsDnf(lexerErrors, parserErrors []*app.CustomSyntaxError) {
	if len(lexerErrors) > 0 {
		fmt.Printf("Lexer %d errors found\n", len(lexerErrors))
		for _, e := range lexerErrors {
			fmt.Println("\t", e.Error())
		}
	}

	if len(parserErrors) > 0 {
		fmt.Printf("Parser %d errors found\n", len(parserErrors))
		for _, e := range parserErrors {
			fmt.Println("\t", e.Error())
		}
	}

	if len(lexerErrors) == 0 && len(parserErrors) == 0 {
		fmt.Println("Formula is DNF")
	}
}

func Execute() {
	cobra.CheckErr(rootCmd.Execute())
}

func init() {
	rootCmd.PersistentFlags().StringVar(&formula, "formula", "", "formula for dnf check")

	log.SetFormatter(&log.TextFormatter{
		DisableColors: true,
		FullTimestamp: true,
	})
}
