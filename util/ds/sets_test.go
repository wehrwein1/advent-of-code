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
