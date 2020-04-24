from abc import ABC

from Pycharm_project.exercises.FIFO_linked import LinkedQueue


class Tree:
    """Abstract tree class representing tree structure"""
    
    class Position:
        """An abstract class representing the location of a single element"""
        
        def element(self):
            """Return element stored at the Position"""
            raise NotImplementedError("must be implemented in subclass")
        
        def __eq__(self, other):
            """Return True if other Position represents the same Position"""
            raise NotImplementedError('must be implemented in a subclass')
        
        def __ne__(self, other):
            """Return True if other Position does not the same Position"""
            return not (self == other)
    
    def root(self):
        """Return the root of the tree"""
        raise NotImplementedError('must be implemented in a subclass')
    
    def parent(self, p):
        """Return the parent of Position p"""
        raise NotImplementedError("must be implemented in a subclass")
    
    def children(self, p):
        """Return the children of Position p"""
        raise NotImplementedError('must be implemented in a subclass')
    
    def num_children(self, p):
        """Return the number of children of Position p"""
        raise NotImplementedError('must be implemented in a subclass')
    
    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('must be implemented in a subclass')
    
    def is_root(self, p):
        """Return True  if Position p is the root """
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p has no children"""
        return self.num_children(p) == 0
    
    def is_empty(self, p):
        """Return True if the tree is empty"""
        return self.__len__() == 0
    
    def depth(self, p):
        """Return the number of parent of Position p.(Return the number of levels separating Position p from root)"""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))  # 递归计算父节点的深度，直到根节点。因为已知根节点的深度为0
    
    def _height1(self):  # 即所有节点的孩子节点的深度最大值， 时间复杂度O(n^2) 
        """Return the height of tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):  # 即p节点的孩子节点的最大值加1， 叶子节点的高度是0
        """Return the height of Position p"""
        if self.is_leaf(p):  # 叶子节点的高度为0
            return 0
        return 1 + max(self._height2(c) for c in self.children(p))  # 递归计算p节点的子节点的高度，直到出现叶子节点
    
    def height(self, p):
        """Return the height of Position p. If p is None, return the height of tree"""
        if p is None:
            p = self.root()
        return self._height2(p)
    
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@多种遍历算法的实现@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element

    def positions(self):
        """Generate an iteration of the tree's position"""
        return self.preorder()

    # --------------先序遍历的实现-----------------------------------------------------------
    def preorder(self):
        """Generate a preorder iteration of position in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start recursion，从整个树的root开始，递归访问子树的根
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p  # 先访问子树的根
        for c in self.children(p):  # 遍历子树的children
            for other in self._subtree_preorder(c):  # 开始递归遍历子树根
                yield other

    # ------------------后序遍历的实现-------------------------------------------------------------
    def postorder(self):
        """Generate a postorder iteration of position in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate an iteration of position in the subtree rooted at p"""
        for c in self.children(p):  # 在子树P中遍历
            for other in self._subtree_postorder(c):
                yield other
        yield p  # 子树P遍历结束后,再访问子树的根p，即所谓后序遍历

    # --------------------------------广度优先遍历的实现----------------------------------------------------------------
    def breadthfirst(self):
        """Generate a breadth-first iteration of position in the tree"""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)


class BinaryTree(Tree, ABC):
    """Abstract base class representing a binary tree structure"""
    
    def left(self, p):
        """Return the left child of Position p.
        Return None if p doesn't have a left child"""
        raise NotImplementedError('must be implemented in a subclass')
    
    def right(self, p):
        """Return the right child of Position p.
        Return None if p doesn't have a right child"""
        raise NotImplementedError('must be implemented in a subclass')
    
    def sibling(self, p):
        """Return a Position representing p's sibling( None if no sibling)"""
        parent = self.parent(p)  # 暂存p的父母节点
        if parent is None:  # 若不存在父母节点，那p必然是root根节点
            return None
        else:
            if p == self.left(parent):  # 若p是其父母节点的左侧孩子节点，则返回右侧孩子节点
                return self.right(parent)
            else:
                return self.left(parent)  # 若p是其父母节点的右侧孩子节点，则返回左侧孩子节点
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        if self.left(p):
            yield self.left(p)
        if self.right(p):  # note that it's better use "if" here, instead of "else".
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary Tree structure"""
    
    class _Node:  # Lightweight, nonpublic class for storing a node.
        __slots__ = "_element", "_right", "_left", "_parent"
        
        def __init__(self, element, right=None, left=None, parent=None):
            self._element = element
            self._parent = parent
            self._right = right
            self._left = left
    
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element()
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    
    def _validate(self, p):
        """Return associated node if position p is valid"""
        if not isinstance(self.Position, p):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # 不明白。。。。
            raise ValueError('p is no longer valid')
        return p._node  # return associated node if position p is valid
    
    def _make_position(self, node):
        """Return Position instance for given node( or None if no node)"""
        return self.Position(node) if node is not None else None
    
    def __init__(self):
        """Create an empty binary tree"""
        self._root = None
        self._size = 0
    
    def __len__(self):
        """Return the root Position of the tree( or None if tree is empty)"""
        return self._size
    
    def root(self):
        """Return the root of the tree"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent.
        To return a Position instance, self._make_position() should be invoked."""
        pnode = self._validate(p)
        return self._make_position(pnode)
    
    def right(self, p):
        pnode = self._validate(p)  # return associated node if p is valid
        return self._make_position(pnode)
    
    def left(self, p):
        pnode = self._validate(p)  # return associated node if p is valid
        return self._make_position(pnode)
    
    def num_children(self, p):
        pnode = self  # return associated node if p is valid
        count = 0
        if pnode._left is not None:  # pnode is a validated Position,
            count += 1
        if pnode._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position"""
        if self._root is not None:
            raise ValueError('Root exist')
        self._root = e
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """Create a new left child for Position p, storing e"""
        node = self._validate(p)  # return associated node if p is valid
        if node._left is not None:
            raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)  # node's left child which should be a node
        return self._make_position(node._left)
    
    def add_right(self, p, e):
        """Create a new right child for Position p, storing e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child"""
        node = self
        if node._right is not None:
            raise ValueError('right child of Position p already exists')
        self._size += 1
        node._right = self._Node(e, node)  # link node._right to its right child
        return self._make_position(node._right)  # wrap the right child of Position p and the return
    
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element"""
        node = self._validate(p)  # method _validate() returns associated node of Position p
        old = node._element
        node._element = e
        return old
    
    def _delete_node(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element stored in Position p.
        raise ValueError if Position p is invalid or p has two children"""
        node = self  # return associated node if Position p is valid
        old = node._element
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:  # break the linking between node._parent and node, reconnect node._left(or node._right) to node._parent.
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated nodes.惯例将废弃节点的父母节点设置为自己。用于self._validate()判断失效节点
        return old
    
    def _attach(self, p, t1, t2):
        """Attach t1 and t2 as left and right subtrees of external p(which has no children nodes)"""
        node = self._validate(p)  # return associated node if Position p is valid
        # if node._left is not None or node._right is not None:
        if not self.is_leaf(p):
            raise ValueError('p is not an external node')
        if not type(p) is type(t1) is type(t2):  # all three types must be exactly the same.
            raise TypeError('Three types must be exactly the same')
        self._size += len(t1) + len(t2)
        # 链接外部节点p（叶子节点）和新增的左右孩子节点p1和p2
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # set t1 instance to None
            t2._size = 0


            