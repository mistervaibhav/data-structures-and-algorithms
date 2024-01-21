from queue import LifoQueue

if __name__ == "__main__":
    # LifoQueue is a stack !
    q = LifoQueue()

    q.put(12)
    q.put(22)
    q.put(122)

    while not q.empty():
        print(q.get())
