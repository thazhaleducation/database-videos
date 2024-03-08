class Key():
  def __init__(self, val, record):
    self.val = val
    self.record = record
    
  def __str__(self) -> str:
    return f"{self.val} -> {self.record}"
  
  def is_lt(self, oKey):
    return self.val < oKey.val
  
  def is_gt(self, oKey):
    return self.val > oKey.val

class Node():
  def __init__(self, key: Key):
    self.key: Key = key
    self.left: Node|None = None
    self.right: Node|None = None
    self.height: int = 1
  
  def __str__(self) -> str:
    return f"key: {self.key}"

class AvlTree():
  def __init__(self):
    self.root = None
  
  def add(self, key: Key):
    self.root = self._add_child(self.root, key)

  def search(self, val):
    return self._search(self.root,  val)

  def _search(self, parent: Node, val):
    if parent is None:
      return None
    elif parent.key.val == val:
      return parent
    elif parent.key.val < val:
      return self._search(parent.right, val)
    else:
      return self._search(parent.left, val)

      
  def delete(self, key: Key):
    pass
  
  def pre_order(self):
    self._pre_order(self.root)

  def _pre_order(self, parent: Node, level="-"):
    if parent is None:
      return ""
    else:
      print(f"{level}{parent.key}")
      self._pre_order(parent.left, level+"-")
      self._pre_order(parent.right, level+"-")

  def _add_child(self, parent: Node, key: Key):
    if parent is None:
      return Node(key)
    elif key.val < parent.key.val:
      parent.left = self._add_child(parent.left, key)
    else:
      parent.right = self._add_child(parent.right, key)
    
    parent.height = 1 + max(self._height(parent.left), self._height(parent.right))
    balance_factor = self._get_balance_factor(parent)

    if balance_factor > 1 and key.is_lt(parent.left.key):
      return self._r_rotation(parent)

    if balance_factor < -1 and key.is_gt(parent.right.key):
      return self._l_rotation(parent)

    if balance_factor > 1 and key.is_gt(parent.left.key):
      parent.left = self._l_rotation(parent.left)
      return self._r_rotation(parent)

    if balance_factor < -1 and key.is_lt(parent.right.key):
      parent.right = self._r_rotation(parent.right)
      return self._l_rotation(parent)
  
    return parent

  def _height(self, root: Node):
    if root is None:
      return 0
    
    return root.height

  def _balance(self, parent: Node, key: Key):
    pass
  
  def _get_balance_factor(self, parent: Node):
    if parent is None:
      return 0
    return self._height(parent.left) - self._height(parent.right)
  
  def _l_rotation(self, parent: Node):

    newParent = parent.right
    currentLeft = newParent.left
    newParent.left = parent
    parent.right = currentLeft
    parent.height = 1 + max(self._height(parent.left), self._height(parent.right))
    newParent.height = 1 + max(self._height(newParent.left), self._height(newParent.right))
    return newParent
    
  def _r_rotation(self, parent: Node):
    newParent = parent.left
    currentRight = parent.left.right
    newParent.right = parent
    parent.left = currentRight
    parent.height = 1 + max(self._height(parent.left), self._height(parent.right))
    newParent.height = 1 + max(self._height(newParent.left), self._height(newParent.right))
    return newParent




tree = AvlTree()
for k in range(1, 50):
  tree.add(Key(k, f"{k}Test"))

print(tree.search(1))
print(tree.search(51))
print(tree.search(30))

# tree.add(Key(2, "two"))
# tree.add(Key(3, "three"))
# tree.add(Key(4, "three"))
# tree.add(Key(5, "three"))
# tree.add(Key(6, "three"))
# tree.add(Key(7, "three"))
# tree.add(Key(8, "three"))
# tree.add(Key(9, "three"))
# tree.add(Key(10, "three"))
# tree.add(Key(11, "three"))
# tree.add(Key(12, "three"))
# tree.add(Key(13, "three"))
# tree.add(Key(14, "three"))
# tree.add(Key(15, "three"))
# tree.add(Key(16, "three"))
# tree.add(Key(17, "three"))
# tree.add(Key(18, "three"))
# tree.add(Key(19, "three"))
# tree.add(Key(20, "three"))
# tree.add(Key(21, "three"))
# tree.pre_order()
