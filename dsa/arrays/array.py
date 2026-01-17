#creating an empty array 
arr = []

#creating a fixed size static array
static_arr = [None] * 4

print(f"Empty array:{arr}, Static Array: {static_arr}")

#Danger case
arr = [[0]]*5 #this is bad because inner lists point to the same object. instead:

arr = [[0] for _ in range(5)]
print(f"Array created using list comprehension {arr}")

#Making something iterable using list
iter = list("abc")
print(f"Typecasting abc to list(abc): {iter}")

print(f"Typecasting using list the range function gives you a list of numbers range would have rerturned: {list(range(5))}")

#Indexing and Negative Indexing
arr = [0,1,2,3]
print(f"doing arr[2] will return me the third element {arr[2]}. returns indexError if out of bounds")

print(f"reverse indexing. -1 = last element. -2 = second last element")
print(arr[-1], arr[-2])

#updating elements.
#slice updating
a = [1,2,3,4,5]
a[1:4] = [20,30,40] #updating 2,3,4 to 20, 30, 40
print(f"post slciing update:{a} ")

#inserting in middle: expensive.
arr = [1,2,3,4,5]
arr.insert(2,30)
print(f"Post inserting {arr}")

#deleting
del arr[2]
print(f"Post deleting {arr}")

#reverse array
print(arr[::-1])
print(arr.reverse()) #reverse in place