package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestAllTrue(t *testing.T) {
	assert.Equal(t, false, AllTrue())
	assert.Equal(t, true, AllTrue(true))
	assert.Equal(t, true, AllTrue(true, true, true))
	assert.Equal(t, false, AllTrue(false, true, true))
	assert.Equal(t, false, AllTrue(true, false, true))
	assert.Equal(t, false, AllTrue(true, true, true, false))
	assert.Equal(t, false, AllTrue(false))
}
