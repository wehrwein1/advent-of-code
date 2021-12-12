package util

import (
	"io/fs"
	"log"
	"os"
	"strings"
)

var FileModeUserReadWrite = fs.FileMode(0644) // 0644 = user read and write, https://stackoverflow.com/a/18415935/3633993

func FileLinesSkipEmpty(filename string) []string {
	return fileLines(filename, false)
}

func FileLinesIncludeEmpty(filename string) []string {
	return fileLines(filename, true)
}

func fileLines(filename string, isIncludeEmptyLines bool) (ret []string) {
	bytes, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalf("error reading file: %s", err.Error())
	}
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
	if err != nil {
		log.Fatalf("error reading file: %s", err.Error())
	}
	return chomp(string(bytes))
}

func chomp(text string) string {
	return strings.TrimRight(text, "\r\n") // handle windows line endings too https://stackoverflow.com/a/44449581
}

func Mkdir(path string) {
	if err := os.MkdirAll(path, os.ModePerm); err != nil {
		log.Fatalf("failed creating dir %s", err.Error())
	}
}
