package ds

// TODO FIXME this likely goes away once generics arrives

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

type RuneSet struct { // would generalize further if had generics
	data map[rune]bool
}

func NewRuneSet() *RuneSet {
	return &RuneSet{data: make(map[rune]bool)}
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
