from classes import linkedList

# Request number of nodes from user
request_string = "Please, enter the number of nodes: "
while True:
    try:
        num_nodes = int(input(request_string))
        # Raise exception if number is less than 1 (does not make sense for linked list)
        if (num_nodes < 1):
            raise Exception
        break
    except Exception:
        # If incorrect input, print newline and change request message
        print()
        request_string = "Please, enter correct value for number of nodes: "


# Create linked list based on user input
newList = linkedList(num_nodes)
# Output information about newly created list
print("Unsorted list: " + str(newList))
print("Head data: {}".format(newList.head.data))
print("Tail data: {}\n".format(newList.tail.data))

# Sort list
newList.sort()
# Output sorted list information
print("Sorted list: " + str(newList))
print("Head data: {}".format(newList.head.data))
print("Tail data: {}\n".format(newList.tail.data))