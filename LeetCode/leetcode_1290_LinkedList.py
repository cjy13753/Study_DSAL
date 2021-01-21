# 1290. Convert Binary Number in a Linked List to integer

# Constraints:
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        marker = self
        node_list = []
        while marker is not None:
            node_list.append(str(marker.val))
            marker = marker.next
        return "|".join(node_list)


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        marker = head
        node_list = []
        while marker is not None:
            node_list.append(str(marker.val))
            marker = marker.next
        tmp_binary_str = "".join(node_list)
        tmp_int = int(tmp_binary_str, 2)
        return tmp_int

given = [1,0,1]
head = ListNode(given[0])
marker = head
for i in range(1, len(given)):
    marker.next = ListNode(given[i])
    marker = marker.next

solution = Solution()
print(solution.getDecimalValue(head))    