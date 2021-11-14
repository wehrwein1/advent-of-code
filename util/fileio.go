package util

import (
	"os"
	"strings"
)

func FileLines(filename string) (ret []string) { // whoa! crazy implicit return value syntax https://stackoverflow.com/a/37563128/3633993
	bytes, err := os.ReadFile(filename)
	Check(err)
	lines := strings.Split(string(bytes), "\n")
	for _, line := range lines {
		if len(line) > 0 { // ignore empty lines
			ret = append(ret, line)
		}
	}
	return
}

func FileContent(filename string) string {
	bytes, err := os.ReadFile(filename)
	Check(err)
	return string(bytes)
}
