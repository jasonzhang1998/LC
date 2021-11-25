# LRU缓存机制


# 使用哈希表加双向链表实现
# 哈希表的键存key，value存储双向链表的节点。双向链表中存储元素的key和value
# 每次get或者更新键值之后，需要将该元素移动到双向链表的表头
# 如果超出容量，则先删除双向链表的表尾元素，然后删除哈希表中对应的项

class BiListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = BiListNode()
        self.tail = BiListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_head(self, key):
        node = self.dic[key]
        # 先把这个节点删除
        node.pre.next = node.next
        node.next.pre = node.pre

        # 再将节点插到表头
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node

    def get(self, key: int) -> int:
        if key in self.dic:
            self.move_to_head(key)
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.move_to_head(key)
            self.dic[key].value = value
        else:
            if len(self.dic) == self.capacity:
                # 删除表尾元素,哈希表中也要删除
                self.dic.pop(self.tail.pre.key)
                self.tail.pre = self.tail.pre.pre
                self.tail.pre.next = self.tail

            # 将元素插到表头
            node = BiListNode(key, value)
            node.pre = self.head
            node.next = self.head.next
            self.head.next = node
            node.next.pre = node
            # 哈希表中也要新增一项
            self.dic[key] = node


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
