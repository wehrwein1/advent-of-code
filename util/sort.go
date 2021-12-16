package util

import "sort"

type RuneSlice []rune

func (sl RuneSlice) Sorted() (sortedRunes []rune) {
	intValues := []int{}
	for _, k := range sl {
		intValues = append(intValues, int(k))
	}
	sort.Ints(intValues)
	sortedRunes = make([]rune, len(intValues))
	for i := 0; i < len(intValues); i++ {
		sortedRunes[i] = rune(intValues[i])
	}
	return
}
