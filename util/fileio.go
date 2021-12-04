package util

import (
	"os"
	"strings"
)

func FileLinesSkipEmpty(filename string) []string {
	return fileLines(filename, false)
}

func FileLinesIncludeEmpty(filename string) []string {
	return fileLines(filename, true)
}

func fileLines(filename string, isIncludeEmptyLines bool) (ret []string) {
	bytes, err := os.ReadFile(filename)
	Check(err)
	lines := strings.Split(string(bytes), "\n")
	for _, line := range lines {
		line = chomp(line)
		if isIncludeEmptyLines || len(line) > 0 {
			ret = append(ret, line)
		}
	}
	return
}

func FileContent(filename string) string {
	bytes, err := os.ReadFile(filename)
	Check(err)
	return chomp(string(bytes))
}

func chomp(text string) string {
	return strings.TrimRight(text, "\r\n") // handle windows line endings too https://stackoverflow.com/a/44449581
}
