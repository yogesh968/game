class Solution:
    def reversePairs(self, nums):
        def merge_sort(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            cnt = merge_sort(l, m) + merge_sort(m + 1, r)
            j = m + 1
            for i in range(l, m + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (m + 1)
            temp = []
            i, j = l, m + 1
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= m:
                temp.append(nums[i])
                i += 1
            while j <= r:
                temp.append(nums[j])
                j += 1
            nums[l:r+1] = temp
            return cnt

        return merge_sort(0, len(nums) - 1)
