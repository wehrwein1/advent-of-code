package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"path"
	"runtime"
	"strconv"
	"text/template"
	"time"

	"github.com/wehrwein1/advent-of-code/util"
)

var str = strconv.Itoa
var mkdir = util.Mkdir

func year() int { return time.Now().Year() }
func day() int  { return time.Now().Day() }

func Bootstrap() {
	rootdir, bootstrapdir, templatedir := dirs()
	year := year()
	day := day()
	daydir := path.Join(rootdir, str(year), fmt.Sprintf("day%d", day))
	inputUrl := fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", year, day)
	inputDestFile := path.Join(rootdir, str(year), "input", fmt.Sprintf("%d_INPUT.txt", day))
	session := util.FileContent(path.Join(bootstrapdir, ".session.txt"))
	println()
	println(fmt.Sprintf("bootstrap rootdir       %s", rootdir))
	println(fmt.Sprintf("bootstrap bootstrapdir  %s", bootstrapdir))
	println(fmt.Sprintf("bootstrap templatedir   %s", templatedir))
	println(fmt.Sprintf("bootstrap daydir        %s", daydir))
	println(fmt.Sprintf("bootstrap input         %s", inputUrl))
	println(fmt.Sprintf("bootstrap inputfile     %s", inputDestFile))
	println()
	downloadFileWithSessionCookie(inputUrl, inputDestFile, session) // download input file
	mkdir(daydir)
	templates := map[string]string{
		"day.tmpl":      fmt.Sprintf("day%d.go", day),
		"day_test.tmpl": fmt.Sprintf("day%d_test.go", day),
	}
	data := TemplateData{Year: year, Day: day}
	for template, destfile := range templates {
		applyTemplate(path.Join(templatedir, template), path.Join(daydir, destfile), data)
	}
}

func main() {
	Bootstrap()
}

func dirs() (rootdir, bootstrapdir, templatedir string) {
	_, mainFile, _, ok := runtime.Caller(0)
	if !ok {
		log.Fatalf("error bootstrap failed")
	}
	bootstrapdir = path.Dir(mainFile)
	rootdir = path.Join(bootstrapdir, "../..")
	templatedir = path.Join(bootstrapdir, "templates")
	return
}

// https://www.reddit.com/r/adventofcode/comments/a2vonl/how_to_download_inputs_with_a_script/
func downloadFileWithSessionCookie(url string, filepath string, session string) {
	if _, err := os.Stat(filepath); err == nil { // file exists
		println(fmt.Sprintf("warn: skip download file (already exists): %s", filepath))
		return
	}
	cmd := exec.Command("curl", "-o", filepath, url, "--cookie", fmt.Sprintf("session=%s", session))
	if err := cmd.Run(); err != nil {
		log.Fatalf("error download failed: %s", err.Error())
	}
}

func applyTemplate(templateFile string, destFile string, data interface{}) {
	t, err := template.New(path.Base(templateFile)).ParseFiles(templateFile)
	if err != nil {
		log.Fatalf("error loading template: %s", err.Error())
	}
	fileout, err := os.Create(destFile)
	if err != nil {
		log.Fatalf("error creating dest file: %s", err.Error())
	}
	defer fileout.Close()
	if err := t.Execute(fileout, data); err != nil {
		log.Fatalf("error running template: %s", err.Error())
	}
}

type TemplateData struct {
	Year int
	Day  int
}
