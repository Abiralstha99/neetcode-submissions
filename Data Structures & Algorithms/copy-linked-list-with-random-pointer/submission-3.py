"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        # 2 passes: 1st to iterate -> create node -> map out old pointer -> new pointer
        # 2nd -> assign next and random points


        current = head
        dict = {None:None}

        while current:
            newNode = Node(current.val,None, None)
            dict[current] = newNode
            current = current.next

        # Now loop again to assign the random pointers

        # reset current
        current = head
        while current:
            newNode = dict[current]
            newNode.next = dict[current.next]
            newNode.random = dict[current.random]
            current = current.next
        
        return dict[head]
