package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"path"
	"regexp"
	"runtime"
	"strconv"
	"strings"
	"text/template"
	"time"

	"github.com/wehrwein1/advent-of-code/util"
	"github.com/wehrwein1/advent-of-code/util/lang"
)

var str = strconv.Itoa
var mkdir = util.Mkdir

func year() int { return time.Now().Year() }
func day() int  { return time.Now().Day() }

func Bootstrap() {
	rootdir, bootstrapdir, templatedir := dirs()
	year := year()
	day := day()
	daydir := path.Join(rootdir, str(year), fmt.Sprintf("day%02d", day))
	inputdir := path.Join(rootdir, str(year), "input")
	inputTextFile := path.Join(inputdir, fmt.Sprintf("%02d_INPUT.txt", day))
	dayHtmlFile := path.Join(inputdir, "html", fmt.Sprintf("%02d.html", day))
	dayUrl := fmt.Sprintf("https://adventofcode.com/%d/day/%d", year, day)
	inputUrl := fmt.Sprintf("%s/input", dayUrl)
	session := readFileContent(path.Join(bootstrapdir, ".session.txt"))
	emailAddress := readFileContent(path.Join(bootstrapdir, ".emailAddressForUserAgentHeader.txt"))
	println()
	println(fmt.Sprintf("bootstrap config/sess.  %s", session))
	println(fmt.Sprintf("bootstrap config/email  %s", emailAddress))
	println(fmt.Sprintf("bootstrap rootdir       %s", rootdir))
	println(fmt.Sprintf("bootstrap bootstrapdir  %s", bootstrapdir))
	println(fmt.Sprintf("bootstrap templatedir   %s", templatedir))
	println(fmt.Sprintf("bootstrap daydir        %s", daydir))
	println(fmt.Sprintf("bootstrap inputfile     %s", inputTextFile))
	println(fmt.Sprintf("bootstrap htmlfile      %s", dayHtmlFile))
	println(fmt.Sprintf("bootstrap inputurl      %s", inputUrl))
	println()
	downloadFileWithSessionCookie(inputUrl, inputTextFile, session, emailAddress) // download input file
	downloadFileWithSessionCookie(dayUrl, dayHtmlFile, session, emailAddress)     // download day HTML file
	extractTestcaseExamples(dayHtmlFile, path.Join(inputdir, fmt.Sprintf("%02d_TEST.txt", day)))
	mkdir(daydir)
	defaultCodingLanguage := readFileContent(path.Join(bootstrapdir, ".settings.txt")) // implied: default coding language (file extension), e.g. "py"
	excludedLanguage := lang.If(defaultCodingLanguage == "py", "go", "py")
	templates := map[string]string{
		// go
		"day.go.tmpl":      fmt.Sprintf("%02d.go", day),
		"day_test.go.tmpl": fmt.Sprintf("%02d_test.go", day),
		// python
		"day.py.tmpl":      fmt.Sprintf("day%02d_%d.py", day, year),
		"day_test.py.tmpl": fmt.Sprintf("day%02d_%d_test.py", day, year),
	}
	// disable templates per config
	for key := range templates {
		if strings.Contains(key, excludedLanguage) {
			delete(templates, key)
		}
	}

	data := TemplateData{Year: str(year), Day1: str(day), Day2: fmt.Sprintf("%02d", day)}
	for template, destfile := range templates {
		applyTemplate(path.Join(templatedir, template), path.Join(daydir, destfile), data)
	}
}

func readFileContent(filename string) (filecontent string) {
	bytes, err := os.ReadFile(filename)
	if err != nil {
		fileout, _ := os.OpenFile(filename, os.O_RDONLY|os.O_CREATE, 0666) // create empty file, per https://stackoverflow.com/a/35558965
		fileout.Close()
	}
	return util.Chomp(string(bytes))
}

func extractTestcaseExamples(dayHtmlFile, destFile string) {
	html := util.FileContent(dayHtmlFile)
	testcase, warning := findTestcase(html)
	if warning != nil {
		println(fmt.Sprintf("warn: %s", warning))
	}
	if err := os.WriteFile(destFile, []byte(testcase), util.FileModeUserReadWrite); err != nil {
		log.Fatalf("error writing file: %s", err.Error())
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
func downloadFileWithSessionCookie(url string, destfilepath string, session string, emailAddress string) {
	if _, err := os.Stat(destfilepath); err == nil { // file exists
		println(fmt.Sprintf("warn: skip download file (already exists): %s", destfilepath))
		return
	}
	mkdir(path.Dir(destfilepath))
	userAgentHeaderValue := fmt.Sprintf("https://github.com/wehrwein1/advent-of-code/blob/main/util/bootstrap/adventofcode.go by %s", emailAddress) // https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent
	cmd := exec.Command("curl", "-o", destfilepath, url,
		"--cookie", fmt.Sprintf("session=%s", session),
		"-A", userAgentHeaderValue,
	)
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
	println(fmt.Sprintf("bootstrap created %s", destFile))
}

type TemplateData struct {
	Year string
	Day2 string // padded to 2 digits
	Day1 string // not padded
}

func findTestcase(html string) (string, error) {
	regex := regexp.MustCompile("<pre><code>(?P<code>(.*|\n|\r)+)+</code></pre>")
	match := regex.FindStringSubmatch(html)
	paramsMap := make(map[string]string)
	for i, name := range regex.SubexpNames() {
		if i > 0 && i <= len(match) {
			if strings.Contains(match[i], "</code></pre>") {
				// println(fmt.Sprintf("match[%d] \"%s\" '%s'", i, name, match[1]))
				paramsMap[name] = strings.Split(match[i], "</code></pre>")[0]
			}
		}
	}
	testcase := paramsMap["code"]
	var err error
	if len(testcase) == 0 {
		err = fmt.Errorf("failed extracting testcase code from html, skipping.. ")
	}
	return testcase, err
}
