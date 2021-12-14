package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDay(t *testing.T) {
	assert.Equal(t, -1, computeDay(fileLines("../input/10_TEST.txt")))
}