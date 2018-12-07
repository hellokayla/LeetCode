class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        # create initial temp node 
        
        temp = ListNode(0)
        head = temp
        carry = 0
        
        while l1 or l2 or carry:
            
            ## add numbers together
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            
            tempSum = temp1 + temp2 + carry
            
            # create next value
            # get remainder, place down remainder
            temp.next = ListNode(tempSum % 10)
            temp = temp.next
            
            # get carry
            # carry is either 1 or 0
            carry = tempSum // 10
            
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
            
        return head.next
        
        
