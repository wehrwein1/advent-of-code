package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPrettyPrintRuneSlice(t *testing.T) {
	assert.Equal(t, "[a b c]", PrettyPrintRuneSlice([]rune{'a', 'b', 'c'}, " ", true))
}
