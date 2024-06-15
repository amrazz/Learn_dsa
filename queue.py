"""
Queuee is a linear datastructure where the element is inserted from one side and removed from other side

Queue will be open at both of the ends so insertion and removal done in both ends

FIFO : First in First out
LILO : Last in Last Out

back/tail/rear -->  ▢▢▢▢▢▢▢▢▢▢   ---> head/Front

 dequeue  --> ▢▢▢▢▢▢▢▢▢▢ --> Enqueue

 ENQUEUE process of adding the elements to queue    (APPEND method)
 DEQUEUE process of removing the elemets from the queue (pop method)

isFull : to check if the queue is full 
isEmpty: to check if the queue is empty.

?. Where we can use queue operations DS?

ans. we use queue while uploading photos where we upload photos, print documents and in real life scenarios
    where we in the music player we use queue to play the next music as we needed
    
    
"""

"""     Implement Queue     """


queue = []
"""queue.append(39)
queue.append(546)
queue.append(45)

queue.pop(0)
queue.pop(0)
"""

# queue.insert(0, 39)
# queue.insert(0, 546)
# queue.insert(0, 45)

# queue.pop()
# queue.pop()
# print(queue)

"""
def enqueue():
    print("Enter the element that you want to insert")
    element = int(input())
    
    queue.insert(0, element)
    print(f"{element} has been inserted!")
    print(queue)
    
def dequeue():
    if queue:
        e = queue.pop()
        print(f"{e} is removed from the queue")
        print(queue)
    else:
        print("The queue is empty!!")
        
while True:
    print("Enter the operation that you want to perform 1.add  2.remove  3.View Queue  4.Quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        print(queue)
    elif choice == 4:
        print("Thank you for using me Come again!!")
        break
    else:
        print("Entered operation not found!!")"""


"""I want to use appendleft using the deque and pop from the right """

from collections import deque

# q = deque()
# q.appendleft(34)
# q.appendleft(23)
# q.pop()
# print(q)


"""I want to use append using the deque and popleft from left"""

q = deque()
q.append(54)
q.append(32)
q.popleft()

print(q)
