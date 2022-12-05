package util

import "strconv"

func BinaryStringToDecimal(binaryString string, intBits int) int64 {
	decimalValue, err := strconv.ParseInt(binaryString, 2, intBits) // bits: e.g. 64 of 32 bit (int)
	if err != nil {
		panic(err)
	}
	return decimalValue
}
