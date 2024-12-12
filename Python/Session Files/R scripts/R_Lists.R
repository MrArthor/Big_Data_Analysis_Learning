# R -List
mylist <- list("grapes","Banana","Orange")
mylist
# access list using indes
mylist[2]
# Change Item Value
mylist[3]= "guava"
mylist
length(mylist)
# check the specific item exist or not
"Orange" %in% thislist

# add any item to the end of list
append(student,"lichi")
# add any item to the list to a specific position
mylist2 <- list("BCA","MCA","MTech")
mylist2
append(mylist2,"BTech", after=2)
# Remove item from the list:
thislist <- list("apple", "banana", "cherry")

newlist <- thislist[-1]

# Print the new list
newlist
# To find the specify a range of items
thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

(thislist)[2:5]
# Join Two Lists

list1 <- list("a", "b", "c")
list2 <- list(1,2,3)
list3 <- c(list1,list2)

list3