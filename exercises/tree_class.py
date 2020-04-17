class Tree:
    """Abstract base class representing a tree structure"""

    # --------------------nested class--------------------------------------------
    class Position:
        """An abstraction representing the location of a single element """

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other Position does not represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")

    # ---------------------abstract methods that concrete subclass must support---------------------------
    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if empty)"""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return number of p's children Position"""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")

    # -------------------concrete methods implemented in this class------------------------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree """
        return p == self.root()

    def is_leaf(self, p):
        """Return True if Position p represents the leaf of the tree"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root
        p的深度就是p的祖先的个数（当然，不计p本身）"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))  # recursive invoke upwards, 本函数O(n), n代表树中节点的总数。

    def _height1(self):  # works, but O(n^2) worst-case time
        """Return the height of the tree"""
        # 叶子节点的depth的最大值
        return max(self._height1(p) for p in self.positions() if self.is_leaf(p))  # 还需另定义position方法，该方法O(n)

    def _height2(self, p):
        """Return the height of subtree rooted at Position p,
        计算一个以p节点为根节点的子树的高度
        it's very important for you to understand the mechanism why _height2 is more efficient than _height1"""
        if self.is_leaf(p):  # time is linear in size of subtree,O(n)
            return 0
        else:
            return 1 + max(self._height2(p) for p in self.children(p))  # children方法返回一个节点迭代器

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p,

        if p is None, return the height of the entire tree"""
        if p is None:
            return self.root()
        return self._height2(p)













