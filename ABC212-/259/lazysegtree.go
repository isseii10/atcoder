package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var wtr = bufio.NewWriter(os.Stdout)

type S struct {
	Zero, One, Inv int
}
func op(x, y S) S {
	return S{
		Zero: x.Zero + y.Zero,
		One:  x.One + y.One,
		Inv:  x.Inv + y.Inv + x.One*y.Zero,
	}
}
var e = S{One: 0, Zero: 0, Inv: 0}

type F bool
func composition(f, g F) F {
	return (f && !g) || (!f && g)
}

var id F = false

func mapping(f F, x S) S {
	if !f {
		return x
	}
	return S{
		Zero: x.One,
		One:  x.Zero,
		Inv:  x.One*x.Zero - x.Inv,
	}
}

func main() {
	defer flush()
	n, q := scanInt2()
	arr := scanIntSlice(n)
	lst := NewLazySegmentTree(n, op, e, composition, mapping, id)
	A := make([]S, n)
	for i := 0; i < n; i++ {
		if arr[i] == 0 {
			A[i] = S{Zero: 1}
		} else {
			A[i] = S{One: 1}
		}
	}
	lst.Initialize(A)
	for i := 0; i < q; i++ {
		t, l, r := scanInt3()
		l--
		r--
		switch t {
		case 1:
			lst.RangeApply(l, r+1, true)
		case 2:
			num := lst.Prod(l, r+1)
			out(num.Inv)
		}
	}
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
func (h IntMinHeap) Len() int           { return len(h) }
func (h IntMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h IntMinHeap) Less(i, j int) bool { return h[i] < h[j] }

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
	to   int
	cost int
}
type Edges []edge
type Graph []Edges

func newGraph(n int) Graph {
	return make([]Edges, n)
}

// Edgesのcostでのsortを可能にするためのsort.interfaceを実装
func (e Edges) Len() int           { return len(e) }
func (e Edges) Swap(i, j int)      { e[i], e[j] = e[j], e[i] }
func (e Edges) Less(i, j int) bool { return e[i].cost < e[j].cost }

// asc: sort.Sort(graph[i])
// dec: sort.Sort(sort.Reverce(graph[i]))

type LazySegmentTree struct {
	data        []S
	op          func(x, y S) S
	e           S
	size        int
	height      int
	composition func(f, g F) F
	mapping     func(f F, x S) S
	id          F
	lazy        []F
}

func NewLazySegmentTree(
	n int,
	op func(x, y S) S,
	e S,
	composition func(f, g F) F,
	mapping func(f F, x S) S,
	id F,
) LazySegmentTree {
	height := bits.Len64(uint64(n - 1))
	size := 1 << height
	data := make([]S, size*2)
	for i := 0; i < size*2; i++ {
		data[i] = e
	}
	lazy := make([]F, size)
	for i := 0; i < size; i++ {
		lazy[i] = id
	}
	return LazySegmentTree{
		data:        data,
		op:          op,
		e:           e,
		size:        size,
		height:      height,
		composition: composition,
		mapping:     mapping,
		id:          id,
		lazy:        lazy,
	}
}
func (l *LazySegmentTree) Initialize(arr []S) {
	for i, a := range arr {
		idx := i + l.size
		l.data[idx] = a
	}
	for i := l.size - 1; i > 0; i-- {
		l.update(i)
	}
}

//
func (l *LazySegmentTree) Set(pos int, x S) {
	pos += l.size
	l.data[pos] = x
	for i := l.height; i > 0; i-- {
		l.push(pos >> i)
	}
	l.data[pos] = x
	for i := 1; i <= l.height; i++ {
		l.update(pos >> i)
	}
}

//
func (l *LazySegmentTree) allApply(i int, f F) {
	// 内部関数
	// data[i]を更新済みにして、lazyに更新内容保存
	l.data[i] = l.mapping(f, l.data[i])
	if i < l.size {
		l.lazy[i] = l.composition(f, l.lazy[i])
	}
}

//
func (l *LazySegmentTree) push(i int) {
	// 内部関数
	// 子を更新して,lazy伝搬させる
	ii := i << 1
	iii := i<<1 | 1
	_ = ii
	_ = iii
	l.allApply(int(i<<1), l.lazy[i])
	l.allApply(int(i<<1|1), l.lazy[i])
	l.lazy[i] = l.id
}

//
func (l *LazySegmentTree) update(i int) {
	l.data[i] = l.op(l.data[i<<1], l.data[i<<1|1])
}
func (l *LazySegmentTree) Update(pos int, x S) {
	// data[pos] = x にする
	pos += l.size
	// bottom to top
	for i := l.height; i > 0; i-- {
		l.push(pos >> i)
	}
	l.data[pos] = x
	// top to bottom
	for i := 1; i <= l.height; i++ {
		l.update(pos >> i)
	}
}
func (l *LazySegmentTree) Apply(pos int, f F) {
	// data[p]にfを作用させる
	pos += l.size
	for i := l.height; i > 0; i-- {
		l.push(pos >> i)
	}
	l.data[pos] = l.mapping(f, l.data[pos])
	for i := 1; i <= l.height; i++ {
		l.update(pos >> i)
	}
}

//
func (l *LazySegmentTree) RangeApply(left, right int, f F) {
	// l, l+1, ..., r-1にfを作用させる
	if left == right {
		return
	}

	left += l.size
	right += l.size
	for i := l.height; i > 0; i-- {
		if ((left >> i) << i) != left {
			l.push(left >> i)
		}
		if ((right >> i) << i) != right {
			l.push((right - 1) >> i)
		}
	}
	left2, right2 := left, right
	for left < right {
		if left&1 == 1 {
			l.allApply(left, f)
			left++
		}
		if right&1 == 1 {
			right--
			l.allApply(right, f)
		}
		left >>= 1
		right >>= 1
	}
	left, right = left2, right2
	for i := 1; i <= l.height; i++ {
		if ((left >> i) << i) != left {
			l.update(left >> i)
		}
		if ((right >> i) << i) != right {
			l.update((right - 1) >> i)
		}
	}
}

//
func (l *LazySegmentTree) Get(pos int) S {
	pos += l.size
	for i := l.height; i > 0; i-- {
		l.push(pos >> i)
	}
	return l.data[pos]
}

//
func (l *LazySegmentTree) Prod(left, right int) S {
	if left == right {
		return l.e
	}
	left += l.size
	right += l.size
	for i := l.height; i > 0; i-- {
		if ((left >> i) << i) != left {
			l.push(left >> i)
		}
		if ((right >> i) << i) != right {
			l.push(right >> i)
			// l.push((right-1) >> i)
		}
	}
	sml := l.e
	smr := l.e
	for left < right {
		if left&1 == 1 {
			sml = l.op(sml, l.data[left])
			left++
		}
		if right&1 == 1 {
			right--
			smr = l.op(l.data[right], smr)
		}
		left >>= 1
		right >>= 1
	}
	return l.op(sml, smr)
}

//
func (l *LazySegmentTree) AllProd() S {
	return l.data[1]
}