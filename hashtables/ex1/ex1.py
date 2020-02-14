#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for curr in range(len(weights)):
            
        wt=weights[curr]
        opp=limit-wt
        htop=hash_table_retrieve(ht, opp)
        if htop==None:
            hash_table_insert(ht, wt, curr)
        else:
            if htop>curr:
                return (htop,curr)
            else:
                return (curr,htop)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
