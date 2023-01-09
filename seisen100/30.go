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
	H, W, N := scanInt3()
	field := make([][]string, H+2)
	for i := range field {
		if i == 0 || i == len(field)-1 {
			field[i] = make([]string, W+2)
			for j := range field[i] {
				field[i][j] = "X"
			}
			continue
		}
		field[i] = make([]string, 0)
		field[i] = append(field[i], "X")
		field[i] = append(field[i], strings.Split(scanString(), "")...)
		field[i] = append(field[i], "X")
	}
	var sy, sx int
	var gy, gx int
	for i := range field {
		for j := range field[i] {
			if field[i][j] == "S" {
				sy = i-1
				sx = j-1
			}
			if field[i][j] == strconv.Itoa(N) {
				gy = i-1
				gx = j-1
			}
		}
	}
	q := NewQueue()
	dist := make([][][]int, H)
	for i := range dist {
		dist[i] = make([][]int, W)
		for j := range dist[i] {
			dist[i][j] = make([]int, N+1)
			for k := range dist[i][j] {
				dist[i][j][k] = -1
			}
		}
	}
	D := [][2]int{
		{0, 1},
		{0, -1},
		{1, 0},
		{-1, 0},
	}
	q.Push([2]int{sy, sx})
	target := 1
	dist[sy][sx][1] = 0
	L: 
		for !q.IsEmpty() {
			p := q.Pop().([2]int)
			py := p[0]
			px := p[1]
			for _, d := range D {
				cy := py + d[0]
				cx := px + d[1]
				if field[cy+1][cx+1] == "X" {
					continue
				}
				if dist[cy][cx][target] != -1 {
					continue
				}
				dist[cy][cx][target] = dist[py][px][target] + 1
				if field[cy+1][cx+1] == strconv.Itoa(target) {
					if target == N {
						break L
					}
					dist[cy][cx][target+1] = dist[cy][cx][target]
					target++
					q = NewQueue()
					q.Push([2]int{cy, cx})
					break
				}
				q.Push([2]int{cy, cx})
			}
		}
	out(dist[gy][gx][N])
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

func outIntSlice(sl []int) {
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
// mod
// =====================================================================================

// modを法としてa+b
func modAdd(a, b int) int {
	ret := a + b
	if ret < 0 {
		ret += mod
	}
	return ret % mod
}

func modSub(a, b int) int {
	ret := a - b
	if ret < 0 {
		ret += mod
	}
	return ret % mod
}
// modを法としてa*b
func modMulti(a, b int) int {
	return a * b % mod
}
// modを法としてa/b
func modDiv(a, b int) int {
	a %= mod
	return a * modInvFermat(b, mod) % mod
}

// mを法としてa^nを求める
func modPow(a, n, m int) int {
	if m == 1 {
		return 0
	}
	r := 1
	for n > 0 {
		if n&1 == 1 {
			r = r * a % m
		}
		a, n = a*a%m, n>>1
	}
	return r
}

// mを法としてaの逆元を求める
func modInv(a, m int) int {
	p, x, u := m, 1, 0
	for p != 0 {
		t := a / p
		a, p = p, a-t*p
		x, u = u, x-t*u
	}
	x %= m
	if x < 0 {
		x += m
	}
	return x
}

// フェルマーの小定理を用いてaの逆元を求める
// mは素数
func modInvFermat(a, m int) int {
	return modPow(a, m-2, mod)
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
func NewStack() *Stack {
	return &Stack{}
}
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
type Queue []interface{}
func NewQueue() *Queue {
	return &Queue{}
}
func (q *Queue) Push(v interface{}) {
	*q = append(*q, v)
}
func (q *Queue) Pop() interface{} {
	old := *q
	x := old[0]
	*q = old[1:]
	return x
}
func (q *Queue) IsEmpty() bool {
	return len(*q) == 0 
}
// deque
type Deque []int
func NewDeque() *Deque {
	return &Deque{}
}
func (d *Deque) PushRight(v int) {
	*d = append(*d, v)
}
func (d *Deque) PushLeft(v int) {
	*d = append([]int{v}, *d...)
}
func (d *Deque) PopLeft() int {
	old := *d
	x := old[0]
	*d = old[1:]
	return x
}
func (d *Deque) PopRight() int {
	old := *d
	n := len(old)
	x := old[n-1]
	*d = old[:n-1]
	return x
}
func (d *Deque) IsEmpty() bool {
	return len(*d) == 0 
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
// desc: sort.Sort(sort.Reverse(graph[i]))