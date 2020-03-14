#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # iterate through the list weights 
    # declare the [key, value] pair 
    # check if hash table contains limit weight 
    # if it does check the index of the limit weight 
    # function should return None if [key, value] does not exist in the list 
    

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
