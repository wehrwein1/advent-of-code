package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSumInts(t *testing.T) {
	assert.Equal(t, SumInts(3, 66, 2, 7), 78, "sumInts() results different")

}

func TestMinInt(t *testing.T) {
	assert.Equal(t, MinInt(31, 66, 2, 7), 2, "minInt() results different")
}
