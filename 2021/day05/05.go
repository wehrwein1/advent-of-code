// https://adventofcode.com/2021/day/5
package main

import (
	"fmt"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
)

type Point = util.Point
type Vector = util.Vector

func parseLines(filename string) (vectors []Vector) {
	lines := util.FileLinesIncludeEmpty(filename)
	for _, line := range lines {
		if len(line) > 0 {
			tokens := strings.Split(line, " -> ")
			startTokens := util.StringSplitToInts(tokens[0], ",")
			endTokens := util.StringSplitToInts(tokens[1], ",")
			startX, startY := startTokens[0], startTokens[1]
			endX, endY := endTokens[0], endTokens[1]
			vectors = append(vectors, Vector{
				Start: Point{X: startX, Y: startY},
				End:   Point{X: endX, Y: endY}})
		}
	}
	return
}

func main() {
	vectors := parseLines("../input/05_INPUT.txt")
	println(fmt.Sprintf("part 1: count overlaps %d", countOverlaysPart1(vectors)))
	println(fmt.Sprintf("part 2: count overlaps %d", countOverlaysPart2(vectors)))
}

func countOverlaysPart1(vectors []Vector) (overlapsCount int) {
	return countOverlays(vectors, false)
}

func countOverlaysPart2(vectors []Vector) (overlapsCount int) {
	return countOverlays(vectors, true)
}

func countOverlays(vectors []Vector, includeDiagonals bool) (overlapsCount int) {
	// mark points
	visitedPointCounts := make(map[Point]int)
	for _, vector := range vectors {
		if !includeDiagonals && vector.IsDiagnonalLine() {
			// println(fmt.Sprintf("Vector %v skipped (diagonal)", vector))
			continue
		}
		// println(fmt.Sprintf("Vector %v", vector))
		for _, point := range vector.ToPoints() {
			// println(fmt.Sprintf(" visited point %v", point))
			val, ok := visitedPointCounts[point]
			if ok {
				visitedPointCounts[point] = val + 1
			} else {
				visitedPointCounts[point] = 1
			}
		}
	}
	// count
	for _, count := range visitedPointCounts {
		// println(fmt.Sprintf("state: visited %v count=%d", point, count))
		if count > 1 {
			overlapsCount += 1
		}
	}
	return
}
