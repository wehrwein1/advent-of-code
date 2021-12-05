package util

import "fmt"

// Coordinate system, x,y
// (0, 0)     +x   (0+x, y)
//
//  +y
//
// (0+y, 0)        (0+x, 0+y)

type Vector struct {
	Start Point
	End   Point
}

type Point struct {
	X int
	Y int
}

func NewPoint(xy ...int) *Point { // syntax: https://stackoverflow.com/a/18125682/3633993
	if len(xy) != 2 {
		panic(fmt.Sprintf("invalid data len %d", len(xy)))
	}
	return &Point{X: xy[0], Y: xy[1]}
}

func NewVector(x1y1x2y2 ...int) *Vector { // syntax: https://stackoverflow.com/a/18125682/3633993
	if len(x1y1x2y2) != 4 {
		panic(fmt.Sprintf("invalid data len %d", len(x1y1x2y2)))
	}
	return &Vector{Start: Point{X: x1y1x2y2[0], Y: x1y1x2y2[1]}, End: Point{X: x1y1x2y2[2], Y: x1y1x2y2[3]}}
}

func (v Vector) IsDiagnonalLine() bool {
	return (v.Start.X != v.End.X) && (v.Start.Y != v.End.Y)
}

func (v Vector) IsHorizontalLine() bool {
	return !v.IsSinglePoint() && (v.Start.Y == v.End.Y)
}

func (v Vector) IsVerticalLine() bool {
	return !v.IsSinglePoint() && (v.Start.X == v.End.X)
}

func (v Vector) IsSinglePoint() bool {
	return (v.Start.X == v.End.X) && (v.Start.Y == v.End.Y)
}

func (v Vector) ToPoints() (points []Point) {
	if v.IsSinglePoint() {
		return []Point{v.Start}
	}
	x1, y1, x2, y2 := v.Start.X, v.Start.Y, v.End.X, v.End.Y
	if v.IsHorizontalLine() {
		y := y1      // vary x, y constant
		if x1 > x2 { // enforce x2 > x1 relation for loop increment
			temp := x1
			x1 = x2
			x2 = temp
		}
		for x := x1; x <= x2; x++ {
			points = append(points, Point{X: x, Y: y})
		}
		return
	}
	if v.IsVerticalLine() {
		x := x1      // vary y, x constant
		if y1 > y2 { // enforce y2 > y1 relation for loop increment
			temp := y1
			y1 = y2
			y2 = temp
		}
		for y := y1; y <= y2; y++ {
			points = append(points, Point{X: x, Y: y})
		}
		return
	}
	if v.IsDiagnonalLine() {
		xvals := []int{}
		if x2 > x1 { // asc X
			for x := x1; x <= x2; x++ {
				xvals = append(xvals, x)
			}
		} else { // desc X
			for x := x1; x >= x2; x-- {
				xvals = append(xvals, x)
			}
		}
		yvals := []int{}
		if y2 > y1 { // asc Y
			for y := y1; y <= y2; y++ {
				yvals = append(yvals, y)
			}
		} else { // desc Y
			for y := y1; y >= y2; y-- {
				yvals = append(yvals, y)
			}
		}
		// zip x and y vals together as points
		for i := 0; i < len(xvals); i++ {
			points = append(points, *NewPoint(xvals[i], yvals[i]))
		}
		return
	}
	panic("unknown vector case not implemented")
}
