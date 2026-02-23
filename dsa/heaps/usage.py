import heapq

arr = [2,1,4,1,5,9,2]

heapq.heapify(arr) #[1, 1, 2, 2, 5, 9, 4]

heapq.heappush(arr, 0) #[0, 1, 2, 1, 5, 9, 4, 2]

min_element = heapq.heappop(arr) #0

"""
by default we get a min heap, so to make it behave like a max heap you can negate the values in the list
and then convert it into a heap using the heapify function.
"""

negated_arr = [-x for x in arr]

heapq.heapify(negated_arr)

heapq.heappush(negated_arr, -11) #push 11 to the heap

max_element = heapq.heappop(negated_arr)*-1 #11

"""
Storing Tuples.
By default heap is ordered based on the first element in the tuple.
If first elemnts are equal, second elements are compared and so on.
"""

tuple_arr = [(3, 1), (1, 5), (4, 2), (1, 9), (5, 3), (9, 4), (2, 6)]

heapq.heapify(tuple_arr)

min_element = heapq.heappop(tuple_arr)
print(min_element)
