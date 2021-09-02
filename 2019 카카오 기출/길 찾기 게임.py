import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정

class Tree:
    def __init__(self, dataList):
        self.data = max(dataList, key= lambda x: x[1])
        leftList = list(filter(lambda x:x[0]<self.data[0], dataList))
        rightList = list(filter(lambda x:x[0]>self.data[0], dataList))
        
        if leftList != []:
            self.left = Tree(leftList)
        else:
            self.left = None
        if rightList != []:
            self.right = Tree(rightList)
        else:
            self.right = None

def order(node, postList, preList): #전위, 후위
    postList.append(node.data)  #root 먼저 삽입
    if node.left is not None:
        order(node.left, postList, preList)
    if node.right is not None:
        order(node.right, postList, preList)
    preList.append(node.data)  #root 마지막에 삽입
    
def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    postList = []
    preList = []
    order(root, postList, preList)
    
    answer.append(list(map(lambda x: nodeinfo.index(x)+1, postList)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1, preList)))
    return answer