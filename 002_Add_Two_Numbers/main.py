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
        step = 0
        head = ListNode(0)
        if (l1.val+l2.val > 9):
            head.val = l1.val + l2.val - 10
            step = 1
        else:
            head.val = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
            
        cursor = head
        while (l1 != None and l2 != None):
            cursor.next = ListNode(0)
            cursor = cursor.next
            if (step == 1):
                cursor.val += 1
                step = 0
            nodeSum = l1.val + l2.val
            cursor.val += nodeSum
            if ( cursor.val > 9):
                step = 1
                cursor.val -= 10
            l1 = l1.next
            l2 = l2.next
        
        if (l1 == None):
            if (l2 == None):
                if (step == 1):
                    cursor.next = ListNode(0)
                    cursor = cursor.next                   
                    cursor.val += 1
                    step = 0
            else:
                while (step == 1 and l2 != None):
                    cursor.next = ListNode(0)
                    cursor = cursor.next    
                    cursor.val = l2.val
                    if (step == 1):
                        cursor.val += 1
                        if (cursor.val > 9):
                            cursor.val = 0
                            step = 1
                        else:
                            step = 0
                    l2 = l2.next

                if (step == 1):
                    cursor.next = ListNode(0)
                    cursor = cursor.next                   
                    cursor.val += 1
                    step = 0
                else:
                    cursor.next = l2
                    
        elif (l2 == None):
            if (l1 == None):
                if (step == 1):
                    cursor.next = ListNode(0)
                    cursor = cursor.next                   
                    cursor.val += 1
                    step = 0
            else:
                while (step == 1 and l1 != None):
                    cursor.next = ListNode(0)
                    cursor = cursor.next    
                    cursor.val = l1.val
                    if (step == 1):
                        cursor.val += 1
                        if (cursor.val > 9):
                            cursor.val = 0
                            step = 1
                        else:
                            step = 0
                    l1 = l1.next

                if (step == 1):
                    cursor.next = ListNode(0)
                    cursor = cursor.next                   
                    cursor.val += 1
                    step = 0
                else:
                    cursor.next = l1
        
        return head
