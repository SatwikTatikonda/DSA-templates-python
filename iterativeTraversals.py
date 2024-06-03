# inorder iterative


# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

# I N O R D E R  T R A V E R S A L----------------------

# # way1------------------------------------------------------------------------------------------------
# def printInorder(root):
#     node=root
#     stack=[]
#     res=[]
#     # going to left extreme--
#     while node:
#         stack.append(node)
#         node=node.left
    
#     while stack:
#         node=stack.pop()
#         # printing the node-----
#         res.append(node.val)
#         # going to right for once--
#         new=node.right
#         # going  to left extreme---
#         while new:
#             stack.append(new)
#             new=new.left
#     print(res)

# way2----------------------------------------------------------------------------------------------------
# class pair:
#     def __init__(self,v) -> None:
#       self.data=v
#       self.task=1
# def printInorder(root):

#     stack=[]
#     res=[]
#     stack.append(pair(root))
#     while stack:
#         node=stack[-1]
#         if node.task==1:
#             node.task+=1
#             if node.data.left:
#                 stack.append(pair(node.data.left))
        
#         elif node.task==2:
#             node.task+=1
#             if node.data:
#                 res.append(node.data.val)
        
#         elif node.task==3:
#             node.task+=1
#             if node.data.right:
#                 stack.append(pair(node.data.right))
#         else:
#             stack.pop()
    
#     print(res)
        
        


# # Driver code
# if __name__ == '__main__':
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(6)
 
#     # Function call
#     print("Inorder traversal of binary tree is:")
#     printInorder(root)

# P R E O R D E R  T R A V E R S A L-------------

# way1-------------------
# def printPreorder(root):
#     stack=[]
#     res=[]
#     node=root
#     while node:
#         stack.append(node)
#         res.append(node.val)
#         node=node.left

#     while stack:
#         node=stack.pop()
#         new=node.right
#         while new:
#             stack.append(new)
#             res.append(new.val)
#             new=new.left
    
#     print(res)

# way2-----------------------
# class pair:
#     def __init__(self,v):
#         self.data=v
#         self.task=1

# def printPreorder(root):

#     stack=[]
#     res=[]
#     stack.append(pair(root))
#     while stack:
#         node=stack[-1]
#         if node.task==2:
#             node.task+=1
#             if node.data.left:
#                 stack.append(pair(node.data.left))
        
#         elif node.task==1:
#             node.task+=1
#             if node.data:
#                 res.append(node.data.val)
        
#         elif node.task==3:
#             node.task+=1
#             if node.data.right:
#                 stack.append(pair(node.data.right))
#         else:
#             stack.pop()
#     print(res)


# # Driver code
# if __name__ == '__main__':
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(6)
 
#     # Function call
#     print("preorder traversal of binary tree is:")
#     printPreorder(root)

# P O S T O R D E R T R A V E R S A L----------------------

# way1----------------------------------

class pair:
    def __init__(self,v) -> None:
        self.data=v
        self.task=1

def printPostorder(root):
    stack=[]
    stack.append(pair(root))
    res=[]
    while stack:
        
        node=stack[-1]
        if node.task==1:
            node.task+=1
            if node.data.left:
            
                stack.append(pair(node.data.left))
        
        elif node.task==2:
            node.task+=1
            if node.data.right:
               
                stack.append(pair(node.data.right))
        
        elif node.task==3:
            node.task+=1
            if node.data:
          
                 res.append(node.data.val)
        else:
            stack.pop()
    
    print(res)
        



# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
 
    # Function call
    print("postorder traversal of binary tree is:")
    printPostorder(root)