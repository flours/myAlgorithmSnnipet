def binarySearch(X,target,left,right):
  while True:
    mid=(left+right)//2
    if X[left]>=target:return left
    if X[right]<=target:return right
    if X[mid]==target:return mid
    if left==right:
      return X[left]
    if X[mid]>target:
      right=mid-1
    else:
      left=mid
      right=right-1

if __name__=='__main__':
  arr=[101,102,103,104,105,106]
  print("102のインデックスは",binarySearch(arr,102,0,len(arr)-1))
  arr=[101,102,103,104,106,107]
  print("105を超えない最大のインデックスは",binarySearch(arr,105,0,len(arr)-1))

  print("10を超えない最大のインデックスはないので0が帰ります",binarySearch(arr,10,0,len(arr)-1))  
  print("つまり最小より値が小さい場合は0,それ以外の場合はその値以下の最大の値を探索します。")