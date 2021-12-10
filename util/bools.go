package util

func AllTrue(boolValues ...bool) bool {
	if len(boolValues) == 0 {
		return false
	}
	allTrue := true
	for _, val := range boolValues {
		allTrue = allTrue && val
	}
	return allTrue
}
