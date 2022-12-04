package lang

// adapted from https://stackoverflow.com/a/59375088/3633993
type If bool

func (c If) Int(a, b int) int {
	if c {
		return a
	}
	return b
}

func (c If) String(a, b string) string {
	if c {
		return a
	}
	return b
}

func (c If) Bool(a, b bool) bool {
	if c {
		return a
	}
	return b
}

func (c If) Rune(a, b rune) rune {
	if c {
		return a
	}
	return b
}

func (c If) Interface(a, b interface{}) interface{} {
	if c {
		return a
	}
	return b
}
