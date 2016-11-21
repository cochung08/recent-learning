// Reading and writing files are basic tasks needed for
// many Go programs. First we'll look at some examples of
// reading files.

package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
	"strings"
)

// Reading files requires checking most calls for errors.
// This helper will streamline our error checks below.
func check(e error) {
	if e != nil {
		panic(e)
	}
}
// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}
func main() {

	// Perhaps the most basic file reading task is
	// slurping a file's entire contents into memory.
	// dat, err := ioutil.ReadFile("./leetcode.txt")
	// check(err)
	// fmt.Print(string(dat))


	lines, err := readLines("./leetcode.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	//var l []string
	//l = strings.Split(string(lines), '\n')
	for i, line := range lines {
		//fmt.Println(i, line)
		fmt.Println(i,strings.Split(line,"       "))
	}


	// Close the file when you're done (usually this would
	// be scheduled immediately after `Open`ing with
	// `defer`).

}
