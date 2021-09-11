def binarySearch(X, target, left, right):
    while True:
        mid = (left + right) // 2
        if X[left] > target:
            return left
        if X[right] <= target:
            return right
        if left == right:
            return left
        if X[mid] > target:
            right = mid - 1
        else:
            left = mid
            right = right - 1

class stdMultiSet:
    def __init__(self, valueList):
        self.size = 1<<len(set(valueList)).bit_length()
        self.tree = [0] * (self.size + 1)
        self.valueSet=set(valueList)
        self.sortedValueList=sorted(list(set(valueList)))
        self.value2Idx={v:i+1 for i,v in enumerate(sorted(list(set(valueList))))}
        self.idx2Value={i+1:v for i,v in enumerate(sorted(list(set(valueList))))}

    # i番目の値を検索
    def __getitem__(self,key):
        if key>self.__len__() or key<=0:
            print("index out of range",key)
        value=0
        idx=2**(len(bin(self.size))-3)
        width=idx//2
        while width:
            if key<=value+self.tree[idx]:
                idx=idx-width
            else:
                value+=self.tree[idx]
                idx=idx+width
            width//=2
        if key<=value+self.tree[idx]:
            return self.idx2Value[idx]
        else:
            return self.idx2Value[idx+1]

    def __len__(self):
        return self.__sum(self.size)

    def __sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def upper_bound(self,i):
        return lower_bound(i+1)
    def lower_bound(self,i):
        idx=min(binarySearch(self.sortedValueList,i,0,len(self.sortedValueList)-1)+1,self.size)
        value = self.__sum(idx)
        return value+1


    # iを削除
    def remove(self,i):
        return self.__add(self.value2Idx2[i],-1)

    # iを追加
    def add(self,i):
        return self.__add(self.value2Idx[i],1)

    def __add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

L,Q=map(int,input().split())
l=[0,L]
queries=[]
for i in range(Q):
    c,x=map(int,input().split())
    if c==1:
        l+=x,
    queries+=(c,x),

multiSet = stdMultiSet(l)     #試用する可能性のある数値を入れて初期化
multiSet.add(0)
multiSet.add(L)

for c,x in queries:
    if c==1:
        multiSet.add(x)
    else:
        idx=multiSet.lower_bound(x)
        print(multiSet[idx]-multiSet[idx-1])