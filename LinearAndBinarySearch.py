#Linear search - O(n)
def linear_search(unordered_list, search_value):
    for index in range(len(unordered_list)):
        if unordered_list[index] == search_value:
            return True
    return False

# Binary search only applies to ordered lists - O(log n)
# Much better time complexity than linear search
def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1

    while first <= last:
        middle = (first + last)//2

        if search_value == ordered_list[middle]:
            return True
        
        elif search_value < ordered_list[middle]:
            last = middle - 1
        
        else:
            first = middle + 1

print(binary_search([1,5,8,9,15,20,70,72], 5))


def binary_search_recursive(ordered_list, search_value):
  # Define the base case
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return binary_search_recursive(ordered_list[middle+1:], search_value)
  
print(binary_search_recursive([1,5,8,9,15,20,70,72], 5))