package main

import (
	"fmt"
	"strings"
)

func main() {
	var (
		n int
		t string
	)
	rule := make(map[int][2]int)
	rule[0] = [2]int{1, 0}  //東
	rule[1] = [2]int{0, -1} // 南
	rule[2] = [2]int{-1, 0} //  西
	rule[3] = [2]int{0, 1}  // 北

	fmt.Scan(&n)
	fmt.Scan(&t)
	t_slice := strings.Split(t, "")
	now := 0
	ans_x := 0
	ans_y := 0
	for _, c := range t_slice {
		if c == "R" {
			now++
			continue
		}
		ans_x += rule[now%4][0]
		ans_y += rule[now%4][1]
		//fmt.Printf("%v, %v, %v\n", now, ans_x, ans_y)
	}

	fmt.Printf("%v %v\n", ans_x, ans_y)

}
