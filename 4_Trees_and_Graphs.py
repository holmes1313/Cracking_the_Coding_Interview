# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:18:37 2019

@author: z.chen7
"""

# 4. Trees and Graphs
"""
A tree is a data structure composed of nodes.
The tree cannot contain cycles.

A binary tree is a tree in which each node has up to two children.

A binary search tree (BST) is a binary tree in which every node fits a specific
ordering property: all left descendents <= n <= all right descendents. This must
be true for each node n.

A complete binary tree is a binary tree in which every level of the tree is 
fully filled, except for perhaps the last level.

A full binary tree is a binary tree in which every node has either zero or two
children.

Perfect binary tree is combination of complete binary tree and full binary tree.


# binary tree traveral
In-order traversal means to visit the left branch then the current node and 
finally the right branch

def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)

Pre-order traveral means to visit the current node before its child nodes

def preOrderTraversal(node):
    if node:
        visit(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

Post-order traveral means to visit the current node after its child nodes.

def postOrderTraversal(node):
    if node:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        visit(node)


# Binary heaps
A min-head is a complete binary tree where each node is smaller than its children.
The root, therefore, is the minimum element in the tree.

Insert:
    inserting the element at the bottom (the next available spot)
    swap the new elelment with its parent (bubble up the new element)
    
Extract minimum element:
    remove the minimum element and swap it with the last element in the heap
    swap it with one of its children (bubble down the this element)


# Graph
A graph is simply a collections of nodes (vertices) with edges between some of them.

# Adjacency List
Adjacency list is the most common way to represent a graph. Every vertex (or node)
stores a list of adjacent vertices. 

# Graph search
In depth-first search (DFS), we start at the root and explore each branch completely
before moving on to the next branch.
DFS is often preferred if we want to visit every node in the graph.

def search(root):
    if root == None:
        return
    
    visit(root)
    root.visited = True
    
    for Node in root.children:
        if Node.visited == False:   # must check if the node has been visited
            search(Node)
    

In breadth-first search (BFS), we start at the root and explore each neighbor 
before going on to any of their children.
If we want to find the shortest path (or just any path) between nodes, BFS is
generally better.
An iterative solution involving a queue usually works the best.

def search(root):
    root.visited = True
    queue = collections.dequeue().appendleft(root)
    
    while queue:
        Node = queue.pop()
        visit(Node)
        for child_node in Node.children:
            if child_node.visited == False:
                child_node.visted = True
                queue.appendleft(child_node)
                
"""
            
# Interview quesitons
import collections

# 4.1 Route between nodes
class GraphNode():
  def __init__(self, data, adjacency_list=None):
    self.data = data
    self.adjacency_list = adjacency_list or []
    
  def add_edge_to(self, node):
    self.adjacency_list += [node]

  def __str__(self):
    return self.data


def find_route(node1, node2):
    if node1.data == node2.data:
        return True
    
    queue = collections.deque()
    queue.appendleft([node1, node1.data])
    
    while queue:
        node, data = queue.pop()
        for neigbor in node.adjacency_list:
            if not hasattr(neigbor, 'visited') or not neigbor.visited:
                if neigbor == node2:
                    print(data + '->' + neigbor.data)
                    return True
                else:
                    queue.appendleft([neigbor, data + '->' + neigbor.data])
                    
        node.visited = True
    return False



def find_route2(node1, node2):
    result = []
    dfs(node1, node2, '', result)
    return result
    
def dfs(node1, node2, current, result):
    current +=  node1.data
    if node1.data == node2.data:
        result.append(current)
    
    else:
        node1.visited = True
        for neighbor in node1.adjacency_list:
            if not hasattr(neighbor, 'visited') or not neighbor.visited:
                dfs(neighbor, node2, current, result)


node_j = GraphNode('J')
node_i = GraphNode('I')
node_h = GraphNode('H')
node_d = GraphNode('D')
node_f = GraphNode('F', [node_i])
node_b = GraphNode('B', [node_j])
node_g = GraphNode('G', [node_d, node_h])
node_c = GraphNode('C', [node_g])
node_a = GraphNode('A', [node_b, node_c, node_d])
node_e = GraphNode('E', [node_f, node_a])
node_d.add_edge_to(node_a)

find_route2(node_a, node_h)    


# 4.2 Minimal Tree

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def __str__(self):
        return '(' + str(self.left) + ':L  ' +  'V:'  + str(self.val) + '  R:' + str(self.right) + ')'
        

def miniTree(array):
    if not array:
        return None
    mid = len(array) // 2
    node = TreeNode(array[mid])
    node.left = miniTree(array[:mid])
    node.right = miniTree(array[mid+1:])
    return node

print(miniTree([-10, -5, -3, 0, 1, 3, 10]))



# 4.3 List of Depths
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val) + ',' + str(self.next)
    
node_h = TreeNode('H')
node_g = TreeNode('G')
node_f = TreeNode('F')
node_e = TreeNode('E')
node_e.left = node_g
node_d = TreeNode('D')
node_d.left = node_h
node_c = TreeNode('C')
node_c.right = node_f
node_b = TreeNode('B')
node_b.left = node_d
node_b.right = node_e
node_a = TreeNode('A')
node_a.left = node_b
node_a.right = node_c

print(node_a)

def listDepth(root):
    result = collections.defaultdict(list)
    depth = 0
    dfs(root, depth, result)
    return result
    
def listDepth_dfs(node, depth, result):
    if node:
        result[depth].append(node.val)
        listDepth_dfs(node.left, depth + 1, result)
        listDepth_dfs(node.right, depth + 1, result)
        
listDepth(node_a)
    
def listDepth_bfs(root):
    result = collections.defaultdict(list)
    queue = collections.deque()
    queue.appendleft((root, 0))
    
    while queue:
        node, depth = queue.pop()
        result[depth].append(node.val)
        if node.left:
            queue.appendleft((node.left, depth+1))
        if node.right:
            queue.appendleft((node.right, depth+1))
            
    return result
    
listDepth_bfs(node_a)
    

# 4.4 Check Balanced

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, node):
        if not node:
            return 0
        
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        return max(left, right) + 1
    
    
# 4.6 Successor
"""
pseudocode

def inorderSucc(node):
    if node has right subtree:
        return leftmost node of right subtree
    else:
        while node is a right child of node.parent:
            node = node.parent
        return node.parent
        
if we hit the very end of the in-order traversal, return None
"""
class Solution6(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # right parent is used to save the parent with value > p's value
        right_parent = None
        
        # locate P
        while root.val != p.val:
            if root.val > p.val:
                # only update right parent if right parent > p
                right_parent = root
                root = root.left
            else:
                root = root.right
        #  return the leftmost child of right subtree
        if root.right:
            return self.getLeftMost(root.right)
        else:
            return right_parent
        
    def getLeftMost(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    
# 4.7 Build Order    
def findBuildOrder(projects, dependencies):
    parents = {p: set() for p in projects}
    children = collections.defaultdict(set)
    buildOrder = []
    
    for p, c in dependencies:
        parents[c].add(p)
        children[p].add(c)
    
    print(parents)
    print(children)
    
    queue = collections.deque()
    
    for p in parents:
        if not parents[p]:
            queue.appendleft(p)
            
    while queue:
        parent = queue.pop()
        buildOrder.append(parent)
        del parents[parent]
        
        for child in children[parent]:
            parents[child].remove(parent)
            if not parents[child]:
                queue.appendleft(child)
                
    if not parents:
        return buildOrder
    else:
        return False
    
findBuildOrder(['a', 'b', 'c', 'd', 'e', 'f'],
               [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')])
    

# 4.8 First Common Ancestor
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_8(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        s, l = sorted([p.val, q.val])
        return self.helper(root, s, l)
        
    def helper(self, node, p, q):
        if p <= node.val <= q:
            return node
        elif node.val > q:
            return self.helper(node.left, p, q)
        elif  node.val < p:
            return self.helper(node.right, p, q)
        
    
    

