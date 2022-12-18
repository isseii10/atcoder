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

type Poteto struct {
	num int
	to int
}

func main() {
	defer flush()
	n, q, x := scanInt3()
	W := scanIntSlice(n)
	s := make([]int, n+1)
	s[0] = 0
	for i:=0;i<n;i++ {
		s[i+1] = s[i] + W[i]
	}
	loop := 0
	if x > s[n] {
		loop = x / s[n]
		x -= s[n]*loop // ここでx=0になる時がある
	}
	W2 := make([]int, 2*n)
	for i := 0; i<2*n; i++ {
		idx := i % n
		if idx < 0 {
			idx += n
		}
		W2[i] = W[idx]
	}
	s2 := make([]int, 2*n+1)
	s2[0] = 0
	for i := 0; i<2*n;i++ {
		s2[i+1] = s2[i] + W2[i]
	}
	nums := make([]Poteto, n) // nums[i]はi番目のポテトから箱に入れ,入るポテトの数と次の始まりのidx
	for i:=0;i<n;i++ {
		nums[i] = bisectLeft(n, i, x, s2)
		nums[i].num += loop*n
	}
	reached := make([]bool, n)
	for i:=0;i<n;i++ {reached[i]=false}
	road := make([]int, 0, n)
	now := 0
	road = append(road, now)
	reached[now] = true
	for !reached[nums[now].to] {
		next := nums[now].to
		road = append(road, next)
		reached[next] = true
		now = next
	}
	cycleEnd := now
	cycleStart := nums[now].to
	cycle := make([]int, 0) // ループが始まってからの道のり
	cycle = append(cycle, cycleStart)
	now = cycleStart
	for {
		next := nums[now].to
		cycle = append(cycle, next)
		if next == cycleEnd {
			break
		}
		now = next
	}
	for i:=0;i<q;i++ {
		k := scanInt()
		k--
		roadLen := len(road)
		if k >= roadLen {
			k -= roadLen
			cycleLen := len(cycle)
			cycleIdx := (k % cycleLen + cycleLen) % cycleLen
			out(nums[cycle[cycleIdx]].num) 
		} else {
			out(nums[road[k]].num)	
		}
	}
}

func bisectLeft(n, startIdx, x int, s []int) Poteto {
	ok := startIdx-1 
	ng := len(s)
	bias := s[startIdx]
	for ng - ok > 1 {
		mid := (ok+ng)/2
		if s[mid] - bias < x {
			ok = mid
		} else {
			ng = mid
		}
	}
	to := (ng % n + n) % n
	return Poteto{num:ng-startIdx, to:to}
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
func newGraph(n int) Graph {
	return make([]Edges, n)
}
// Edgesのcostでのsortを可能にするためのsort.interfaceを実装
func (e Edges) Len() int {return len(e)}
func (e Edges) Swap(i, j int) {e[i], e[j] = e[j], e[i]}
func (e Edges) Less(i, j int) bool {return e[i].cost < e[j].cost}
// asc: sort.Sort(graph[i])
// dec: sort.Sort(sort.Reverce(graph[i]))