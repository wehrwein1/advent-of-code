package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDayPart1(t *testing.T) {
	assert.Equal(t, 7, computeDay([]string{"mjqjpqmgbljsphdztnvjfqwrcgsmlb"}, Part1))
	assert.Equal(t, 5, computeDay([]string{"bvwbjplbgvbhsrlpgdmjqwftvncz"}, Part1))
	assert.Equal(t, 6, computeDay([]string{"nppdvjthqldpwncqszvftbrmjlhg"}, Part1))
	assert.Equal(t, 10, computeDay([]string{"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}, Part1))
	assert.Equal(t, 11, computeDay([]string{"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}, Part1))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, 19, computeDay([]string{"mjqjpqmgbljsphdztnvjfqwrcgsmlb"}, Part2))
	assert.Equal(t, 23, computeDay([]string{"bvwbjplbgvbhsrlpgdmjqwftvncz"}, Part2))
	assert.Equal(t, 23, computeDay([]string{"nppdvjthqldpwncqszvftbrmjlhg"}, Part2))
	assert.Equal(t, 29, computeDay([]string{"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}, Part2))
	assert.Equal(t, 26, computeDay([]string{"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}, Part2))
}
