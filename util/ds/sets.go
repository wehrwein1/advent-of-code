package ds

import "github.com/wehrwein1/advent-of-code/util"

// Set
type Set struct {
	data map[any]bool
}

var itemExists = true

func NewSet(items ...any) *Set {
	s := &Set{data: make(map[any]bool)}
	s.PutAll(items...)
	return s
}

func (s Set) Has(val any) bool {
	_, ok := s.data[val]
	return ok
}

func (s Set) Put(val any) {
	s.data[val] = itemExists
}

func (s Set) PutAll(vals ...any) {
	for _, val := range vals {
		s.data[val] = itemExists
	}
}

func (s Set) Keys() []any {
	keys := make([]any, len(s.data)) // https://stackoverflow.com/a/27848197/3633993
	i := 0
	for k := range s.data {
		keys[i] = k
		i++
	}
	return keys
}

func (s Set) Remove(val rune) {
	delete(s.data, val)
}

func (s Set) Len() int {
	return len(s.data)
}

func (s Set) IsEmpty() bool {
	return s.Len() == 0
}

func (s1 Set) Union(s2 Set) *Set { // TODO FIXME clarity memory behavior, return value as convenience
	smaller := util.If(s1.Len() <= s2.Len()).Interface(s1, s2).(Set)
	larger := util.If(s1.Len() > s2.Len()).Interface(s1, s2).(Set)
	union := NewSet()
	for _, k := range smaller.Keys() {
		if larger.Has(k) {
			union.Put(k)
		}
	}
	return union
}
