package ds

import (
	"fmt"
	"strings"
)

// TODO FIXME this likely goes away once generics arrives

// **************
// IntSet
// **************

type IntSet struct { // would generalize further if had generics
	data map[int]bool
}

func NewIntSet() *IntSet {
	return &IntSet{data: make(map[int]bool)}
}

func (s IntSet) Put(val int) {
	s.data[val] = true
}

func (s IntSet) Has(val int) bool {
	_, ok := s.data[val]
	return ok
}

func (s IntSet) Keys() []int {
	keys := make([]int, len(s.data)) // https://stackoverflow.com/a/27848197/3633993
	i := 0
	for k := range s.data {
		keys[i] = k
		i++
	}
	return keys
}

// **************
// RuneSet
// **************

type RuneSet struct { // would generalize further if had generics
	data map[rune]bool
}

func NewRuneSet(initialVals ...rune) *RuneSet {
	s := RuneSet{data: make(map[rune]bool)}
	s.Put(initialVals...)
	return &s
}

func (s RuneSet) Put(vals ...rune) {
	for _, val := range vals {
		s.data[val] = true
	}
}

func (s RuneSet) Has(val rune) bool {
	_, ok := s.data[val]
	return ok
}

func (s RuneSet) Remove(val rune) {
	delete(s.data, val)
}

func (s RuneSet) Keys() []rune {
	keys := make([]rune, len(s.data)) // https://stackoverflow.com/a/27848197/3633993
	i := 0
	for k := range s.data {
		keys[i] = k
		i++
	}
	return keys
}

func (s RuneSet) Len() int {
	return len(s.data)
}

func (s RuneSet) IsEmpty() bool {
	return s.Len() == 0
}

func (s RuneSet) String() string {
	chars := []string{}
	for k := range s.data {
		chars = append(chars, fmt.Sprintf("%c", k))
	}
	return fmt.Sprintf("[%s]", strings.Join(chars, " "))
}
