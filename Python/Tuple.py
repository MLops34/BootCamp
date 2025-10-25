# # # # empty_tuple=()
# # # # print(empty_tuple)
# # # # print(type(empty_tuple))

# # # lst=list()
# # # print(type(lst))
# # # tpl=tuple()
# # # print(type(tpl))

numbers=tuple([1,2,3,4,5,6])
numbers


mixed_tuple=(1,"Hello World",3.14, True)
print(mixed_tuple)

## Tuple Operations

concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)

## Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)