import pytest
from avl import AVLTree, Node

def test_node():
    tree = AVLTree([1])
    assert tree.node.key == 1

def test_height():
    tree = AVLTree()
    assert tree.height == -1

def test_tree_heigh_function():
    tree = AVLTree([1,5, 6, 10, 20])
    assert tree.tree_height() == 0

def test_tree():
    tree = AVLTree()
    assert tree.inorder() == []

    tree = AVLTree([12,37,44,2,11])
    assert tree.inorder() == [2,11,12,37,44]

def test_postorder_traversal():
    tree = AVLTree([10, 20, 5, 15, 25])
    assert tree.postorder_traversal() == [5, 15, 25, 20, 10]

def test_postorder_sum():
    tree = AVLTree([1, 5, 10])
    assert tree.postorder_sum() == 16

def test_preorder_traversal():
    tree = AVLTree([10,20,5,15,25])
    assert tree.preorder_traversal() == [10, 5, 20, 15, 25]

def test_find_min_max():
    tree = AVLTree([1,12,999,4])
    assert tree.find_min() == 1
    assert tree.find_max() == 999

def test_is_leaf():
    tree = AVLTree([1,2,3,4])
    leaf_node = tree.node.left
    assert leaf_node.is_leaf() is True
    assert tree.node.right.is_leaf() is False

def test_insert():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(999)
    tree.insert(1)
    assert tree.inorder() == [1, 5, 999]

def test_rebalance():
    tree = AVLTree([10, 20, 5])
    assert tree.check_balanced() is True

def test_delete_node_with_one_child():
    tree = AVLTree([10,15,5,20,25])
    tree.delete(20)
    assert tree.inorder() == [5,10,15,25]

def test_rebalance():
    tree = AVLTree([10, 20, 5])
    assert tree.check_balanced() is True

def test_rebalance():
    tree = AVLTree([10, 20, 5])
    assert tree.check_balanced() is True




