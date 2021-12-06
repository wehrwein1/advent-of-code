package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := "3,4,3,1,2"
	assert.Equal(t, 26, len(simulateLanternfish(testcase, 18)))
	assert.Equal(t, []int{6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8}, simulateLanternfish(testcase, 18))
	assert.Equal(t, 5934, len(simulateLanternfish(testcase, 80)))
	// assert.Equal(t, 26984457539, len(simulateLanternfish(testcase, 256)))
}
