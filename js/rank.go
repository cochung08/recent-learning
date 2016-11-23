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
	"strconv"
	"encoding/json"
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

	result := make([]([]string), 400)
	var company string
	for i, line := range lines {
		_ = i

		s := strings.Split(line, "        ")
		if len(s) == 1 && s[0] != "" {
			//fmt.Println(s)
			company = s[0]
		}

		if len(s) == 5 {
			s = append(s[:4])
			//fmt.Println(s)
			num, err := strconv.Atoi(s[0])
			if err != nil {
				fmt.Println(err)
				os.Exit(2)
			}
			if len(result[num]) == 0 {
				result[num] = make([]string, 5)
				result[num][0] = s[1]
				result[num][1] = strconv.Itoa(1)
				result[num][2] = s[3]
				result[num][3] = s[2]
				result[num][4] = company
				//fmt.Println(result[num])

			} else {
				//fmt.Println(reflect.TypeOf(result[num][1]))
				count, err := strconv.Atoi(result[num][1])
				if err != nil {
					// handle error
				}
				result[num][1] = strconv.Itoa(count + 1)
				result[num][4] += ", " + company
				//fmt.Println(result[num])
				//fmt.Println(len(result[num]))
			}
		}
	}

	//for i, v := range result {
	//	fmt.Println(i, v)
	//}
	//for i := 1; i < len(result); i += 1 {
	//	fmt.Println(i,result[i])
	//}

	//var mapD  map[int] []string
	mapD := make(map[string][]string)
	for i, v := range result {
		if len(v) != 0 {
			mapD[strconv.Itoa(i)] = v
			//fmt.Println(i, v)

		}
	}
	smapB, _ := json.Marshal(mapD)
	fmt.Println(string(smapB))

	//for key, value := range mapD {
	//	fmt.Println("Key:", key, "Value:", value)
	//}




	// Close the file when you're done (usually this would
	// be scheduled immediately after `Open`ing with
	// `defer`).

}
