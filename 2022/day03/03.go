// https://adventofcode.com/2022/day/3
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

var sum = util.SumInts

var fileLines = util.FileLinesSkipEmpty

type Set = ds.Set

func main() {
	println(fmt.Sprintf("part 1: %d", computeDay(fileLines("../input/03_INPUT.txt"), Part1)))
	println(fmt.Sprintf("part 2: %d", computeDay(fileLines("../input/03_INPUT.txt"), Part2)))
}

func computeDay(lines []string, part ProblemPart) (res int) {
	priorities := []int{}
	if part == Part1 {
		for _, rucksackItems := range lines {
			compartmentSize := len(rucksackItems) / 2
			compartment1 := rucksackItems[:compartmentSize]
			compartment2 := rucksackItems[compartmentSize:]
			commonItem := getCommonItem(compartment1, compartment2)
			priority := priority(commonItem)
			println(fmt.Sprintf("%s -> %s, %s --> %s(%d) -> %d", rucksackItems, compartment1, compartment2, string(commonItem), commonItem, priority))
			priorities = append(priorities, priority)
		}
	} else {
		// Part 2
		for i := 0; i < len(lines); i += 3 {
			threeLines := lines[i : i+3]
			for _, line := range threeLines {
				println("line", line)
			}
			commonItem := getCommonItem(threeLines...)
			priority := priority(commonItem)
			println(fmt.Sprintf("lines[%d-%d] --> %s(%d) -> %d", i, i+2, string(commonItem), commonItem, priority))
			println()
			priorities = append(priorities, priority)
		}
	}
	return sum(priorities...)
}

func getCommonItem(items ...string) rune {
	var commonItems string
	for i := 0; i < len(items); {
		first := items[i]
		set1 := *makeSet([]rune(first))
		var set2 Set
		if i == 0 { // initial state empty
			second := items[i+1]
			set2 = *makeSet([]rune(second))
			i += 2
		} else {
			second := commonItems
			set2 = *makeSet([]rune(second))
			i += 1
		}
		// merge common items
		commonItems = string(getRuneArray(set1.Intersection(set2).Keys()))
	}
	return rune(commonItems[0])
}

func getRuneArray(array []any) (res []rune) {
	for _, item := range array {
		res = append(res, item.(rune))
	}
	return
}

func priority(commonItem rune) int {
	ord := int(commonItem)
	is_lowercase := int('a') <= ord && ord <= int('z')
	// is_uppercase := int('A') <= ord && ord <= int('Z')
	const min_lowercase_priority = 1
	if is_lowercase {
		return min_lowercase_priority + ord - int('a')
	}
	const min_uppercase_priority = 27
	return min_uppercase_priority + ord - int('A')
}

func makeSet(compartment []rune) *Set {
	s := ds.NewSet()
	for _, item := range compartment {
		s.Put(item)
	}
	return s
}
