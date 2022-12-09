// https://adventofcode.com/2022/day/8
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/ds"
)

type ProblemPart int

const (
	Part1 ProblemPart = iota
	Part2
)

var max = util.MaxInt

var product = util.ProductInts

// var all = util.AllTrue
var fileLines = util.FileLinesSkipEmpty
var get2dIntArray = util.StringsToInt2dArray

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/08_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/08_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) int {
	for _, line := range lines {
		println(line)
	}
	grid := get2dIntArray(lines)
	count := 0
	NWES := []util.Direction{util.North, util.West, util.East, util.South}
	allScenicScores := ds.NewSet[int]()
	for r := 1; r < util.RowCount(grid)-1; r++ {
		for c := 1; c < util.ColCount(grid)-1; c++ {
			treeHeight := grid[r][c]
			println(fmt.Sprintf("(%d,%d) %d", r, c, treeHeight))
			treeViewingDistances := []int{}
			for _, direction_ := range NWES {
				direction := util.Direction(direction_)
				directionViewableHeights := util.Int2dArrayWalk(grid, r, c, direction)
				isVisible := treeHeight > max(directionViewableHeights...)
				// part 2
				viewingDistance := 0
				for _, viewedHeight := range directionViewableHeights {
					viewingDistance += 1
					if viewedHeight >= treeHeight {
						break
					}
				}
				treeViewingDistances = append(treeViewingDistances, viewingDistance)
				println(fmt.Sprintf(" %-6s %v %t %d", direction, directionViewableHeights, isVisible, viewingDistance))
				if isVisible {
					count += 1
					if part == Part1 {
						break
					}
				}
			}
			if part == Part2 {
				scenicScore := product(treeViewingDistances...)
				allScenicScores.Put(scenicScore)
				println(fmt.Sprintf(" ScenicScore %d", scenicScore))
			}
		}
	}
	// part 1
	if part == Part1 {
		dim := util.RowCount(grid)
		edgeTreesCount := 4*dim - 4 // -1 for each corner
		return count + edgeTreesCount
	}
	// part 2
	return max(allScenicScores.Keys()...)
}
