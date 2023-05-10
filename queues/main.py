from queue import Queue

if __name__ == "__main__":

    q = Queue()

    q.put(12)
    q.put(22)
    q.put(122)

    while not q.empty():
        print(q.get())
# ass