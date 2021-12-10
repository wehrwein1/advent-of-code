package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDirectionTranslate(t *testing.T) {
	{
		newRow, newCol := North.Translate(0, 0)
		assert.Equal(t, -1, newRow)
		assert.Equal(t, 0, newCol)
	}
	{
		newRow, newCol := East.Translate(0, 0)
		assert.Equal(t, 0, newRow)
		assert.Equal(t, 1, newCol)
	}
	{
		newRow, newCol := South.Translate(0, 0)
		assert.Equal(t, 1, newRow)
		assert.Equal(t, 0, newCol)
	}
	{
		newRow, newCol := West.Translate(0, 0)
		assert.Equal(t, 0, newRow)
		assert.Equal(t, -1, newCol)
	}
	var panicMsg string
	defer func() { // defer() has stack semantics, push first = run second
		assert.Equal(t, "unhandled direction case: NorthEast", panicMsg, "panic() msg different")
	}()
	defer func() { // defer() has stack semantics, push last = run first. Intent: basically try/catch
		panicInfo := recover()
		panicMsg = panicInfo.(string)
	}()
	NorthEast.Translate(0, 0)
}
