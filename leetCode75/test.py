class TreeNode(object):
    def __init__(self,val) -> None:
        self.left=None
        self.right=None
        self.val=val
    def __str__(self) -> str:
        return f"{self.val}"


def printTree(root:TreeNode):
    res=[]
    stack=[root]
    while len(stack) > 0:
        node=stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res



def serialize(root:TreeNode):
    if root==None:
        return []
    stack=[root]
    result=[]
    while len(stack):
        currentNode=stack.pop()
        result.append(str(currentNode.val))
        if currentNode.right!=None:
            stack.append(currentNode.right)
        else:
            result.append("N")
        if currentNode.left!=None:
            stack.append(currentNode.left)
        else:
            result.append("N")
    return   ",".join(result)

class Code:
    def deserialize(self,inputStr:str):
        vals=inputStr.split(",")
        self.i=0

        def dfs(self):
            if vals[self.i]=="N":
                self.i+=1
                return None
            node=TreeNode(int(vals[self.i]))
            self.i+=1
            node.left=dfs(self)
            node.right=dfs(self)
            return node
        return dfs(self)


one=TreeNode(1)
two=TreeNode(2)
three=TreeNode(3)
four=TreeNode(4)
five=TreeNode(5)

one.left=two
one.right=three
three.left=four
three.right=five


print(printTree(one))
serialized=serialize(one)
print(serialized)
print(printTree(Code().deserialize(serialized)))



