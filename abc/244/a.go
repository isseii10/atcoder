package main

import (
	"fmt"
)

func main() {
	var (
		n int
		s string
	)
	fmt.Scan(&n)
	fmt.Scan(&s)
	for i, c := range s {
		if i != n-1 {
			continue
		}
		fmt.Printf("%c\n", c)
	}
}
