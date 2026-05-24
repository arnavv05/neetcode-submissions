class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult, r_mult = 1,1
        n = len(nums)
        l_arr, r_arr = [0]*n, [0]*n
        for i in range(n):
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l_arr[x]*r_arr[x] for x in range(len(l_arr))]