from Queue import Queue

queue = Queue()
queue.push(55)
queue.push(75)
queue.push(99)
queue.push(21)

print(queue.peek())

queue.pop()

print(queue.peek())

queue.pop()

print(queue.peek())

queue.pop()

print(queue.peek())

queue.pop()

print(queue.peek())