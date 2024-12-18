# A STACK is a LIFO data structure with the following methods:
# pop() - remove the last item added to the stack and return to the user
# append() - add an item to the stack.
# You'll notice that the list data structure already fufills this role, and so you may use the list as a stack.
# Using a list for a stack yields O(1) time complexity for both pop() and append() methods.

# example of using a list as a stack
s = []
s.append(1)
s.append(2)
s.pop()
s.append(3)
s.append(4)
s.pop()
s.pop()
s.append(5)
print(s) # prints ?

# Stacks are handy in certain problems involving recursive structure, undo/redo, or other LIFO scenarios.

# A QUEUE is a FIFO data structure with the following methods:
# enqueue() - add an item to the queue at the end of the line
# dequeue() - remove an item from the front of the line
# Notice that the list data structure is not exactly efficient when dealing with queues, as the analog methods to enqueue() and dequeue() are either:
# pop(0) and append() (pop(0) has O(n) time complexity) 
# OR
# pop() and insert(0) (insert(0) has O(n) time complexity)
# So in Python, a list is not a very good queue because of the time complexity of either dequeueing or enqueueing depending on the combination of operations chosen.  So we import deque (pronounced 'deck')

from collections import deque

# To use the deque as a queue, you can use either of the 2 following combinations of methods:
# append() and popleft()
# appendleft() and pop()
# Here is an example
q = deque()
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.pop()
q.pop()
q.appendleft(4)
q.appendleft(5)
q.pop()
print(q) # prints ?

# WARNING: a deque has O(n) time when accessing indices, say x = q[3].  Avoid using a deque if accessing indices often will be a requirement.

# You can also use a deque as a stack, by using the same pop() and append() methods; however, a list works just fine for a stack as well as described above.
