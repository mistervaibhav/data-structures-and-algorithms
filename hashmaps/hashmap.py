class HashMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.__count = 0
        self.__bucket_size = 10
        self.__buckets = [None] * self.__bucket_size

    def __len__(self):
        return self.__count

    def __str__(self):
        string = "{ \n"

        for head in self.__buckets:
            while head is not None:
                print("iter", head.key)
                string += f"  {head.key} : {head.value}, \n"
                head = head.next

        string += "}"

        return string

    def __get_hash_code(self, key):
        return hash(key)

    def __get_compressed_hash(self, hash_code):
        return abs(hash_code) % self.__bucket_size

    def insert(self, key, value):
        hash_code = self.__get_hash_code(key)
        index = self.__get_compressed_hash(hash_code)

        head = self.__buckets[index]

        while head is not None:
            if head.key == key:
                head.value = value
                return

            head = head.next

        head = self.__buckets[index]

        new_node = HashMapNode(key, value)
        new_node.next = head

        self.__buckets[index] = new_node
        self.__count += 1
        print("INSERTED", key, "VALUE => ", value)

    def get(self, key, default=None):
        hash_code = self.__get_hash_code(key)
        index = self.__get_compressed_hash(hash_code)

        head = self.__buckets[index]

        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        if default is not None:
            return default

        raise Exception(f"[KeyError]: {key} does not exist ")

    def remove(self, key):
        hash_code = self.__get_hash_code(key)
        index = self.__get_compressed_hash(hash_code)

        head = self.__buckets[index]

        prev = None

        for head in self.__buckets:
            while head is not None:
                if head.key == key:
                    if prev is None:
                        self.__buckets[index] = head.next
                    else:
                        prev.next = head.next

                    self.__count -= 1
                    return head.value

                prev = head
                head = head.next

        raise Exception(f"[KeyError]: {key} does not exist ")


if __name__ == "__main__":
    map = HashMap()

    map.insert("hello", "point")
    map.insert(2, "alpha")
    map.insert(3, "beta")
    map.insert(4, "gamma")
    map.insert(5, "delta")
    map.insert(10, "epsilon")
    map.insert("numbers", [1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(map)
    print(map.get(5))
    # map.remove(4)
    # print(map)
