# print('hello world')

# -----python数据结构与算法-----

# 栈

# -------------------------------

# 顺序栈
# 栈的初始化
# def init_(self):
#     self.top=0
#     self.maxsize=50
#     self.stack=[None for x in range(0,self.maxsize)]
# # 如果你写成 def init_(self):，它就是一个普通的“自定义方法”，不会在你创建对象（比如 s = Stack()）时自动执行。
#
# def __init__(self):
#     self.top = 0
#     self.maxsize = 50
#     self.stack = [None for x in range(0, self.maxsize)]
# # 只有写成 __init__，Python 才会在你创建对象的那一刻自动调用它。
# def stackempty(self):      # 判断栈是否为空
#     if self.top == 0:
#         return True
#     else:
#         return False
# def gettop(self):          # 取栈顶元素
#     if self.stacksmpty():
#         print('栈为空，取栈顶元素失败')
#         return None
#     else:
#         return self.stack[self.top-1]
# def pushstack(self,x):     # 入栈操作
#     if self.top >=self.maxsize :
#         print('栈已满')
#         return False
#     else:
#         self.stack[self.top] = x
#         self.top += 1
#         return True
# def popstack(self):        # 出栈操作
#     if self.stacksmpty():
#         print('栈为空，不能出栈')
#         return None
#     else:
#         self.top-=self.top
#         x=self.stack[self.top]
#         return x
# def stacklength(self):     # 返回栈的长度
#     return self.top
# def clearstack(self):      # 清空栈
#     self.top=0

# ---------------------------------

# # 链栈
# # 设栈顶指针为top，初始化的时候，对于不带头节点的链栈，top=None,
# # 对于带头节点的链栈，top.next=None
#
# # 链栈结点的描述
# class linkstacknode:
#     def __init__(self):
#         self.data=None
#         self.next=None
#
# # 链栈的初始化
# class mylinkstack():
#     def __init__(self):
#         self.top = linkstacknode()   # new了一个节点对象，作为哨兵
#
# # 看到 self.top = None → 不带头结点
# # 看到 self.top = LinkStackNode() → 带头结点
#
# # 判断链栈是否为空
# def stackempty(self):
#     if self.top.next is None:
#         return True
#     else:
#         return False
#
# # 入栈操作
# def pushstack(self,e):
#     p=linkstacknode()
#     p.data=e
#     p.next=self.top.next
#     self.top.next=p
#
# # 出栈操作
# def popstack(self):
#     if self.stackempty():
#         print('栈为空，不能进行出栈操作')
#         return None
#     else:
#         p=self.top.next.data   # 头结点的下一个数据（即所要出栈的第一个数据）赋予给p
#         self.top.next=self.top.next.next  # 头结点则指向头结点的下下个
#         return p   # 返回p
#
# # 取栈顶元素
# def gettop(self):
#     if self.stacksmpty():
#         print('栈为空，取栈顶元素失败')
#         return None
#     else:
#         return self.top.next.data
#
# # 求表长操作
# def stacklength(self):
#     if self.stacksmpty():  # 可删  因为 p = self.top.next 如果是 None，
#         return 0           # 可删  while 根本不会执行，len 自然为 0，最后返回 0
#     p=self.top.next
#     len=0
#     while p is not None:
#         p=p.next
#         len+=1
#     return len
#
# # 销毁链栈
# def clearstack(self):
#     while self.top is not None:
#         p=self.top
#         self.top=self.top.next
#         del p
#
# # 创建链栈，将元素一次入栈
# def craetstack(self):
#     print('请输入要入栈的整数（用空格分开）：')
#     eElem=list(map(int,input().split()))
#     for e in eElem:
#         pnode=linkstacknode()
#         pnode.data=e
#         pnode.next=self.top.next
#         self.top.next=pnode

# -------------------------------

# 递归
# 指在函数的定义中，定义自己的同时又出现对自身的调用。
# 如果一个函数在函数体直接调用自己，称为直接递归函数。
# 如果经过一系列的中间调用，间接调用自己的函数称为间接递归调用。
'''正常可以直接用迭代，通过循环结构就可以消除递归'''
# def fact9(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
'''递归算法实现'''
# def ack(m,n):
#     if m==0:
#         return n+1
#     elif n==0:
#         return ack(m-1,1)
#     else:
#         return ack(m-1,ack(m,n-1))
'''递归就是有记录的迭代'''

# ----------------------------------

# 队列
'''队列也是一种限定性线性表，允许在表的一端进行插入操作，在表的另一端进行删除操作'''
# 顺序队列的实现
# class sqe(object):
#     def __init__(self):
#         self.maxsize=20
#         self.s=[None for x in range(0,self.maxsize)]
#         self.front=0
#         self.rear=0
#     # 顺序循环队列的实现
# class Link:
#     def __init__(self):
#         self.maxsize=20
#         self.s = [None for x in range(0, self.maxsize)]
#         self.front = 0
#         self.rear = 0
#     def isempty(self):
#         if self.front==self.rear:
#             return True
#         else:
#             return False
#     def enqueue(self,x):
#         if (self.rear+1)%self.maxsize!=self.front:
#             self.s[self.rear]=x
#             self.rear=(self.rear+1)%self.maxsize
#             # (self.rear+1)%self.maxsize的值就是原本self.rear的下一个下标
#             # 即尾指针移动一个位置
#             return True
#         else:
#             print("当前队列已满")
#             return False
#     def dequeue(self):
#         if self.front==self.rear:
#             print("队列为空，出队操作失败")
#             return False
#         else:
#             e=self.s[self.front]
#             self.front=(self.front+1)%self.maxsize # 头指针往后移一个
#             return e
#     # 取头元素
#     def gethead(self):
#         if not self.isempty():
#             return self.s[self.front]
#         else:
#             print("队列为空")
#             return None
#     def length(self):
#         return (self.rear-self.front+self.maxsize)%self.maxsize
#     # +self.maxsize作为安全垫以防self.rear-self.front有负数的情况
#     # 创建队列
#     def creatsequeue(self):
#         data=input("请输入元素（#作为输入结束）：")
#         while (data!='#'):
#             self.enqueue(data)
#             data=input("请输入元素（#作为输入结束）:")
#     # 另一种写法：
#     def creatsequeue(self):
#         while True:   # 无限循环，全靠 break 跳出
#             data = input("请输入元素（#作为输入结束）：")
#             if data == '#':
#                 break   # 遇到 #，直接跳出循环
#             self.enqueue(data)

# 链式循环队列
# class queuenode:
#     def __init__(self):
#         self.data=None
#         self.next=None
# class LinkQueue:
#     def __init__(self):
#         myqueue=queuenode()  # 头结点
#         self.front=myqueue
#         self.rear=myqueue
#     def isempty(self):
#         if self.front==self.rear:
#             return True
#         else:
#             return False
#     def enqueue(self,x):
#         pnode=queuenode()
#         pnode.data=x
#         self.rear.next=pnode
#         self.rear=pnode
#     def dequeue(self):
#         if self.isempty():
#             print("队列为空，不能出队操作")
#             return None
#         else:
#             pnode=self.front.next
#             self.front.next=pnode.next
#             if pnode==self.rear:
#                 self.rear=self.front
#             return pnode.data
#     def gethead(self):
#         if not self.isempty():
#             return self.front.next.data
#     def clearqueue(self):
#         pnode=self.front.next
#         while pnode is not None:
#             e=pnode.next
#             del pnode
#             pnode=e
#         self.front.next = None
#         self.rear=self.front

# --------------------------------------

# 串 数据为字符串的线性结构
# 顺序存储方式  Brute-Force匹配算法
# def B_FIndex(self,pos,T):
#     # 在主串的pos位置开始查找串T
#     i=pos-1
#     j=0
#     while i<self.lengeth and j<T.length:
#         if self.str[i]==T.str[j]:
#             i+=1
#             j+=1
#         else:
#             i=i-j+1
#             j=0
#     if j>=T.length:
#         return i-j+1,count
#     else:
#         return -1
#
# # KMP算法
# def KMP_Index(self,pos,T,next):
#     i=pos-1
#     j=0
#     while i<S.length and j<T.length:
#         if j==-1 or self.str[i]==T.str[j]:
#             i+=1
#             j+=1
#         else:
#             j=next[j]
#     if j>=T.length:
#         return i-T.length+1,count
#     else:
#         return -1
#
# # 求next函数值的算法描述如下
# def GetNext(self,pos,T):
#     j=0
#     k=-1
#     next=[None for i in range(T.length)]
#     next[0]=-1
#     while j<T.length:
#             if k==-1 or T.str[j]==T.str[k]:
#                 j+=1
#                 k+=1
#                 next[j]=k
#             else:
#                 k=next[k]
#     return next

# ------------------------------------------------

# 数组
# n=10
# a=[None]*n
# m,n=10,20
# a=[[None]*n for i in range(m)]
# print(a)
#
# 广义表
#
# class GListNode:
#     def __init__(self,tag=None,ptr=None,tp=None):
#         self.tag=tag
#         self.ptr=ptr
#         self.tp=tp
#     #     求广义表的长度
#     def getGListNodeLength(self,GLNode):
#         if GLNode.tp is None or GLNode.tp.ptr is None:
#             return 0
#         count=0
#         node=GLNode.tp
#         while node:
#             count+=1
#             node=node.tp
#         return count
#     #     求广义表的深度
#     def getGListNodeDepth(self,GLNode):
#         depth=-1
#         while GLNode:
#             if GLNode.tag==1:     # 如果是子表就递归遍历
#                 count=self.getGListNodeDepth(GLNode.ptr)
#                 if count>depth:
#                     depth=count
#             GLNode=GLNode.tp      # 遍历下一个元素
#         return depth+1

# -----------------------------------------

# 排序
# class SqList:
#     def __init__(self,length=0):
#         self.data=[]
#         self.length=length
#
#
#     def InsertSort(self):
#         # 直接插入排序
#         for i in range(self.length-1):
#             t=self.data[i+1]
#             j=i
#             while j>-1 and t<self.data[j]:
#                 self.data[j+1]=self.data[j]
#                 j-=1
#             self.data[j+1]=t
#
#     def BinInsertsort(self):
#         # 折半插入排序
#         for i in range(self.length-1):
#             t=self.data[i+1]
#             low,high=0,i
#             while low<=high:
#                 mid=(low+high)//2
#                 if self.data[mid]>t:
#                     high=mid-1
#                 else:
#                     low=mid-1
#             for j in range(i,low-1,-1):
#                 self.data[j+1]=self.data[j]
#             self.data[low]=t
#
#     def Bubblesort(self):
#         # 冒泡排序
#         flag=True
#         for i in range(self.length-1):
#             if flag==True:
#                 flag=False
#                 for j in range(self.length-1-i):
#                     if self.data[j]>self.data[j+1]:
#                         t=self.data[j]
#                         self.data[j]=self.data[j+1]
#                         self.data[j+1]=t
#                         flag=True
#
#     def Partition(self,low,high):
#         # 快速排序-分区
#         pivotkey=self.data[low]
#         t=self.data[low]
#         while low<high:
#             while low<high and self.data[high]>=pivotkey:
#                 high-=1
#             if low<high:
#                 self.data[low]=self.data[high]
#                 low+=1
#             while low<high and self.data[high]<=pivotkey:
#                 low+=1
#             if low<high:
#                 self.data[high]=self.data[low]
#                 high-=1
#             self.data[low]=t
#         return low
#     def QuickSort(self,low,high):
#         # 快速排序算法-多次递归调用
#         if low<high:
#             pivot=self.Partition(low,high)
#             self.QuickSort(low,pivot-1)
#             self.QuickSort(pivot+1,high)
#
#     def SelectSort(self):
#         # 简单选择排序
#         for i in range(self.length-1):
#             j=i
#             for k in range(i+1,self.length):
#                 if self.data[k]<self.data[j]:
#                     j=k
#             if j!=i:
#                 t=self.data[i]
#                 self.data[i]=self.data[j]
#                 self.data[j]=t

# ------------------------------------------

# 树与二叉树
# 二叉链表存储结构的类型定义表述
# class BiTreeNode():
#     def __init__(self,data,lchild=None,rchild=None):
#         self.data=data
#         self.lchild=lchild
#         self.rchild=rchild
# # 二叉树的定义及初始化
# class BiTree(object):
#     def __init__(self):
#         self.root=BiTreeNode(None)
#         self.num=0
# # 创建二叉树的算法实现
#     def CreatBiTree(self,vals):
#         if len(vals) == 0:
#             return None
#         if vals[0] != '#':
#             node = BiTreeNode(vals[0])
#             if self.num == 0:
#                 self.root = node
#             self.num += 1
#             vals.pop(0)
#             node.lchild = self.CreatBiTree(vals)
#             node.rchild = self.CreatBiTree(vals)
#             return node
#         else:
#             vals.pop(0)
#             return None
# # 使用完二叉树之后需要将二叉树销毁
#     def DestroyBiTree(self,T):
#         if T:
#             if T.lchild:
#                 self.DestroyBiTree(T.lchild)
#             if T.rchild:
#                 self.DestroyBiTree(T.rchild)
#             del T
#             T=None
#         return T
# # 二叉树的先序递归算法
#     def PreOrderTraverse(self,T):
#         if T:
#             print(T.data,end='')
#             # 先访问根节点，再先后访问左子树右子树
#             self.PreOrderTraverse(T.lchild)
#             self.PreOrderTraverse(T.rchild)
# # 二叉树的非递归算法
#     def PreOderTraver2(self,T):
#         stack=[]
#         top=0
#         p=T
#         while p != None or top>0:
#             while p !=None:    # 如果p不空，访问根节点，遍历左子树
#                 print('%2c'%p.data,end='')
#                 stack.append(p)
#                 top+=1
#                 p=p.lchild
#             if top>0:
#                 p=stack.pop(-1)
#                 top-=1
#                 p=p.rchild
#     # 二叉树的中序遍历
#     def InOderTraverse(self,T):
#         # 中序二叉树的递归实现
#         if T:
#             self.InOderTraverse(T.lchild)
#             print(T.data,end='')
#             self.InOderTraverse(T.rchild)
#     def InOderTraverse2(self,T):
#         # 中序遍历二叉树的非递归实现
#         stack=[]
#         top=0
#         p=T
#         while p != None or top >0:
#             while p !=None:
#                 stack.append(p)
#                 top+=1
#                 p=p.lchild
#             if top>0:
#                 p=stack.pop(-1)
#                 top-=1
#                 print('%2c'%p.data,end='')
#                 p=p.rchild
#     def PostOderTaverse(self,T):
#         # 后序遍历二叉树的递归实现
#         if T:
#             self.PostOderTaverse(T.lchild)
#             self.PostOderTaverse(T.rchild)
#             print('%2c'%T.data)
#     def PostOderTraverse2(self,T):
#         # 后序遍历二叉树的非递归实现
#         stack=[]
#         p=T
#         q=None
#         while p != None or len(stack)>0:
#             while p != None:
#                 stack.append(p)
#                 p=p.lchild
#             if len(stack)>0:
#                 p=stack[-1]
#                 if p.rchild==None or p.rchild==q:
#                     print('%2c'%(p.data),end='')
#                     q=p
#                     p=None
#                     stack.pop()
#                 else:
#                     p=p.rchild
#     def LevelTraverse(self,T):
#         # 二叉树的层次遍历
#         if T is None:
#             return
#         queue=[]
#         queue.append(T)
#         while queue:
#             p=queue.pop(0)
#             print('%2c'%p.data,end='')
#             if p.lchild:
#                 queue.append(p.lchild)
#             if p.rchild:
#                 queue.append(p.rchild)
# # 二叉树的线索化
# class BiThrNode():
#     # 线索二叉树的存储结构
#     def __init__(self,data,lchild=None,rchild=None,ltag=None,rtag=None):
#         self.data=data
#         self.lchild=lchild
#         self.rchild=rchild
#         # 线索标志域
#         self.ltag=ltag
#         self.rtag=rtag
#     def InOderPre(self,p):
#         # 查找指定节点的中序直接前驱
#         if p.ltag==1:
#             return p.lchild
#         else:
#             pre=p.lchild
#             while pre.rtag==0: # 右子树非空时，沿右链往下查找
#                 pre=pre.rchild
#             return pre
#     def InOderPost(self,p):
#         # 查找指定节点的中序直接后继
#         if p.rtag==1:
#             return p.rchild
#         else:
#             pre=p.rchild
#             while pre.ltag==0:
#                 pre=pre.lchild
#             return pre
#     def InOderTraverse(self,T,visit):
#         # 中序遍历线索二叉树。其中visit是函数指针，指向访问节点的函数实现
#         p=T.lchild
#         while p!=T:   # 空树或遍历结束的时候，p==T
#             while p!=None and p.ltag==0:
#                 p=p.lchild
#             if visit(p)!=1:  # 打印
#                 return 0
#             while p.rtag==1 and p.rchild!=T:
#                 p=p.rchild
#                 visit(p)
#             p=p.rchild
#         return 1

# 树的双亲表示法存储结构的描述
# class PNode:
#     # 双亲表示法的结点定义
#     def __init__(self,data=None,parent=None):
#         self.data=data
#         self.parent=parent
# class PTree:
#     # 双亲表示法的类型定义
#     def __init__(self):
#         self.node=[]
#         self.num=0   # 结点的个数
# # 树的孩子表示法的类型描述
# class ChildNode:  # 孩子结点的类型
#     def __init__(self,child=None,next=None):
#         self.child=child
#         self.next=next
# class DataNode:  # n个数据结构与孩子链表的指针构成一个结构
#     def __init__(self,data=None):
#         self.data=data
#         self.firstchild=ChildNode()
# class CTree:  # 孩子表示法的类型定义
#     def __init__(self,num=0,root=None):
#         self.node=[]
#         self.num=num
#         self.root=root
# # 树的孩子兄弟法的描述类型
# class CSNode:  # 兄弟表示法的类型定义
#     def __init__(self,firstchild=None,nextsibling=None,data=None):
#         self.data=data
#         self.firstchild=firstchild
#         self.nestsibling=nextsibling
# class DisjiintSet:
#     # 初始时，每一个元素代表一棵树。假设有n个编号分别为1,2..n的元素，
#     # 使用列表parent存储每个元素的父结点，初始时现将父结点设为自身。
#     def __init__(self,n=100):
#         self.MAXSIZE=100
#         self.parent=[0]*self.MAXSIZE
#         self.rank=[0]*self.MAXSIZE
#         for i in range(1,n+1):
#             self.parent[i]=i
#     def Find(self,x):
#         # 查找
#         if self.parent[x]==x:
#             return x
#         else:
#             return self.Find(self.parent[x])
#     def Find(self,x):
#         # 带路径压缩的查找算法
#         if self.parent[x]==x:
#             return x
#         else:
#             self.parent[x]=self.Find(self.parent[x])
#             return self.parent[x]
#     def Find_NonRec(self,x):
#         root=x
#         while self.parent[root]!=root:
#             root=self.parent[root]
#         y=x
#         while y!=root:
#             y_next=self.parent[y]
#             self.parent[y]=root
#             y=y_next
#         return root
#     # 合并算法
#     def Mergr(self,x,y):
#         root_x,root_y=self.Find(x),self.Find(y)
#         if self.rank[root_x]<=self.rank[root_y]:
#             self.parent[root_x]=root_y
#         else:
#             self.parent[root_y]=root_x
#         if self.rank[root_x]==self.rank[root_y] and root_x!=root_y:
#             self.rank[root_y]+=1
# 顺序表存储顺序描述
# class SSTable:
#     def __init__(self):
#         self.list=[]
#         self.length=0
# # 顺序表的查找算法描述
#     def SeqSearch(self,x):
#         i=0
#         while i<self.length and self.list[i]!=x:
#             i+=1
#         if i>=self.length:
#             return 0
#         elif self.list[i]==x:
#             return i+1  # 下标加一为其位置
#     def SeqSearch2(self,x,):
#         # 也可以通过设置监视哨的方法实现
#         i=self.length
#         self.list[0]=x
#         while self.list[i]!=x:
#             i-=1
#         return i
# # 顺序查找
#     def SeqSearch3(self,x,):
#         i=self.length
#         self.list[0]=x
#         while self.list[i]!=x:
#             i-=1
#         if self.list[i]==x:
#             return i
#         else:
#             return 0
# # 折半查找
#     def BinarySearch(self,x):
#         # 在有序顺序表中折半查找关键字为x的元素，如果找到，返回该元素在表中位置，否则返回0
#         # 设置待查找元素范围的下界和上界
#         low=0
#         high=self.length-1
#         while low<=high:
#             mid=(low+high)//2  # 整除并向下取整
#             if self.list[mid]==x:
#                 return mid+1
#             elif self.list[mid]>x:
#                 high=mid-1
#             elif self.list[mid]<x:
#                 low=mid+1
#         return 0
# # 二叉树的链式存储结构，二叉树的类型定义如下
# class BiTreeNode:
#     def __init__(self,data,lchild=None,rchild=None):
#         self.data=data
#         self.lchild=lchild
#         self.rchild=rchild
# # 二叉排序树的查找算法描述如下
#     def BSTSearch(self,x):
#         T=self.root
#         if T!=None:   # 如果二叉树不为空
#             p=T
#         while p!=None:
#             if p.data==x:
#                 return p
#             elif x<p.data:
#                 p=p.lchild
#             else:
#                 p=p.rchild
#         return None
# # 二叉排序树的插入操作
#     def BSTInsert(self,x):
#         if self.root is None:
#             self.root=BiTreeNode(x)
#             return
#         parent=self.root
#         while True:
#             e=parent.data
#             if x<e:
#                 if parent.lchild==None:
#                     parent.lchild=BiTreeNode(x)
#                 else:
#                     parent=parent.lchild
#             elif x>e:
#                 if parent.rchild==None:
#                     parent.rchild=BiTreeNode(x)
#                 else:
#                     parent=parent.rchild
#             else:
#                 return
# # 二叉排序树的删除操作算法描述
#     def BSTdelete2(self,x):
#         # 在二叉排序树T中存在值为x的数据元素时，删除高该数据元素节点，并返回1，否则返回0
#         p,s=None,self.root
#         if not s:
#             print("二叉树为空，不能进行删除操作")
#             return 0
#         else:
#             while s:
#                 if s.data!=x:
#                     p=s
#                 else:
#                     break   # 找到值为x的数据元素，此时s为要删除的数据结点
#                 if x<s.data:
#                     s=s.lchild
#                 else:
#                     s=s.rchild
#         # 删除结点，并使二叉排序树的性质不变
#         if not s.lchild:
#             if p is None:
#                 self.root=s.rchild
#             elif s==p.lchild:
#                 p.lchild=s.rchild
#             else:
#                 p.rchild=s.rchild
#             return
#         if not s.rchild:
#             if p is None:
#                 self.root=s.lchild
#             elif s==p.lchild:
#                 p.lchild=s.lchild
#             else:
#                 p.rchild=s.lchild
#             return
#         x_node=s
#         y_node=s.lchild
#         while y_node.rchild:
#             x_node=y_node
#             y_node=y_node.rchild
#         s.data=y_node.data
#         if x_node!=s:
#             x_node.rchild=y_node.lchild
#         else:
#             x_node.lchild=y_node.lchild
#
# # ---------------------------------------
#
# # 哈希表的操作
# class HashData:     # 元素类型定义
#     def __init__(self,hi=0,key=None):
#         self.hi=hi
#         self.key=key
# class HashTable:    # 哈希表类型定义
#     def __init__(self,tableSize=0,curSize=0):
#         self.data=[]
#         self.tableSize=tableSize
#         self.curSize=curSize
#     def CreateHashTable(self,m,p,hash,n):
#         # 构造一个空的哈希表，并处理冲突
#         k=1
#         for i in range(m):
#             hd=HashData(0,-1)
#             self.data.append(hd)
#             for i in range(n):
#                 sum=0
#                 addr=hash[i]%p
#                 di=addr
#                 if self.data[addr].key==-1:
#                     self.data[addr].key=hash[i]
#                     self.data[addr].hi=1
#                 else:
#                     while self.data[di].key!=hash[i]:
#                         di=(di+k)%m
#                         sum+=1
#                         self.data[di].key=hash[i]
#                         self.data[di].hi=sum+1
#         self.curSize=n
#         self.tableSize=m
#     def SearchHash(self,k):   # 在哈希表H中查找关键字k的元素
#         m=self.tableSize
#         d=k%m
#         d1=k%m
#         while self.data[d].key!=-1:
#             if self.data[d].key==k:
#                 return d
#             else:
#                 d=(d+1)%m
#             if d==d1:
#                 return 0
#         return 0
#     def HashASL(self,m):     # 求哈希表的平均查找长度
#         average=0
#         for i in range(m):
#             average+=self.data[i].hi
#             average=average/self.curSize
#             print("平均查找长度ASL=%。2f"%average)

# -----------------------------

# 图
# 图的邻接矩阵存储结构描述-----------------
# class MGraph:
#     def __init__(self):
#         self.vex=[]     # 存储顶点 'A','B'...
#         self.arc=[]     # 邻接矩阵，存储边/弧的信息 矩阵
#         self.vexnum=0   # 顶点数
#         self.arcnum=0   # 边/弧的数目
#         self.kind=None  # 图的类型
#
# # 图的邻接表存储结构描述------------------
# class GKind:     # 图的类型：有向图，无向图，有向网，无向网
#     DG=1
#     DN=2
#     UG=3
#     UN=4
#
# class ArcNone:   # 边结点的类型定义
#     def __init__(self,adjvex):
#         self.adjvex=adjvex  # 弧指向的顶点的位置
#         self.nextarc=None   # 指示下一个与该顶点相邻接的顶点
#         self.info=None      # 与弧相关的信息
#
# class VNode:                # 头结点的类型定义
#     def __init__(self,data):
#         self.data=data      # 存储顶点
#         self.firstarc=None  # 指向第一个与该顶点相邻接的顶点
#
# class AdjGraph:             # 图的类型定义
#     def __init__(self):
#         self.vertex=[]
#         self.vexnum=0       # 图的顶点数目
#         self.arcnum=0       # 弧的数目
#         self.kind=GKind.UG  # 图的类型
#
# # 有向图的十字链表存储结构描述------------------
# # 无向图的邻接多重表存储结构描述------------------
#
# # 图的深度优先遍历（邻接表）的算法描述
#     def DFTraverse(self,visited):
#         self.visited=visited
#         for v in range(self.vexnum):
#             visited.append(0)   # 访问标志列表初始化为未被访问
#         for v in range(self.vexnum):
#             if visited[v]==0:
#                 self.DFS(v)
#         print()
#     def DFS(self,v):
#         self.visited[v]=1
#         print(self.vertex[v].data,end='')
#         w=self.FirstAdjVertex(self.vertex[v].data)
#         while w>=0:
#             if self.visited[w]==0:
#                 self.DFS(w)     # 递归
#             w=self.NextAdjVertex(self.vertex[v].data,self.vertex[w].data)
#     def FirstAdjVertex(self,v):
#         # 返回顶点v的第一个邻接顶点的序号
#         v1=self.LocateVertex(v)
#         p=self.vertex[v1].firstarc
#         if p!=None:
#             return p.adjvex
#         else:
#             return -1
#     def NextAdjVertex(self,v,w):
#         # 返回v的相对于w的下一个邻接顶点的序号
#         v1=self.LocateVertex(v)
#         w1=self.LocateVertex(w)
#         next=self.vertex[v1].firstarc
#         while next!=None:
#             if next.adjvex!=w1:
#                 next=next.nextrac
#             else:
#                 break
#         p=next
#         if p==None or p.nextrac==None:
#             return -1
#         else:
#             return p.nextrac.adjvex
# # 图的广度优先遍历的算法实现
#     def BFSTraverse(self):
#         MaxSize=20
#         visited=[]
#         queue=[]
#         front=-1
#         rear=-1
#         for v in range(self.vexnum):
#             visited.append(0)
#         v=0
#         visited[v]=1
#         print(self.vertex[v].data,end='')
#         rear=(rear+1)%MaxSize
#         queue.append(v)
#         while front<rear:
#             front=(front+1)%MaxSize
#             v=queue.pop(0)
#             p=self.vertex[v].firstarc
#             while p!=None:
#                 if visited[p.adjvex]==0:
#                     visited[p.adjvex]=1
#                     print(self.vertex[p.adjvex].data,end='')
#                     rear=(rear+1)%MaxSize
#                     queue.append(p.adjvex)
#                 p=p.nextrac













