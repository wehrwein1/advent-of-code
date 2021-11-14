package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStringSplitToInts(t *testing.T) {
	assert.Equal(t, StringSplitToInts("2x3x4", "x"), []int{2, 3, 4})
}
