#import random, math
from __future__ import print_function

#outputdebug = False
OUTPUTDEBUG = False

def debug(msg):
    if OUTPUTDEBUG:
        print(msg)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __eq__(self, node2):
        if node2 is None:
            return False
        if self.key != Node(node2).key:
            return False
        try:
            if self.height != node2.height:
                return False
        except:
            pass
        if not self.left == node2.left:
            return False
        if not self.right == node2.right:
            return False
        return True
    def __ne__(self, node2):
        return not self == node2

class AVLTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def __eq__(self,other):
        if other is None:
            return False
        if self.height != other.height:
            return False
        if self.balance != other.balance:
            return False
        if not self.node == other.node:
            return False
        return True

    def __ne__(self,other):
        return not self == other

    def tree_height(self):
        if self.node:
            try:
                return self.node.height
            except:
                return 0
        else:
            return 0

    #newly added function
    def postorder_traversal(self):
        #check for empty tree case
        if self.node is None:
            #set result
            return []
        # set traversal list
        result = []
        #traverse left
        if self.node.left is not None:
            #recurse left
            result.extend(self.node.left.postorder_traversal())
        #traverse right
        if self.node.right is not None:
            #recurse right
            result.extend(self.node.right.postorder_traversal())
        #add the root
        result.append(self.node.key)
        #return result
        return result

    #newly added function
    def postorder_sum(self):
        #check for empty tree case
        if self.node is None:
            result = 0
        #get the sum of the left side
        if self.node.left.node:
            #recurse through left side
            leftsum = self.node.left.postorder_sum()
        #otherwise assume end of nodes
        else:
            leftsum = 0
        #get the sum of the right side
        if self.node.right.node:
            #recurse through right side
            rightsum = self.node.right.postorder_sum()
        #otherwise assume end of nodes
        else:
            rightsum = 0
        #assign and return result
        result = leftsum + rightsum + self.node.key
        return result

    #newly added function
    def preorder_traversal(self):
        #check for empty tree case
        if self.node is None:
            return []
        #start at root node
        result = [self.node.key]
        #traverse left side
        if self.node.left is not None:
            result.extend(self.node.left.preorder_traversal())
        #traverse right side
        if self.node.right is not None:
            result.extend(self.node.right.preorder_traversal())

        return result

    #newlly added function
    def find_min(self):
        #set a temp value
        temp = self.node
        #check for empty tree case
        if temp is None:
            result = None
        #search the left side for smallest while not empty
        else:
            while temp.left.node is not None:
                #iterate left
                temp = temp.left.node
            #set the result
            result = temp.key
        return result

    #newly added function
    def find_max(self):
        #set a temp value
        temp = self.node
        #check for empty tree case
        if temp is None:
            result = None
        # search the right side for largest while not empty
        else:
            while temp.right.node is not None:
                #iterate right
                temp = temp.right.node
            #set result
            result =  temp.key
        return result

    def is_leaf(self):
        return self.height == 0

    def find(self, key):
        tree = self.node

        if tree is None:
            return False

        if key == tree.key:
            return True

        if key < tree.key:
            return self.node.left.find(key)
        if key > tree.key:
            return self.node.right.find(key)

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree is None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")
        self.rebalance()

    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.updateheights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate() # we're in case II
                    self.updateheights()
                    self.update_balances()
                self.rrotate()
                self.updateheights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.updateheights()
                    self.update_balances()
                self.lrotate()
                self.updateheights()
                self.update_balances()



    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T


    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T


    def updateheights(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateheights()
                if self.node.right is not None:
                    self.node.right.updateheights()

            self.height = max(self.node.left.height,self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node is not None:
            if self.node.key == key:
                debug("Deleting ... " + str(key))
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement is not None: # sanity check
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)
                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node is not None: # just a sanity check

            while node.left is not None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        # We always need to make sure we are balanced
        self.updateheights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and
                                                self.node.right.check_balanced())

    def inorder(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.inorder()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.updateheights()  # Must update heights before balances
        self.update_balances()
        if self.node is not None:
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" +
                                                          str(self.balance) + "]", end=' ')
            if self.is_leaf():
                print('L')
            else:
                print()
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.left is not None:
                self.node.right.display(level + 1, '>')
