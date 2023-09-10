package main

import (
    "fmt"
    "math"
)

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scan(&n)

    fmt.Println("Prime numbers up to", n, "are:")
    for i := 2; i <= n; i++ {
        if isPrime(i) {
            fmt.Printf("%d ", i)
        }
    }
}
