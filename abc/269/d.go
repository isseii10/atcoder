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


type UnionFind struct {
	n    int
	root []int
}

func NewUnionFind(n int) UnionFind {
	root := make([]int, n)
	for i := 0; i < n; i++ {
		root[i] = -1
	}
	uf := UnionFind{n: n, root: root}
	return uf
}
func (u *UnionFind) Find(x int) int {
	if u.root[x] < 0 {
		return x
	}
	u.root[x] = u.Find(u.root[x])
	return u.root[x]
}
func (u *UnionFind) Union(x, y int) {
	x = u.Find(x)
	y = u.Find(y)
	if x == y {
		return
	}
	if -u.root[x] < -u.root[y] {
		x, y = y, x
	} // xの方がサイズ大きいように
	u.root[x] += u.root[y]
	u.root[y] = x
}
func (u *UnionFind) IsSame(x, y int) bool {
	return u.Find(x) == u.Find(y)
}
func (u *UnionFind) Size(x int) int {
	return -u.root[u.Find(x)]
}

func main() {
	defer flush()
	n := scanInt()
	blackMap := make(map[[2]int]bool)
	idxMap := make(map[[2]int]int)
	X := make([]int, n)
	Y := make([]int, n)
	for i:=0;i<n;i++ {
		x, y := scanInt2()
		X[i] = x
		Y[i] = y
		blackMap[[2]int{x, y}] = true
		idxMap[[2]int{x, y}] = i
	}
	next := [6][2]int{
		[2]int{-1, -1},
		[2]int{-1, 0},
		[2]int{0, -1},
		[2]int{0, 1},
		[2]int{1, 0},
		[2]int{1, 1},
	}
	ans := n
	used := make([]bool, n)
	var dfs func(x, y int) int
	dfs = func(x, y int) int {
		if _, ok := blackMap[[2]int{x, y}]; !ok {
			return 0
		}
		idx := idxMap[[2]int{x, y}]
		if used[idx] {
			return 0
		}
		used[idx] = true
		ret := 1
		for i := range next {
			dx := next[i][0]
			dy := next[i][1]
			ret += dfs(x+dx, y+dy)
		}
		return ret
	}
	for i:=0;i<n;i++ {
		if used[i] {
			continue
		}
		ans -= dfs(X[i], Y[i])-1
	}
	out(ans)
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
type Heap []int
func NewHeap() *Heap {
	return &Heap{}
}
func (h Heap) IsEmpty() bool {
	return len(h) == 0
}

//heapインターフェースの実装 heap化はheap.Init(hq)
func (h Heap) Len() int {return len(h)}
func (h Heap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h Heap) Less(i, j int) bool {return h[i] < h[j]}

func (h *Heap) Push(e interface{}) {
	*h = append(*h, e.(int))
}
func (h *Heap) Pop() interface{} {
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