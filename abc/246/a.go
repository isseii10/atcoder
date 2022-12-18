package main

import (
	"fmt"
)

func main() {
	var (
		xs, ys [3]int
	)
	x_count := make(map[int]int)
	y_count := make(map[int]int)

	for i := 0; i < 3; i++ {
		fmt.Scan(&xs[i], &ys[i])
		x_count[xs[i]]++
		y_count[ys[i]]++
	}
	var ans [2]int
	for k, v := range x_count {
		if v == 1 {
			ans[0] = k
		}
	}
	for k, v := range y_count {
		if v == 1 {
			ans[1] = k
		}
	}
	fmt.Println(ans[0], ans[1])
}
