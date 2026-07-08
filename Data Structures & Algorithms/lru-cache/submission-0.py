class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> value(Node)
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    # inserting at the end
    def insert(self, node):
        prev,next = self.tail.prev, self.tail
        prev.next = node
        next.prev = node
        node.prev, node.next = prev, next

    # removing from the head
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update the most recent used
            # Remove and Insert at the end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # first check if the key exist or not
        if key in self.cache:
            # Remove from the list and add again 
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
       
        if len(self.cache) > self.capacity:
            # self.remove the least recently used key -- self.remove head
            LRU_node = self.head.next
            self.remove(LRU_node)
            del self.cache[LRU_node.key]
