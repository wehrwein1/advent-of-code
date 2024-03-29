package ds

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIntSet(t *testing.T) {
	s := NewSet[int]()
	assert.Equal(t, 0, len(s.data))
	assert.Equal(t, false, s.Has(55))
	s.Put(88)
	assert.Equal(t, true, s.Has(88))
}

func TestIntersection(t *testing.T) {
	assert.ElementsMatch(t, []rune{}, NewSet[rune]().Intersection(*NewSet('a', 'b', 'c')).Keys())
	assert.ElementsMatch(t, []rune{}, NewSet('a', 'b', 'c').Intersection(*NewSet('x', 'y', 'z')).Keys())
	assert.ElementsMatch(t, []rune{'a', 'b'}, NewSet('a', 'b', 'c').Intersection(*NewSet('_', 'b', 'a')).Keys())
}
