// https://adventofcode.com/2015/day/1
package main

import (
	"log"
	"os"
	"strings"
)

func main() {
	bytes, err := os.ReadFile("../input/01_INPUT.txt")
	check(err)
	UP, DOWN := "(", ")"
	steps := string(bytes)
	log.Println("part 1: Santa ends on floor:", strings.Count(steps, UP)-strings.Count(steps, DOWN))
	floor := 0
	i := 0
	for floor >= 0 {
		delta := 0
		if string(steps[i]) == UP {
			delta = 1
		} else {
			delta = -1
		}
		floor += delta
		i += 1
	}
	log.Println("part 2: Santa first goes to basement on step:", i)
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
