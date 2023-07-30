def rotate(nums,k):
    def rev(s, e):
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

    l = len(nums)
    k = k % l

    rev(0, l - k - 1)
    rev(l - k, l - 1)
    rev(0, l - 1)
    return nums

nums=[1,2,3,4,5,6,7,8]
k=3
print(rotate(nums,k))