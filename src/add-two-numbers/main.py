# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.next = None



class Solution(object):

    def addTwoNumbers(self, l1, l2):

        """

        :type l1: ListNode

        :type l2: ListNode

        :rtype: ListNode

        """
        result = []
        len_one = len(l1)
        len_two = len(l2)
        index_one = 0
        index_two = 0
        up_value = 0
        while True:
            if index_one >=  len_one or index_two > len_two:
                break
            sum_value = l1[index_one] + l2[index_two]
            value = (sum_value + up_value)  % 10
            up_value = sum_value - value 
            if up_value > 0:
                up_value = 1
            else:
                up_value = 0
            result.append( value )
            index_one += 1
            index_two += 1
        while index_one < len_one:
            sum_value = l1[index_one]
            value = (sum_value + up_value)  % 10
            up_value = sum_value - value
            if up_value > 0:
                up_value = 1
            else:
                up_value = 0
            result.append( value )
            index_one += 1
        while index_two < len_two:
            sum_value = l2[index_two]
            value = (sum_value + up_value)  % 10
            up_value = sum_value - value
            if up_value > 0:
                up_value = 1
            else:
                up_value = 0
            result.append( value )
            index_two += 1
        if up_value > 0:
            result.append( 1 )         
        return result
                    

if __name__ == "__main__":
    a = [2,4,3]
    b = [5,6,4]
    obj = Solution()
    print obj.addTwoNumbers(a,b)
