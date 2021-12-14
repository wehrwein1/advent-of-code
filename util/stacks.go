package util

// TODO FIXME this likely goes away once generics arrives

type RuneStack struct {
	data []rune
}

func NewRuneStack() *RuneStack {
	return &RuneStack{data: []rune{}}
}

func (s *RuneStack) Push(item rune) {
	s.data = append(s.data, item)
}

func (s *RuneStack) Peek() rune {
	return s.data[len(s.data)-1]
}

func (s *RuneStack) Pop() (val rune) {
	val = s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1] // Pop
	return
}

func (s *RuneStack) IsEmpty() bool {
	return len(s.data) == 0
}
