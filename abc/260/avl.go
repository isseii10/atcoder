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
	avl := NewAVLTree()
	avl.Insert(Key(1), Value(5))
	avl.Insert(Key(3), Value(5))
	avl.Insert(Key(4), Value(5))
	avl.Insert(Key(7), Value(5))
	avl.Insert(Key(8), Value(5))
	avl.Insert(Key(11), Value(5))
	k, ok := avl.FindKthElement(1)
	out(k, ok)
	k, ok = avl.FindKthElement(3)
	out(k, ok)
	k, ok = avl.FindKthElement(10)
	out(k, ok)
	k, ok = avl.LowerBound(Key(5))
	out(k, ok)
	k, ok = avl.LowerBound(Key(15))
	out(k, ok)
	ok = avl.Delete(Key(2))
	out(ok)
	ok = avl.Delete(Key(1))
	out(ok)
	_, ok = avl.Get(Key(1))
	out(ok)
	avl.Insert(Key())

	
}

type nodeDir struct {
	node *Node
	dir  int
}
type nodeStack []nodeDir

func (s *nodeStack) Push(v nodeDir) {
	*s = append(*s, v)
}
func (s *nodeStack) Pop() nodeDir {
	old := *s
	n := len(old)
	x := old[n-1]
	*s = old[:n-1]
	return x
}
func (s *nodeStack) IsEmpty() bool {
	return len(*s) == 0
}
func (s *nodeStack) Top() nodeDir {
	return (*s)[len(*s)-1]
}

type Key int
type Value int

type Node struct {
	key                   Key   // ノードのキー 比較可能な型にする
	value                 Value // ノードの値
	leftChild, rightChild *Node // 左右の子ノード
	bias                  int   // 平衡度 (左部分木の高さ)-(右部分木の高さ)
	size                  int   // 自ノードを根とする部分木の大きさ
}

func NewNode(key Key, value Value) *Node {
	return &Node{key: key, value: value, leftChild: nil, rightChild: nil, bias: 0, size: 1}
}

type AVLTree struct {
	root *Node
}

func NewAVLTree() AVLTree {
	return AVLTree{root: nil}
}

func (a *AVLTree) rotateLeft(v *Node) *Node {
	u := v.rightChild
	u.size = v.size
	if u.rightChild != nil {
		v.size -= u.rightChild.size + 1
	} else {
		v.size -= 1
	}
	v.rightChild = u.leftChild
	u.leftChild = v
	if u.bias == -1 {
		u.bias = 0
		v.bias = 0
	} else {
		u.bias = 1
		v.bias = -1
	}
	return u
}
func (a *AVLTree) rotateRight(v *Node) *Node {
	u := v.leftChild
	u.size = v.size
	if u.leftChild != nil {
		v.size -= u.leftChild.size + 1
	} else {
		v.size -= 1
	}
	v.leftChild = u.rightChild
	u.rightChild = v
	if u.bias == 1 {
		u.bias = 0
		v.bias = 0
	} else {
		u.bias = -1
		v.bias = 1
	}
	return u
}
func (a *AVLTree) rotateLR(v *Node) *Node {
	u := v.leftChild
	t := u.rightChild
	t.size = v.size
	if t.rightChild != nil {
		v.size -= u.size - t.rightChild.size
		u.size -= t.rightChild.size + 1
	} else {
		v.size -= u.size
		u.size -= 1
	}
	u.rightChild = t.leftChild
	t.leftChild = u
	v.leftChild = t.rightChild
	t.rightChild = v
	a.updateBiasDouble(t)
	return t
}
func (a *AVLTree) rotateRL(v *Node) *Node {
	u := v.rightChild
	t := u.leftChild
	t.size = v.size
	if t.leftChild != nil {
		v.size -= u.size - t.leftChild.size
		u.size -= t.leftChild.size + 1
	} else {
		v.size -= u.size
		u.size -= 1
	}
	u.leftChild = t.rightChild
	t.rightChild = u
	v.rightChild = t.leftChild
	t.leftChild = v
	a.updateBiasDouble(t)
	return t
}
func (a *AVLTree) updateBiasDouble(v *Node) {
	switch v.bias {
	case 1:
		v.rightChild.bias = -1
		v.leftChild.bias = 0
	case -1:
		v.rightChild.bias = 0
		v.leftChild.bias = 1
	default:
		v.rightChild.bias = 0
		v.leftChild.bias = 0
	}
	v.bias = 0
}
func (a *AVLTree) Insert(key Key, value Value) {
	if a.root == nil {
		a.root = NewNode(key, value)
		return
	}
	v := a.root
	history := make(nodeStack, 0)
	for v != nil {
		if key < v.key {
			history.Push(nodeDir{v, 1})
			v = v.leftChild
		} else if key > v.key {
			history.Push(nodeDir{v, -1})
			v = v.rightChild
		} else {
			v.value = value
			return
		}
	}
	p := history.Top()
	if p.dir == 1 {
		p.node.leftChild = NewNode(key, value)
	} else {
		p.node.rightChild = NewNode(key, value)
	}

	var newV *Node
	for !history.IsEmpty() {
		v, direction := history.Top().node, history.Top().dir
		history.Pop()
		v.bias += direction
		v.size++

		bias := v.bias
		if bias == 0 {
			break
		}
		if bias == 2 {
			u := v.leftChild
			if u.bias == -1 {
				newV = a.rotateLR(v)
			} else {
				newV = a.rotateRight(v)
			}
			break
		}
		if bias == -2 {
			u := v.rightChild
			if u.bias == 1 {
				newV = a.rotateRL(v)
			} else {
				newV = a.rotateLeft(v)
			}
			break
		}
	}
	if newV != nil {
		if history.IsEmpty() {
			a.root = newV
			return
		}
		p := history.Pop()
		p.node.size++
		if p.dir == 1 {
			p.node.leftChild = newV
		} else {
			p.node.rightChild = newV
		}
	}
	for !history.IsEmpty() {
		p := history.Pop()
		p.node.size++
	}
}
func (a *AVLTree) Delete(key Key) bool {
	v := a.root
	history := make(nodeStack, 0)
	found := false
	for v != nil {
		if key < v.key {
			history = append(history, nodeDir{v, 1})
			v = v.leftChild
		} else if v.key < key {
			history = append(history, nodeDir{v, -1})
			v = v.rightChild
		} else {
			found = true
			break
		}
	}
	if !found {
		return false
	}
	if v.leftChild != nil {
		history = append(history, nodeDir{v, 1})
		leftMax := v.leftChild
		for leftMax.rightChild != nil {
			history = append(history, nodeDir{leftMax, -1})
			leftMax = leftMax.rightChild
		}
		v.key = leftMax.key     // 要らないかも
		v.value = leftMax.value // 要らないかも
		v = leftMax
	}
	var c *Node
	if v.leftChild != nil {
		c = v.leftChild
	} else {
		c = v.rightChild
	}
	if len(history) != 0 {
		p, pdir := history.Top().node, history.Top().dir
		if pdir == 1 {
			p.leftChild = c
		} else {
			p.rightChild = c
		}
	} else {
		a.root = c
		return true
	}
	var newP *Node
	for !history.IsEmpty() {
		p, pdir := history.Top().node, history.Top().dir
		history.Pop()
		p.bias -= pdir
		p.size -= 1

		b := p.bias
		if b == 2 {
			if p.leftChild.bias == -1 {
				newP = a.rotateLR(p)
			} else {
				newP = a.rotateRight(p)
			}
		} else if b == -2 {
			if p.rightChild.bias == 1 {
				newP = a.rotateRL(p)
			} else {
				newP = a.rotateLeft(p)
			}
		} else if b != 0 {
			break
		}
		if newP != nil {
			if history.IsEmpty() {
				a.root = newP
				return true
			}
			gp, gpDir := history.Top().node, history.Top().dir
			if gpDir == 1 {
				gp.leftChild = newP
			} else {
				gp.rightChild = newP
			}
			if newP.bias != 0 {
				break
			}
		}
	}
	for !history.IsEmpty() {
		p := history.Top().node
		history.Pop()
		p.size--
	}
	return true
}

// mapみたいに _, ok := avl.Get(k)して存在確認する
func (a *AVLTree) Get(key Key) (Value, bool) {
	v := a.root
	for v != nil {
		if key < v.key {
			v = v.leftChild
		} else if v.key < key {
			v = v.rightChild
		} else {
			return v.value, true
		}
	}
	var zero Value
	return zero, false
}

// 指定されたkey以上で最小のkeyを返す。 boolで存在判定
func (a *AVLTree) LowerBound(key Key) (Key, bool) {
	var ret Key
	v := a.root
	// retに値が代入されているかどうか
	retIsEmpty := true
	for v != nil {
		if v.key >= key {
			if retIsEmpty || ret > v.key {
				ret = v.key
				retIsEmpty = false
			}
			v = v.leftChild
		} else {
			v = v.rightChild
		}
	}
	return ret, !retIsEmpty
}

// 指定されたkey未満で最大のkeyを返す。 boolで存在判定
func (a *AVLTree) UpperBound(key Key) (Key, bool) {
	var ret Key
	v := a.root
	retIsEmpty := true
	for v != nil {
		if v.key < key {
			if retIsEmpty || ret < v.key {
				ret = v.key
			}
			v = v.rightChild
		} else {
			v = v.leftChild
		}
	}
	return ret, !retIsEmpty
}
func (a *AVLTree) FindKthElement(k int) (Key, bool) {
	v := a.root
	s := 0
	for v != nil {
		t := 0
		if v.leftChild != nil {
			t = s + v.leftChild.size
		} else {
			t = s
		}
		if t == k {
			return v.key, true
		} else if t < k {
			s = t + 1
			v = v.rightChild
		} else {
			v = v.leftChild
		}
	}
	var zero Key
	return zero, false
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