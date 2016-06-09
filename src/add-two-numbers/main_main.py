# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next =None

#         self.val = x

#         self.next = None



class Solution(object):

    def addTwoNumbers(self, l1, l2):

        """

        :type l1: ListNode

        :type l2: ListNode

        :rtype: ListNode

        """
        result = ListNode(-1)
        result_head = result
        up_value = 0
        while True:
            if l1 == None or l2 == None:
                break
            value = l1.val + l2.val + up_value
            new_value = value - 10
            if new_value >= 0:
                up_value = 1
                value = new_value
            else:
                up_value = 0
            result.next = ListNode(-1)
            result = result.next
            result.val = value
            l1 = l1.next
            l2 = l2.next
            
        while l1 <> None:
            value = l1.val + up_value
            new_value = value - 10
            if new_value >= 0:
                up_value = 1
                value = new_value
            else:
                up_value = 0
            result.next = ListNode(-1)
            result = result.next
            result.val = value
            l1 = l1.next
            


        while l2 <> None:
            value = l2.val + up_value
            new_value = value - 10
            if new_value >= 0:
                up_value = 1
                value = new_value
            else:
                up_value = 0
            result.next = ListNode(-1)
            result = result.next
            result.val = value
            l2 = l2.next

        if up_value > 0:
            result.next = ListNode(-1)
            result = result.next
            result.val = up_value
            result.next = None

        return result_head.next
                    
def constructNodes(a):
    result = ListNode(-1)
    result_head = result
    for e in a:
        result.next = ListNode(e)
        result = result.next
    return result_head.next
if __name__ == "__main__":
    a = [2,4,3]
    b = [5,6,4]
    obj = Solution()
    result = obj.addTwoNumbers(constructNodes(a),constructNodes(b))
    while result <> None:
        print result.val
        result = result.next
    
