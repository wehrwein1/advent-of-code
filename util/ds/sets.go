package ds

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
