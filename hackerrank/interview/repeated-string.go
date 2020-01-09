package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "math"
    "strings"
)

// Complete the repeatedString function below.
func repeatedString(s string, n int64) int64 {
    l := float64(len(s))
    baseA := int64(0)
    for _, letter := range s {
        if letter == 'a' {
            baseA++
        }
    }
    incompleteRepeat := math.Floor(float64(n)/l)
    incompleteLength := incompleteRepeat * l


    reminder := n - int64(incompleteLength)

    reminderA := int64(0)
    for index := int64(0); index < reminder; index++ {
        if s[index] == 'a' {
            reminderA++
        }
    }

    return (baseA * int64(incompleteRepeat)) + reminderA
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 1024 * 1024)

    s := readLine(reader)

    n, err := strconv.ParseInt(readLine(reader), 10, 64)
    checkError(err)

    result := repeatedString(s, n)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}


