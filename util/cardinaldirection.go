package util

import "fmt"

type Direction int

// https://www.educative.io/edpresso/what-is-an-enum-in-golang
const (
	North Direction = iota
	NorthEast
	East
	SouthEast
	South
	SouthWest
	West
	NorthWest
)

func (me Direction) String() string {
	return [...]string{"North", "NorthEast", "East", "SouthEast", "South", "SouthWest", "West", "NorthWest"}[me]
}

func (direction Direction) Translate(row int, col int) (newRow int, newCol int) {
	switch direction {
	case North:
		return row - 1, col
	case East:
		return row, col + 1
	case South:
		return row + 1, col
	case West:
		return row, col - 1
	default:
		panic(fmt.Sprintf("unhandled direction case: %s", direction.String()))
	}
}
