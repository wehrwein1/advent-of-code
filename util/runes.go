package util

import (
	"fmt"
	"strings"
)

func PrettyPrintRuneSlice(runes []rune, delim string, printBrackets bool) string {
	chars := []string{}
	for _, r := range runes {
		chars = append(chars, fmt.Sprintf("%c", r))
	}
	formatString := If(printBrackets).String("[%s]", "%s")
	return fmt.Sprintf(formatString, strings.Join(chars, delim))
}
