n = [3,2,4]
target = 6
def twoSum(n,target):
    i=0
    dic={}
    while i <= len(n)-1:
        dic.update({i:target - n[i]})
        if (dic[i] in n) and i != n.index(dic[i]):
            print(dic[i], i , n.index(dic[i]) )
            return print([i,n.index(dic[i])])
        i=i+1
twoSum(n,target)