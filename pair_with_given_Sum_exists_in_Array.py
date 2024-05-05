def pairSum(arr, S):
    sum_inverse = [i - S for i in arr]
    for i in sum_inverse:
        return 'Yes'
        
pairSum([0,-1,2,-3,1],-2)
