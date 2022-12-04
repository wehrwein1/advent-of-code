package ds

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIntSet(t *testing.T) {
	s := NewSet()
	assert.Equal(t, 0, len(s.data))
	assert.Equal(t, false, s.Has(55))
	s.Put(88)
	assert.Equal(t, true, s.Has(88))
}

func TestUnion(t *testing.T) {
	assert.ElementsMatch(t, []rune{}, NewSet().Union(*NewSet('a', 'b', 'c')).Keys())
	assert.ElementsMatch(t, []rune{'b', 'd'}, NewSet('b', 'd').Union(*NewSet('a', 'b', 'c', 'd')).Keys())
}
