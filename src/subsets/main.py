#!/usr/bin/python
#-*-coding:utf-8-*-
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_list = len(nums)
        whole_number = 1 << len_list
        my_dict = {}
        for index in xrange(len_list):
            my_dict[index] = 1 << index
        #for e in my_dict:
        #    print e, my_dict[e]    
        result = []
        for value in xrange( whole_number):
            tmp_result = []
            for index in my_dict:
                if value & my_dict[index]:
                    tmp_result.append( nums[index] )
            result.append( tmp_result)
        return result

if __name__ == "__main__":
    obj = Solution()
    print obj.subsets( [1,2,3])
    
