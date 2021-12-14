package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRuneStack(t *testing.T) {
	s := NewRuneStack()
	assert.Equal(t, true, s.IsEmpty())
	s.Push('a')
	assert.Equal(t, false, s.IsEmpty())
	assert.Equal(t, 'a', s.Peek())
	s.Push('b')
	assert.Equal(t, false, s.IsEmpty())
	s.Push('c')
	assert.Equal(t, 'c', s.Pop())
	assert.Equal(t, false, s.IsEmpty())
	assert.Equal(t, 'b', s.Pop())
	assert.Equal(t, false, s.IsEmpty())
	assert.Equal(t, 'a', s.Pop())
	assert.Equal(t, true, s.IsEmpty())
}
