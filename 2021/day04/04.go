// https://adventofcode.com/2021/day/4
package main

import (
	"fmt"

	"github.com/wehrwein1/advent-of-code/util"
)

var sum = util.SumInts

var returnFirst = func(scores []int) int { return scores[0] }
var returnLast = func(scores []int) int { return scores[len(scores)-1] }

func computeWinningScorePart1(calledNumbers []int, boards [][][]int) int {
	return computeWinningScore(calledNumbers, boards, returnFirst)
}

func computeWinningScorePart2(calledNumbers []int, boards [][][]int) int {
	return computeWinningScore(calledNumbers, boards, returnLast)
}

func computeWinningScore(calledNumbers []int, boards [][][]int, scoreSelector func([]int) int) int {
	println(fmt.Sprintf("called numbers: %v", calledNumbers))
	println(fmt.Sprintf("boards: %d", len(boards)))
	printBoards(boards)
	boardCount := len(boards)
	dim := len(boards[0])
	boardsMarks := make([][][]bool, boardCount)
	for i := 0; i < boardCount; i++ {
		boardsMarks[i] = make([][]bool, dim)
		for j := 0; j < dim; j++ {
			boardsMarks[i][j] = make([]bool, dim)
		}
	}
	winningBoards := []int{}
	winningScores := []int{}
	for _, calledNumber := range calledNumbers {
		for i, board := range boards {
			for j, row := range board {
				for k, cell := range row {
					if cell == calledNumber {
						boardsMarks[i][j][k] = true // board i, row j, col k
						if isBingo(boardsMarks[i]) && !util.IntSliceContains(winningBoards, i) {
							score := sum(unmarkedNumbers(boards[i], boardsMarks[i])...) * calledNumber
							winningScores = append(winningScores, score)
							winningBoards = append(winningBoards, i)
							println(fmt.Sprintf("Winner board %d calledNumber %d score %d", i, calledNumber, score))
						}
					}
				}
			}
		}
	}
	winningScore := scoreSelector(winningScores)
	return winningScore
}

func unmarkedNumbers(board [][]int, boardMarks [][]bool) (unmarkedNumbers []int) {
	dim := len(board[0])
	for i := 0; i < dim; i++ {
		for j := 0; j < dim; j++ {
			isUnmarked := !boardMarks[i][j]
			if isUnmarked {
				unmarkedNumbers = append(unmarkedNumbers, board[i][j])
			}
		}
	}
	return
}

func isBingo(boardMarks [][]bool) bool {
	rowCount := len(boardMarks)
	colCount := len(boardMarks[0])
	if rowCount == 0 || colCount == 0 || (rowCount != colCount) {
		panic(fmt.Sprintf("invalid board dimensions %d x %d", rowCount, colCount))
	}
	// check rows
	for _, row := range boardMarks {
		allTrue := true
		for _, cell := range row {
			allTrue = allTrue && cell
		}
		if allTrue {
			return true
		}
	}
	// check cols
	for colIndex := 0; colIndex < colCount; colIndex++ {
		allTrue := true
		for rowIndex := 0; rowIndex < rowCount; rowIndex++ {
			allTrue = allTrue && boardMarks[rowIndex][colIndex]
		}
		if allTrue {
			return true
		}
	}
	return false
}

func parseBoards(boardPartitions [][]string) (boards [][][]int) {
	for _, board := range boardPartitions {
		var rows [][]int
		for _, row := range board {
			rows = append(rows, util.StringSplitToIntsWhitespace(row))
		}
		boards = append(boards, rows)
	}
	return
}

func printBoards(boards [][][]int) {
	for i, board := range boards {
		println(fmt.Sprintf("board[%d]:", i))
		for _, row := range board {
			println(fmt.Sprintf("%v", row))
		}
		println()
	}
}

func loadBingoData(filename string) (calledNumbers []int, boards [][][]int) {
	partitions := util.PartitionSliceStrings(util.FileLinesIncludeEmpty(filename))
	calledNumbers = util.StringSplitToInts(partitions[0][0], ",")
	boards = parseBoards(partitions[1:])
	return calledNumbers, boards
}

func main() {
	calledNumbers, boards := loadBingoData("../input/04_INPUT.txt")
	println(fmt.Sprintf("part 1: winning score (first) %d", computeWinningScorePart1(calledNumbers, boards)))
	println(fmt.Sprintf("part 2: winning score (last)  %d", computeWinningScorePart2(calledNumbers, boards)))
}
