class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binaryTree:

    def __init__(self, data):
        self.data = treeNode(data)


    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = treeNode(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = treeNode(data)
                else:
                    self.right.insert(data)



    def in_order_traversal(self, root):
        result= []
        if root:
            result.append(self.in_order_traversal(root.left))

            result.append(root.data)

            result.append(self.in_order_traversal(root.right))

        return result

bin_trey = binaryTree("A")