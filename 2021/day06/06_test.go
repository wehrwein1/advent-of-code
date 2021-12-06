package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	testcase := parseAges("3,4,3,1,2")
	assert.Equal(t, 26, simulateLanternfish(testcase, 18))
	assert.Equal(t, 5934, simulateLanternfish(testcase, 80))
}
