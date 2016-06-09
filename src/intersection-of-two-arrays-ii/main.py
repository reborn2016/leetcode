class Solution(object):

    def intersect(self, nums1, nums2):

        """

        :type nums1: List[int]

        :type nums2: List[int]

        :rtype: List[int]

        """
        nums1.sort()
        nums2.sort()
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        result = []
        index_one = 0
        index_two = 0
        while index_one  < len_nums1 and index_two < len_nums2:
            value_1 = nums1[index_one]
            value_2 = nums2[index_two]
            if value_1 == value_2 :
                result.append( value_1 )
                index_one += 1
                index_two += 1
                continue
            if value_1 > value_2:
                index_two += 1
            if value_1 < value_2:
                index_one += 1
        
        return result

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print solution.intersect(nums1, nums2)
                
