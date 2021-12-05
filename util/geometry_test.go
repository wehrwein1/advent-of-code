package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func horizontalLine() Vector {
	return Vector{Start: Point{1, 2}, End: Point{8, 2}}
}

func verticalLine() Vector {
	return Vector{Start: Point{3, 0}, End: Point{3, 1}}
}

func diagonalLine() Vector {
	return Vector{Start: Point{9, 7}, End: Point{7, 9}}
}

func singlePoint() Vector {
	return Vector{Start: Point{8, 8}, End: Point{8, 8}}
}

func TestVectorIsDiagonal(t *testing.T) {
	assert.Equal(t, false, horizontalLine().IsDiagnonalLine())
	assert.Equal(t, false, verticalLine().IsDiagnonalLine())
	assert.Equal(t, true, diagonalLine().IsDiagnonalLine())
	assert.Equal(t, false, singlePoint().IsDiagnonalLine())
}

func TestVectorIsHorizontal(t *testing.T) {
	assert.Equal(t, true, horizontalLine().IsHorizontalLine())
	assert.Equal(t, false, verticalLine().IsHorizontalLine())
	assert.Equal(t, false, diagonalLine().IsHorizontalLine())
	assert.Equal(t, false, singlePoint().IsHorizontalLine())
}

func TestVectorIsVertical(t *testing.T) {
	assert.Equal(t, false, horizontalLine().IsVerticalLine())
	assert.Equal(t, true, verticalLine().IsVerticalLine())
	assert.Equal(t, false, diagonalLine().IsVerticalLine())
	assert.Equal(t, false, singlePoint().IsVerticalLine())
}

func TestVectorIsSinglePoint(t *testing.T) {
	assert.Equal(t, false, horizontalLine().IsSinglePoint())
	assert.Equal(t, false, verticalLine().IsSinglePoint())
	assert.Equal(t, false, diagonalLine().IsSinglePoint())
	assert.Equal(t, true, singlePoint().IsSinglePoint())
}

func TestVectorToPointsVerticalLine(t *testing.T) {
	verticalAsc := NewVector(1, 1, 1, 3)
	verticalDesc := NewVector(1, 3, 1, 1)
	assert.Equal(t, true, verticalAsc.IsVerticalLine())
	assert.Equal(t, true, verticalDesc.IsVerticalLine())
	assert.Equal(t, []Point{*NewPoint(1, 1), *NewPoint(1, 2), *NewPoint(1, 3)}, verticalAsc.ToPoints())
	assert.Equal(t, []Point{*NewPoint(1, 1), *NewPoint(1, 2), *NewPoint(1, 3)}, verticalDesc.ToPoints())
}

func TestVectorToPointsHorizontalLine(t *testing.T) {
	horizontalAsc := NewVector(7, 2, 9, 2)
	horizontalDesc := NewVector(9, 7, 7, 7)
	assert.Equal(t, true, horizontalAsc.IsHorizontalLine())
	assert.Equal(t, true, horizontalDesc.IsHorizontalLine())
	assert.Equal(t, []Point{*NewPoint(7, 2), *NewPoint(8, 2), *NewPoint(9, 2)}, horizontalAsc.ToPoints())
	assert.Equal(t, []Point{*NewPoint(7, 7), *NewPoint(8, 7), *NewPoint(9, 7)}, horizontalDesc.ToPoints())
}

func TestVectorToPointsDiagonal(t *testing.T) {
	{
		diagonalSE := NewVector(1, 1, 3, 3)
		assert.Equal(t, true, diagonalSE.IsDiagnonalLine())
		assert.Equal(t, []Point{*NewPoint(1, 1), *NewPoint(2, 2), *NewPoint(3, 3)}, diagonalSE.ToPoints())
	}
	{
		diagonalSW := NewVector(9, 7, 7, 9)
		assert.Equal(t, true, diagonalSW.IsDiagnonalLine())
		assert.Equal(t, []Point{*NewPoint(9, 7), *NewPoint(8, 8), *NewPoint(7, 9)}, diagonalSW.ToPoints())
	}
	{
		diagonalNE := NewVector(0, 3, 2, 1)
		assert.Equal(t, true, diagonalNE.IsDiagnonalLine())
		assert.Equal(t, []Point{*NewPoint(0, 3), *NewPoint(1, 2), *NewPoint(2, 1)}, diagonalNE.ToPoints())
	}
	{
		diagonalNW := NewVector(5, 5, 3, 3)
		assert.Equal(t, true, diagonalNW.IsDiagnonalLine())
		assert.Equal(t, []Point{*NewPoint(5, 5), *NewPoint(4, 4), *NewPoint(3, 3)}, diagonalNW.ToPoints())
	}
}

func TestVectorToPointsSinglePoint(t *testing.T) {
	assert.Equal(t, []Point{*NewPoint(3, 7)}, NewVector(3, 7, 3, 7).ToPoints())
}
