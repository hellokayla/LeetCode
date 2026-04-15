class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
       self.map = [ListNode() for i in range(1000)] 
        
    def put(self, key: int, value: int) -> None:
        # inserting key for the first time
        index = key % len(self.map)
        curr_node = self.map[index] # dummy head node
        # have to use curr_node.next otherwise loop ends on curr_node = None
        # can't curr_node.next if curr_node is None
        # stay 
        while curr_node.next: # first real node
            if curr_node.next.key == key: # update
                curr_node.next.value = value
                return
            curr_node = curr_node.next
        # curr_node = actual node, curr_node.next = None
        # now we insert.
        curr_node.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        index = key % len(self.map)
        # don't need to start at the dummy node
        curr_node = self.map[index].next 
        # since we aren't updating, don't need to do curr_node.next
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return -1
        

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        # need to start at the dummy node
        curr_node = self.map[index]

        while curr_node and curr_node.next:
            if curr_node.next.key == key:
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)