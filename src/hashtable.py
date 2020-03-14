# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.count = 0
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # get hashed value
        index = self._hash_mod(key)
        print(index, key, value)
        
        # see if hashed value exists
        if self.storage[index] is not None:
            # match at first linkedPair, 
            if self.storage[index].key == key:
                self.storage[index].value = value
                return

            ## take in index and iterate through to end of LinkedPairs to add to end
            current_pair = self.storage[index]

            while current_pair is not None:
                print('*** FIND ***', key, current_pair.key, current_pair.value)
                # if key match
                if current_pair.key == key:
                    # update value with new value
                    current_pair.value = value
                    print('*** UPDATE ***', current_pair.key, current_pair.value)
                    return

                if current_pair.next is not None:
                    # no match, iterate to next
                    current_pair = current_pair.next
                else: 
                    # no match, add to end of LinkedPair chain
                    current_pair.next = LinkedPair(key, value)
                    print(f"INSERT {key} at {index}")
                
        else:
            # no value at storage index
            self.storage[index] = LinkedPair(key, value)
            print(f"INSERT {key} at {index}")

        self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get hashed value
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            self.storage[index] = None
        else:
            print('Error, key not found')
            return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get hashed value
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        else:
            current_pair = self.storage[index]

            while current_pair is not None:
                print('---looking for key', key, current_pair.key, current_pair.value)
                if current_pair.key == key:
                    return current_pair.value
                
                current_pair = current_pair.next
            
            print('key not found')
            return
            


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_table = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for headPair in old_table:
            if headPair is None:
                return
            else:
                self.insert(headPair.key, headPair.value)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
