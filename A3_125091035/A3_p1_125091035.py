class Node:
    __slots__ = ("key", "left", "right")  
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, x):
    if root is None:
        return Node(x)
    cur = root
    while True:
        if x < cur.key:
            if cur.left is None:
                cur.left = Node(x)
                return root
            cur = cur.left
        elif x > cur.key:
            if cur.right is None:
                cur.right = Node(x)
                return root
            cur = cur.right
        else: 
            return root
def delete(root, x):
    parent = None
    cur = root
    while cur is not None and cur.key != x:   
        parent = cur
        cur = cur.left if x < cur.key else cur.right
    if cur is None:                           
        return root
    # case1:2 childs
    if cur.left is not None and cur.right is not None:
        sp, succ = cur, cur.right              #
        while succ.left is not None:
            sp, succ = succ, succ.left
        cur.key = succ.key 
        parent, cur = sp, succ
    #case2/3: 0/1 child
    child = cur.left if cur.left is not None else cur.right
    if parent is None:                         
        return child
    if parent.left is cur:
        parent.left = child
    else:
        parent.right = child
    return root
def query(root, x):
    pred = succ = None
    cur = root
    while cur is not None:
        if cur.key < x:            
            pred = cur.key
            cur = cur.right
        elif cur.key > x:          
            succ = cur.key
            cur = cur.left
        else:                      
            t = cur.left          
            if t is not None:
                while t.right is not None:
                    t = t.right
                pred = t.key
            t = cur.right        
            if t is not None:
                while t.left is not None:
                    t = t.left
                succ = t.key
            break
    return pred, succ

q = int(input())
root = None
out = []
for _ in range(q):
    op, x = input().split()
    x = int(x)
    if op == "I":
        root = insert(root, x)
    elif op == "D":
        root = delete(root, x)
    else:  # "Q"
        p, s = query(root, x)
        out.append(f"{p if p is not None else 'NONE'} {s if s is not None else 'NONE'}")
print("\n".join(out)) 