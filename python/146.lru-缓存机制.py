#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class LinkedNode():
    # 双向链表，需要保存key以便删除hashmap中值使用
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = dict()

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move2head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.move2head(node)
        else:
            node = LinkedNode(key, value)
            self.hashmap[key] = node
            self.add2head(node)
            if self.size < self.capacity:
                self.size += 1
            else:
                self.remove_tail()
    
    @staticmethod
    def remove_node(node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def add2head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def move2head(self, node):
        self.remove_node(node)
        self.add2head(node)
        
    def remove_tail(self):
        tail = self.tail.prev
        self.remove_node(tail)
        self.hashmap.pop(tail.key)


l=LRUCache(2)
print(l.put(1,1))
print(l.put(2,2))
print(l.get(1))
print(l.put(3,3))
print(l.get(2))
print(l.put(4,4))
print(l.get(1))
print(l.get(3))
print(l.get(4))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

