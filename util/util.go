package util

// Deprecated: not best practice, handle at source
func Check(e error) {
	if e != nil {
		panic(e)
	}
}
