package ds

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestQueue(t *testing.T) {
	q := NewQueue[string](10)
	assert.Equal(t, 0, q.Length())
	q.Enqueue("first")
	assert.Equal(t, 1, q.Length())
	q.Enqueue("second")
	assert.Equal(t, 2, q.Length())
	assert.Equal(t, "first", q.Dequeue())
	assert.Equal(t, 1, q.Length())
	assert.Equal(t, "second", q.Dequeue())
	assert.Equal(t, 0, q.Length())
}
