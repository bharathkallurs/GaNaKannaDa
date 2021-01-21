"""
GaNaKannaDa: Binary Tree
Problem: Show case insert, delete, inorder, preorder, postorder
         and level order traversal in a binary tree.

Binary Tree:
Binary Tree is one of the non-linear data structures.
It has a maximum of 2 children per node. The tree starts from root node
at 0th level. Then proceeds to first level with left child and right child.
It then goes ahead and branches further untill leaf nodes are reached.
Leaf nodes are the ones without any children further.

"""


class TreeNode(object):
    """Class to create a tree node with data and left, right pointers
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """Class to define tree and its functions
    """

    def insert(self, root, data):
        """
        Insert data node into tree in level order fashion

        Level order indicates parsing the tree based on each level of it.
        Example, root node from level 0, root's children from level 1, and so on.
        We insert a node into the tree as soon as we see an empty space in the
        left most region in a given level.

        Steps:
        1. Check if root node is null, if yes insert root node and return
        2. Create a queue and add the root node to it
        3. While the length of queue is not null, iterate
        4. Get the first node of the queue from left and put it in a temp variable
        5. If temp.left is null, then insert new tree node here
        6. Else append temp.left to queue
        7. If temp.right is null, then insert new tree node here
        8. Else append temp.right to queue
        9. Return once the new node is inserted in any one place as mentioned
           in point 5 to 8 
        """
        if not root:
            root = TreeNode(data)
            return

        qu = list()
        qu.append(root)
        # print(qu)
        while len(qu):
            temp = qu.pop(0)

            if not temp.left:  # Checks if root.left node is None
                temp.left = TreeNode(data)
                print("left node ", temp.left.data)
                return
            else:
                qu.append(temp.left)

            if not temp.right:  # Checks if root.right node is None
                temp.right = TreeNode(data)
                print("right node", temp.right.data)
                return
            else:
                qu.append(temp.right)

    def inOrder(self, root):
        """
        Inorder tree traversal
        Draw a sample tree like 3 vertices of a triangle.
        Left verex first, root vertex next, right vertex last is inOrder.

        """
        if root:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    def preOrder(self, root):
        """
        PreOrder tree traversal
        Draw a sample tree like 3 vertices of a triangle.
        Root vertex first, left vertex next, Right vertex last is preOrder.
        """
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        """
        PostOrder tree traversal
        Draw a sample tree like 3 vertices of a triangle.
        Left verex first, right vertex next, root vertex last is postOrder.
        """
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)

    def delete(self, root, data):
        """Delete a node from the tree matching the data variable

        In deletion also we follow level order based node deletion.
        We ensure that we always delete nodes from right most end by
        copying the data of right most end's node to the node's data 
        that we actually want to delete
        Steps:
        1. Check if root node is null, if yes then return none
        2. Else check if root's left and right children are none.
        3. If yes return root else return none
        4. Create a list and append the root node to it
        5. While the length of the queue is not zero iterate
        6. Get the first node in queue into temp variable
        7. check if data if that matches with data to be deleted.
        8. If yes, mark it as node_to_delete
        9. Else, check if temp.left is not none, add it to list
        10. Check if temp.right is not none, add it to list
        11. Once the while loop completes, if node_to_delete is not none, get right most node from the tree
        12. Assign the data of node_to_delete with right most node's data.
        Returns:
            root node of the new tree formed post deletion
        """
        if not root:
            return None

        if not root.left and not root.right:
            if data == root.data:
                return root
            else:
                return None

        qu = list()
        qu.append(root)

        node_to_delete = None
        while len(qu):
            temp = qu.pop(0)

            if temp.data == data:
                node_to_delete = temp

            if temp.left:
                qu.append(temp.left)
            if temp.right:
                qu.append(temp.right)

        if node_to_delete:
            x = temp.data
            right_most_node = self._getRightMostNode(root, temp)
            node_to_delete.data = x
        return root

    def printTreeInLevelOrder(self, root):
        """Prints a given tree in level order
        """
        if not root:
            print("Root is NULL so not printing anything")
            return

        qu = list()
        qu.append(root)
        while len(qu):
            temp = qu.pop(0)
            print(temp.data, " ")

            if temp.left:
                qu.append(temp.left)

            if temp.right:
                qu.append(temp.right)

    def _getRightMostNode(self, root, to_delete_node):
        """
        Get the right most node from the tree. (Check step 11 in delete code above)
        """
        q = []
        q.append(root)
        while(len(q)):
            temp = q.pop(0)
            if temp is to_delete_node:
                temp = None
                return
            if temp.right:
                if temp.right is to_delete_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is to_delete_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)


if __name__ == "__main__":
    tree = Tree()
    root = TreeNode(6)
    print("Inserting nodes to tree")
    # insert nodes to tree
    tree.insert(root, 8)
    tree.insert(root, 10)
    tree.insert(root, 12)
    tree.insert(root, 14)
    tree.insert(root, 16)

    print("Printing level order tree traversal")
    # print tree nodes in level order
    tree.printTreeInLevelOrder(root)

    print("Printing inorder tree traversal")
    # inorder traversal of tree
    tree.inOrder(root)

    print("Printing preorder tree traversal")
    # preorder traversal of tree
    tree.preOrder(root)

    print("Printing postorder tree traversal")
    # postorder traversal of tree
    tree.postOrder(root)

    print("Deleting nodes from tree")
    # delete nodes from tree
    new_root = tree.delete(root, 12)
    # print tree nodes in level order
    tree.printTreeInLevelOrder(new_root)
