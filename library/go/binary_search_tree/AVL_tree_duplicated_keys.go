package binary_search_tree

type Key int
type Value struct {
	num int
	cards []int
}
func NewValue(x int) Value {
	cards := make([]int, 0)
	cards = append(cards, x)
	return Value{num: 1, cards: cards}
}

type Node struct {
	key                   Key   // ノードのキー 比較可能な型にする
	value                 Value // ノードの値
	leftChild, rightChild *Node // 左右の子ノード
	bias                  int   // 平衡度 (左部分木の高さ)-(右部分木の高さ)
	size                  int   // 自ノードを根とする部分木の大きさ
}

func newNode(key Key, value Value) *Node {
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
	w := u.rightChild
	w.size = v.size
	if w.rightChild != nil {
		v.size -= u.size - w.rightChild.size
		u.size -= w.rightChild.size + 1
	} else {
		v.size -= u.size
		u.size -= 1
	}
	u.rightChild = w.leftChild
	w.leftChild = u
	v.leftChild = w.rightChild
	w.rightChild = v
	a.updateBiasDouble(w)
	return w
}
func (a *AVLTree) rotateRL(v *Node) *Node {
	u := v.rightChild
	w := u.leftChild
	w.size = v.size
	if w.leftChild != nil {
		v.size -= u.size - w.leftChild.size
		u.size -= w.leftChild.size + 1
	} else {
		v.size -= u.size
		u.size -= 1
	}
	u.leftChild = w.rightChild
	w.rightChild = u
	v.rightChild = w.leftChild
	w.leftChild = v
	a.updateBiasDouble(w)
	return w
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
		a.root = newNode(key, value)
		return
	}
	// 挿入地点まで探索
	v := a.root
	history := make(nodeStack, 0)
	for v != nil {
		if key <= v.key {
			history.Push(nodeDir{v, 1})
			v = v.leftChild
		} else if v.key < key {
			history.Push(nodeDir{v, -1})
			v = v.rightChild
		}
	}
	p, pdir := history.Top().node, history.Top().dir
	if pdir == 1 {
		p.leftChild = newNode(key, value)
	} else {
		p.rightChild = newNode(key, value)
	}
	// バランス回復
	var newV *Node = nil
	for !history.IsEmpty() {
		v, direction := history.Top().node, history.Top().dir
		history.Pop()
		v.bias += direction
		v.size++
		newV = nil
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
		p, pdir := history.Top().node, history.Top().dir
		history.Pop()
		p.size++
		if pdir == 1 {
			p.leftChild = newV
		} else {
			p.rightChild = newV
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
		} else if key > v.key {
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
	// vは削除対象のノード
	if v.leftChild != nil {
		history = append(history, nodeDir{v, 1})
		// leftMax: vの左部分木の中で最大のキーを持つノード
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
		newP = nil
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
		p := history.Pop().node
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
		} else if key > v.key {
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
	retExists := false 
	for v != nil {
		if v.key >= key {
			if !retExists || ret > v.key {
				ret = v.key
				retExists = true
			}
			v = v.leftChild
		} else {
			v = v.rightChild
		}
	}
	return ret, retExists
}

// 指定されたkey未満で最大のkeyを返す。 boolで存在判定
func (a *AVLTree) UpperBound(key Key) (Key, bool) {
	var ret Key
	v := a.root
	retExists := false
	for v != nil {
		if v.key < key {
			if !retExists || ret < v.key {
				ret = v.key
				retExists = true
			}
			v = v.rightChild
		} else {
			v = v.leftChild
		}
	}
	return ret, retExists
}
// kは0-indexed
func (a *AVLTree) FindKthElement(k int) (Key, bool) {
	v := a.root
	s := 0
	for v != nil {
		vLeftChiledSize := 0
		if v.leftChild != nil {
			vLeftChiledSize = v.leftChild.size
		}
		t := s + vLeftChiledSize
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