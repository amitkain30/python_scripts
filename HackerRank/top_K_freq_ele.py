# Input: nums = [1,2,2,3,3,3], k=2
# Output: [2,3]

class Solution:
    def topKFrequent(self, nums: list[int], k:int)->list[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        print(count)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])

        return res


if __name__ =="__main__":
    nums = [1,2,2,3,3,3]
    k=2

    res = Solution()

    print(res.topKFrequent(nums, k))
    print(res.topKFrequent([7,7], 1))

