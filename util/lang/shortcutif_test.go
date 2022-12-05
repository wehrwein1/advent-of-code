package lang

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestShortcutIfInt(t *testing.T) {
	month := 3
	day := 15
	assert.Equal(t, day, If(month > day).Int(month, day))   // basically max()
	assert.Equal(t, month, If(month < day).Int(month, day)) // basically min()
}
