#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length-1)
    route = [None] * (length-1)
    for tix in tickets:
        if tix.source=='NONE':
            curr=tix.destination
            route[0]=curr
        else:
            hash_table_insert(hashtable,tix.source,tix.destination)
    indx=1
    while True:
        curr=hash_table_retrieve(hashtable,curr)
        if curr=='NONE':
            break
        else:
            route[indx]=curr
            indx+=1
    return route

