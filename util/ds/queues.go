package ds

// Queue data type
type Queue[T any] struct {
	data chan T
}

func NewQueue[T any](capacity int) *Queue[T] {
	return &Queue[T]{data: make(chan T, 1000)}
}

func (queue Queue[T]) Enqueue(val T) {
	queue.data <- val
}

func (queue Queue[T]) Dequeue() T {
	return <-queue.data
}

func (queue Queue[T]) Length() int {
	return len(queue.data)
}

func (queue Queue[T]) IsEmpty() bool {
	return queue.Length() == 0
}
