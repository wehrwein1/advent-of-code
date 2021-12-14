package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/wehrwein1/advent-of-code/util"
)

func TestDayPart1(t *testing.T) {
	assertLineValid(t, "()")
	assertLineValid(t, "[]")
	assertLineValid(t, "([])")
	assertLineValid(t, "{()()()}")
	assertLineValid(t, "<([{}])>")
	assertLineValid(t, "[<>({}){}[([])<>]]")
	assertLineValid(t, "(((((((((())))))))))")
	assertLineCorrupt(t, "(]", 1, ')')
	assertLineCorrupt(t, "{()()()>", 7, '}')
	assertLineCorrupt(t, "(((()))}", 7, ')')
	assertLineCorrupt(t, "<([]){()}[{}])", 13, '>')
	assertLineCorrupt(t, "{([(<{}[<>[]}>{[]{[(<()>", 12, ']')
	assertLineCorrupt(t, "[[<[([]))<([[{}[[()]]]", 8, ']')
	assertLineCorrupt(t, "[{[{({}]{}}([{[{{{}}([]", 7, ')')
	assertLineCorrupt(t, "[<(<(<(<{}))><([]([]()", 10, '>')
	assertLineCorrupt(t, "<{([([[(<>()){}]>(<<{{", 16, ']')
	assert.Equal(t, 3, sumSyntaxErrorScore("[[<[([]))<([[{}[[()]]]"))
	assert.Equal(t, 57, sumSyntaxErrorScore("[{[{({}]{}}([{[{{{}}([]"))
	assert.Equal(t, 1197, sumSyntaxErrorScore("{([(<{}[<>[]}>{[]{[(<()>"))
	assert.Equal(t, 25137, sumSyntaxErrorScore("<{([([[(<>()){}]>(<<{{"))
	assert.Equal(t, 26397, sumSyntaxErrorScore(fileLines("../input/10_TEST.txt")...))
}

func TestDayPart2(t *testing.T) {
	assert.Equal(t, 288957, completionStringScore("}}]])})]"))
	assert.Equal(t, 5566, completionStringScore(")}>]})"))
	assert.Equal(t, 1480781, completionStringScore("}}>}>))))"))
	assert.Equal(t, 995444, completionStringScore("]]}}]}]}>"))
	assert.Equal(t, 294, completionStringScore("])}>"))
	assert.Equal(t, 288957, middleCompletionStringScore(fileLines("../input/10_TEST.txt")...))
}

func assertLineValid(t *testing.T, line string) {
	lineResult, invalidIndex, expectedChar := evaluateLine(line, util.NewRuneStack())
	assert.Equal(t, Valid, lineResult, "line result different")
	assert.Equal(t, -1, invalidIndex, "index different")
	assert.Equal(t, int32(-1), expectedChar, "char different")
}

func assertLineCorrupt(t *testing.T, line string, expectedInvalidIndex int, expectedChar rune) {
	lineResult, actualInvalidIndex, actualChar := evaluateLine(line, util.NewRuneStack())
	assert.Equal(t, Corrupt, lineResult, "line result different")
	assert.Equal(t, expectedInvalidIndex, actualInvalidIndex, "index different")
	assert.Equal(t, expectedChar, actualChar, "char different")
}
