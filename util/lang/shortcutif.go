package lang

// adapted from https://stackoverflow.com/a/59375088/3633993
func If[T any](condition bool, trueval T, falseval T) T {
	if condition {
		return trueval
	}
	return falseval
}
