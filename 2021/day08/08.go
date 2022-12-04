// https://adventofcode.com/2021/day/8
package main

import (
	"fmt"
	"sort"
	"strings"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/ds"
)

var fileLines = util.FileLinesSkipEmpty
var part1CountedDigits = []digit{One, Four, Seven, Eight}
var prettyPrint = func(runes []rune, printBrackets bool) string {
	return PrettyPrintRuneSlice(runes, "", printBrackets)
}

func main() {
	lines := fileLines("../input/08_INPUT.txt")
	println(fmt.Sprintf("part 1: count of (1,4,7,8): %d", countSelectedDigits(lines, part1CountedDigits...)))
	println(fmt.Sprintf("part 2: sum output values: %d", sumOutputValues(lines)))
}

func countSelectedDigits(lines []string, countedDigits ...digit) (count int) {
	for _, line := range lines {
		tokens := strings.Split(line, " | ")
		outputSignals := tokens[1]
		outputSignalTokens := strings.Split(outputSignals, " ")
		for _, outputSignalToken := range outputSignalTokens {
			outputSignalLen := len(outputSignalToken)
			for _, countedDigit := range countedDigits {
				if countedDigit.segmentCount() == outputSignalLen {
					count += 1
				}
			}
		}
	}
	return
}

func decodeSignal(line string) (signalPatterns map[string]int, outputValue int) {
	tokens := strings.Split(line, " | ")
	segmentEncodings := strings.Split(tokens[0], " ")
	// outputSignals := tokens[1]
	// state
	signalIndexCandidates := map[int]RuneSet{} // e.g. 0 => ('a','c','d')
	for i := 0; i < Eight.segmentCount(); i++ {
		signalIndexCandidates[i] = *NewRuneSet()
	}
	println(fmt.Sprintf("line '%s'", line))
	// process exact match encodings
	for _, segmentEncoding := range segmentEncodings {
		digit, found := digitForUniqueSegmentCount(len(segmentEncoding))
		if found {
			candidates := []rune(segmentEncoding)
			for _, digitSegment := range digit.segments() {
				if signalIndexCandidates[digitSegment].IsEmpty() {
					signalIndexCandidates[digitSegment].PutAll(candidates...)
				} else {
					signalIndexCandidates[digitSegment] = *runeSetUnion(signalIndexCandidates[digitSegment], *NewRuneSet(candidates...))
				}
				println(fmt.Sprintf("After digit %v segmentIndex %d in %v", digit, digitSegment, signalIndexCandidates[digitSegment]))
			}
		}
	}
	printProgress(signalIndexCandidates)
	// TODO FIXME search for equal length candidate sets

	outputValues := []int{1} // TODO FIXME
	signalPatterns = map[string]int{}
	for segmentIndex := range signalIndexCandidates {
		activeSignal := prettyPrint(signalIndexCandidates[segmentIndex].Keys(), false)
		signalPatterns[activeSignal] = segmentIndex
	}
	return signalPatterns, util.IntSliceToDigitsValue(outputValues)
}

func printProgress(signalIndexCandidates map[int]RuneSet) {
	maxNumberOfSegments := Eight.segmentCount()
	for i := 0; i < maxNumberOfSegments; i++ {
		candidates := signalIndexCandidates[i].Keys()
		println(fmt.Sprintf("segmentIndex %d in %s", i, prettyPrint(RuneSlice(candidates).Sorted(), true)))
	}
}

func sumOutputValues(lines []string) (sumOutputValues int) {
	for _, line := range lines {
		_, outputValue := decodeSignal(line)
		sumOutputValues += outputValue
	}
	return
}

type digit int

const (
	Zero digit = iota
	One
	Two
	Three
	Four
	Five
	Six
	Seven
	Eight
	Nine
)

// Segments
//   0
// 1   2
//   3
// 4   5
//   6

var digitSegmentVectors = map[digit][]int{
	Zero:  {0, 1, 2, 4, 5, 6},
	One:   {2, 5}, // unique count
	Two:   {0, 2, 3, 4, 6},
	Three: {0, 2, 3, 5, 6},
	Four:  {1, 2, 3, 5}, // unique count
	Five:  {0, 1, 3, 5, 6},
	Six:   {0, 1, 3, 4, 5, 6},
	Seven: {0, 2, 5},             // unique count
	Eight: {0, 1, 2, 3, 4, 5, 6}, // unique count
	Nine:  {0, 1, 2, 3, 5, 6},
}

func (d digit) segmentCount() int {
	return len(d.segments())
}

func (d digit) segments() []int {
	return digitSegmentVectors[d]
}

func digitForUniqueSegmentCount(segmentCount int) (digit digit, ok bool) {
	for _, digit := range part1CountedDigits {
		if digit.segmentCount() == segmentCount {
			return digit, true
		}
	}
	return
}

func runeSetUnion(s1, s2 RuneSet) *RuneSet { // TODO FIXME clarity memory behavior, return value as convenience
	smaller := util.If(s1.Len() <= s2.Len()).Interface(s1, s2).(RuneSet)
	larger := util.If(s1.Len() > s2.Len()).Interface(s1, s2).(RuneSet)
	union := NewRuneSet()
	for _, k := range smaller.Keys() {
		if larger.Has(k) {
			union.Put(k)
		}
	}
	return union
}

type RuneSet struct {
	ds.Set
}

func NewRuneSet(items ...rune) *RuneSet {
	s := &RuneSet{}
	s.Set = *ds.NewSet()
	s.PutAll(items...)
	return s
}

func (s RuneSet) Keys() []rune {
	keys := make([]rune, s.Len()) // https://stackoverflow.com/a/27848197/3633993
	i := 0
	for _, k := range s.Set.Keys() {
		keys[i] = k.(rune)
		i++
	}
	return keys
}

func (s RuneSet) PutAll(items ...rune) {
	for _, item := range items {
		s.Set.Put(item)
	}
}

func (s RuneSet) String() string {
	chars := []string{}
	for _, k := range s.Keys() {
		chars = append(chars, fmt.Sprintf("%c", k))
	}
	return fmt.Sprintf("[%s]", strings.Join(chars, " "))
}

func PrettyPrintRuneSlice(runes []rune, delim string, printBrackets bool) string {
	chars := []string{}
	for _, r := range runes {
		chars = append(chars, fmt.Sprintf("%c", r))
	}
	formatString := util.If(printBrackets).String("[%s]", "%s")
	return fmt.Sprintf(formatString, strings.Join(chars, delim))
}

type RuneSlice []rune

func (sl RuneSlice) Sorted() (sortedRunes []rune) {
	intValues := []int{}
	for _, k := range sl {
		intValues = append(intValues, int(k))
	}
	sort.Ints(intValues)
	sortedRunes = make([]rune, len(intValues))
	for i := 0; i < len(intValues); i++ {
		sortedRunes[i] = rune(intValues[i])
	}
	return
}
