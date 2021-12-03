package util

// adapted from https://stackoverflow.com/a/59375088/3633993
type If bool

func (c If) Int(a, b int) int {
	if c {
		return a
	}
	return b
}
