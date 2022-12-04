package ds

import "github.com/wehrwein1/advent-of-code/util"

// Set
type Set[T comparable] struct {
	data map[T]bool
}

var itemExists = true

func NewSet[T comparable](items ...T) *Set[T] {
	s := &Set[T]{data: make(map[T]bool)}
	s.PutAll(items...)
	return s
}

func (s Set[T]) Has(val T) bool {
	_, ok := s.data[val]
	return ok
}

func (s Set[T]) Put(val T) {
	s.data[val] = itemExists
}

func (s Set[T]) PutAll(vals ...T) {
	for _, val := range vals {
		s.data[val] = itemExists
	}
}

func (s Set[T]) Keys() []T {
	keys := make([]T, len(s.data)) // https://stackoverflow.com/a/27848197/3633993
	i := 0
	for k := range s.data {
		keys[i] = k
		i++
	}
	return keys
}

func (s Set[T]) Remove(val T) {
	delete(s.data, val)
}

func (s Set[T]) Len() int {
	return len(s.data)
}

func (s Set[T]) IsEmpty() bool {
	return s.Len() == 0
}

func (s1 Set[T]) Intersection(s2 Set[T]) *Set[T] { // TODO FIXME clarity memory behavior, return value as convenience
	smaller := util.If(s1.Len() <= s2.Len()).Interface(s1, s2).(Set[T])
	larger := util.If(s1.Len() > s2.Len()).Interface(s1, s2).(Set[T])
	union := NewSet[T]()
	for _, k := range smaller.Keys() {
		if larger.Has(k) {
			union.Put(k)
		}
	}
	return union
}
