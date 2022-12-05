package ds

type Stack[T any] struct {
	data []T
}

func NewStack[T any]() *Stack[T] {
	return &Stack[T]{data: []T{}}
}

func (s *Stack[T]) Push(item T) {
	s.data = append(s.data, item)
}

func (s *Stack[T]) Peek() T {
	return s.data[len(s.data)-1]
}

func (s *Stack[T]) Pop() (val T) {
	val = s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1] // Pop
	return
}

func (s *Stack[T]) IsEmpty() bool {
	return len(s.data) == 0
}
