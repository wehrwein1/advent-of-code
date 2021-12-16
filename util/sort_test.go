package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSortedRuneSlice(t *testing.T) {
	assert.Equal(t, []rune{'a', 'b', 'c', 'd'}, RuneSlice([]rune{'d', 'a', 'c', 'b'}).Sorted())
}
