package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var wtr = bufio.NewWriter(os.Stdout)

func main() {
	defer flush()
	n, c := scanInt2()
	t, a := scanIntSlice2(n)
	dp0 := make([][30]int, n+1)
	dp1 := make([][30]int, n+1)
	for i:=0;i<30;i++ {
		dp0[0][i] = 0
		dp1[0][i] = 1
	}
	var op func(int, int) int
	for i:=0;i<n;i++ {
		for j:=0;j<30;j++ {
			digitA := a[i] >> j & 1
			switch t[i] {
			case 1:
				op = func(i, j int) int {return i & j} 
			case 2:
				op = func(i, j int) int {return i | j}
			case 3:
				op = func(i, j int) int {return i ^ j}
			}
			dp0[i+1][j] = op(dp0[i][j], digitA) 
			dp1[i+1][j] = op(dp1[i][j], digitA) 
		}
	}
	x := c
	for i:=0;i<n;i++ {
		x = convertX(x, dp0[i+1], dp1[i+1])
		out(x)
	}
}
func convertX(x int, dp0, dp1 [30]int) int {
	res := 0
	for i:=0;i<30;i++ {
		if x >> i & 1 == 0 {
			res += dp0[i] << i
		} else {
			res += dp1[i] << i
		}
	}
	return res
}
// ==================================================
// init
// ==================================================

const inf = math.MaxInt64
const mod1000000007 = 1000000007
const mod998244353 = 998244353
const mod = mod1000000007

func init() {
	sc.Buffer([]byte{}, math.MaxInt64)
	sc.Split(bufio.ScanWords)
	if len(os.Args) > 1 && os.Args[1] == "i" {
		b, e := ioutil.ReadFile("./input")
		if e != nil {
			panic(e)
		}
		sc = bufio.NewScanner(strings.NewReader(strings.Replace(string(b), " ", "\n", -1)))
	}
}

// ==================================================
// io
// ==================================================

func scanInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func scanInt2() (int, int) {
	return scanInt(), scanInt()
}

func scanInt3() (int, int, int) {
	return scanInt(), scanInt(), scanInt()
}

func scanInt4() (int, int, int, int) {
	return scanInt(), scanInt(), scanInt(), scanInt()
}

func scanIntSlice(n int) []int {
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = scanInt()
	}
	return a
}

func scanIntSlice2(n int) ([]int, []int) {
	a := make([]int, n)
	b := make([]int, n)
	for i := 0; i < n; i++ {
		a[i], b[i] = scanInt2()
	}
	return a, b
}

func scanIntSlice3(n int) ([]int, []int, []int) {
	a := make([]int, n)
	b := make([]int, n)
	c := make([]int, n)
	for i := 0; i < n; i++ {
		a[i], b[i], c[i] = scanInt3()
	}
	return a, b, c
}

func scanIntSlice4(n int) ([]int, []int, []int, []int) {
	a := make([]int, n)
	b := make([]int, n)
	c := make([]int, n)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		a[i], b[i], c[i], d[i] = scanInt4()
	}
	return a, b, c, d
}

func scanFloat() float64 {
	sc.Scan()
	f, e := strconv.ParseFloat(sc.Text(), 64)
	if e != nil {
		panic(e)
	}
	return f
}

func scanString() string {
	sc.Scan()
	return sc.Text()
}

func scani() int {
	var i int
	fmt.Scanf("%i", &i)
	return i
}

func scans() string {
	var s string
	fmt.Scanf("%s", &s)
	return s
}

func out(v ...interface{}) {
	_, e := fmt.Fprintln(wtr, v...)
	if e != nil {
		panic(e)
	}
}

func outwoln(v ...interface{}) {
	_, e := fmt.Fprint(wtr, v...)
	if e != nil {
		panic(e)
	}
}

func outis(sl []int) {
	r := make([]string, len(sl))
	for i, v := range sl {
		r[i] = itoa(v)
	}
	out(strings.Join(r, " "))
}

func flush() {
	e := wtr.Flush()
	if e != nil {
		panic(e)
	}
}


func atoi(s string) int {
	i, e := strconv.Atoi(s)
	if e != nil {
		panic(e)
	}
	return i
}

func itoa(i int) string {
	return strconv.Itoa(i)
}

func btoi(b byte) int {
	return atoi(string(b))
}

// ==================================================
// num
// ==================================================

func min(arr ...int) int {
	if len(arr) == 0 {
		panic("min error: len(arr) = 0")
	}
	res := inf
	for _, v := range arr {
		if res > v {
			res = v
		}
	}
	return res
}

func max(arr ...int) int {
	if len(arr) == 0 {
		panic("max error: len(arr) = 0")
	}
	res := -inf
	for _, v := range arr {
		if res < v {
			res = v
		}
	}
	return res
}


func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

// =====================================================================================
// heap
// =====================================================================================
type IntMinHeap []int

//heapインターフェースの実装 heap化はheap.Init(hq)
func (h IntMinHeap) Len() int {return len(h)}
func (h IntMinHeap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h IntMinHeap) Less(i, j int) bool {return h[i] < h[j]}

func (h *IntMinHeap) Push(e interface{}) {
	*h = append(*h, e.(int))
}
func (h *IntMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}
// =====================================================================================
// stack and queue
// =====================================================================================
type Stack []int
func (s *Stack) Push(v int) {
	*s = append(*s, v)
}
func (s *Stack) Pop() int {
	old := *s
	n := len(old)
	x := old[n-1]
	*s = old[:n-1]
	return x
}
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}
// queue
type Queue []int
func (q *Queue) Push(v int) {
	*q = append(*q, v)
}
func (q *Queue) Pop() int {
	old := *q
	x := old[0]
	*q = old[1:]
	return x
}
func (q *Queue) IsEmpty() bool {
	return len(*q) == 0 
}

// =====================================================================================
// Graph
// =====================================================================================
type edge struct {
	to int
	cost int
}
type Edges []edge
type Graph []Edges
// G := NewGraph(n)  G[a] = append(G[a], edge{to:b, cost:x})
func newGraph(n int) Graph {
	return make([]Edges, n)
}
// Edgesのcostでのsortを可能にするためのsort.interfaceを実装
func (e Edges) Len() int {return len(e)}
func (e Edges) Swap(i, j int) {e[i], e[j] = e[j], e[i]}
func (e Edges) Less(i, j int) bool {return e[i].cost < e[j].cost}
// asc: sort.Sort(graph[i])
// dec: sort.Sort(sort.Reverce(graph[i]))