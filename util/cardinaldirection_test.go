package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDirectionTranslate(t *testing.T) {
	// main 4 directions
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
	// diagonals
	{
		newRow, newCol := NorthEast.Translate(0, 0)
		assert.Equal(t, -1, newRow)
		assert.Equal(t, 1, newCol)
	}
	{
		newRow, newCol := SouthEast.Translate(0, 0)
		assert.Equal(t, 1, newRow)
		assert.Equal(t, 1, newCol)
	}
	{
		newRow, newCol := SouthWest.Translate(0, 0)
		assert.Equal(t, 1, newRow)
		assert.Equal(t, -1, newCol)
	}
	{
		newRow, newCol := NorthWest.Translate(0, 0)
		assert.Equal(t, -1, newRow)
		assert.Equal(t, -1, newCol)
	}
}

func TestString(t *testing.T) {
	assert.Equal(t, "North", North.String())
	assert.Equal(t, "NorthWest", NorthWest.String())
	assert.Equal(t, "South", South.String())
	assert.Equal(t, "SouthEast", SouthEast.String())
}
