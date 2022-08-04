package library

type UnionFind struct {
	n    int
	root []int
}

func newUnionFind(n int) UnionFind {
	root := make([]int, n)
	for i := 0; i < n; i++ {
		root[i] = -1
	}
	uf := UnionFind{n: n, root: root}
	return uf
}
func (u *UnionFind) find(x int) int {
	if u.root[x] < 0 {
		return x
	}
	u.root[x] = u.find(u.root[x])
	return u.root[x]
}
func (u *UnionFind) union(x, y int) {
	x = u.find(x)
	y = u.find(y)
	if x == y {
		return
	}
	if -u.root[x] < -u.root[y] {
		x, y = y, x
	} // xの方がサイズ大きいように
	u.root[x] += u.root[y]
	u.root[y] = x
}
func (u *UnionFind) isSame(x, y int) bool {
	return u.find(x) == u.find(y)
}
func (u *UnionFind) size(x int) int {
	return -u.root[u.find(x)]
}
