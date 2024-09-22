from collections import deque
dq = deque(range(10),maxlen=10)
print(dq)

dq.rotate(3)
print(dq)
dq.appendleft(10)
print(dq)# LIFO usally but here its append left so,
dq.extend([11, 22, 33])#deque remove the first one and insert form last LIFO
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

money = 0.85
val =f"money: {money*10000:.2f}"
print(val)

tt = (1,2,(30,40))
print(hash(tt))

tt = (1, 2, frozenset([30, 40]))
print(hash(tt))

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)


class queueusingstack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
             self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None



queue = queueusingstack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
first = queue.dequeue()
second = queue.dequeue()
third = queue.dequeue()

print("\n{}\n{}".format(second, third))
print(f"\n{second}\n{third}")
print("\n" + str(second) + "\n" + str(third))


