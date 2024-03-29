package ds

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStack(t *testing.T) {
	s := NewStack[rune]()
	assert.Equal(t, true, s.IsEmpty())
	assert.Equal(t, 0, s.Size())
	s.Push('a')
	assert.Equal(t, false, s.IsEmpty())
	assert.Equal(t, 1, s.Size())
	assert.Equal(t, 'a', s.Peek())
	s.Push('b')
	assert.Equal(t, false, s.IsEmpty())
	s.Push('c')
	assert.Equal(t, 'c', s.Pop())
	assert.Equal(t, 2, s.Size())
	assert.Equal(t, false, s.IsEmpty())
	assert.Equal(t, 'b', s.Pop())
	assert.Equal(t, false, s.IsEmpty())
	assert.Equal(t, 'a', s.Pop())
	assert.Equal(t, true, s.IsEmpty())
	assert.Equal(t, 0, s.Size())
}
