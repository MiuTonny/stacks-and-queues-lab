import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # TODO: Add an item to the end of the queue
        self.items.append(item)
    

    def dequeue(self):
        # TODO: Remove and return the item from the front of the queue
        return self.items.pop(0)

    def peek(self):
        # TODO: Return the item at the front of the queue without removing it
        return self.items[0]

    def is_empty(self):
        # TODO: Return True if the queue is empty
        return not self.items
        

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # TODO: Implement winner selection and dequeue process
        if self.is_empty():
            return None
        #random index for winner
        winner_index = random.randint(0, len(self.items) - 1)

        #Dequeue everyone 
        for _ in range(winner_index + 1):
            winner = self.dequeue()
        return winner
