package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBinaryStringToDecimal(t *testing.T) {
	assert.Equal(t, int64(15), BinaryStringToDecimal("1111", 32))
}
