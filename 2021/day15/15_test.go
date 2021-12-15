package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	assert.Equal(t, 40, computeDay(fileLines("../input/15_TEST.txt")))
}
