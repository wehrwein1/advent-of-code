package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStringSplitToInts(t *testing.T) {
	assert.Equal(t, StringSplitToInts("2x3x4", "x"), []int{2, 3, 4})
}

func TestStringsToInts(t *testing.T) {
	assert.Equal(t, []int{2, 3, 4, 6}, StringsToInts([]string{"2", "3", "4", "6"}))
}
