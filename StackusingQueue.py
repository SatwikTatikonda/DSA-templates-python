from queue import Queue

def push(val):
    q1.put(val)

def pop():
    global q1, q2  # Declare q1 and q2 as global variables

    while q1.qsize() > 1:
        q2.put(q1.get())
  
    top = q1.get()
    q1, q2 = q2, q1  # Swap the names of q1 and q2
    return top

q1 = Queue()
q2 = Queue()
for i in range(2, 12, 2):
    push(i)

print(pop())  # Output: 10
print(pop())  # Output: 8


