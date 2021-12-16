package ds

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIntSet(t *testing.T) {
	s := NewIntSet()
	assert.Equal(t, 0, len(s.data))
	assert.Equal(t, false, s.Has(55))
	s.Put(88)
	assert.Equal(t, true, s.Has(88))
}

func TestRuneSet(t *testing.T) {
	s := NewRuneSet()
	assert.Equal(t, "[]", s.String())
	s.Put('a', 'b')
	assert.ElementsMatch(t, []rune{'a', 'b'}, s.Keys())
	assert.Contains(t, s.String(), "a") // sets are unordered, could be "[a b]" or "[b a]" depending on impl
	assert.Contains(t, s.String(), "b") // sets are unordered, could be "[a b]" or "[b a]" depending on impl
	s.Remove('a')
	assert.Equal(t, false, s.Has('a'))
	assert.Equal(t, "[b]", s.String())
	s.Remove('b')
	assert.Equal(t, true, s.IsEmpty())
}
