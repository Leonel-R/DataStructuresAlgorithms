#Sorting Algorithms:

#Bubble sorts are not good for highly unsorted large lists: O(n^2)
#Bubble sorts are good for large sorted/almost sorted lists or small lists
def bubble_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length-1):
        for j in range(list_length-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j] , my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

#better version that will check if list is already sorted
def bubble_sort(my_list):
    list_length = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(list_length-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1] , my_list[i]
                is_sorted = False
        list_length -= 1


#Selection sort: O(n^2)
def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        lowest = my_list[i]
        index = i
        for j in range(i + 1, list_length):
            if my_list[j] < lowest:
                index = j
                lowest = my_list[j]
        my_list[i] , my_list[index] = my_list[index] , my_list[i]
    return my_list

#Insertion sort: O(n^2)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        number_to_order = my_list[i]
        j = i - 1
        while j >= 0 and number_to_order < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = number_to_order
    return my_list

#Merge sort: O(n logn) - suitable for sorting large unorganized lists
#Significant improvement over above sorting algorithms
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i+=1
            else:
                my_list[k] = right_half[j]
                j+=1
            k+=1
        
        while i < len(left_half):
            my_list[k] = left_half[i]
            i+=1
            k+=1
        while j < len(right_half):
            my_list[k] = right_half[j]
            j+=1
            k+=1

my_list = [35,22,90,4,50,20,30,40,1]
merge_sort(my_list)
print(my_list)

#Quicksort: O(n^2) but has better average and best case complexity compared to bubble,insertion, and selection sorts 
def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index
    while True:
        while my_list[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1
        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if  left_pointer >= right_pointer:
            break
        my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]
    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    return right_pointer


def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
        partition_index = partition(my_list, first_index, last_index)
        quicksort(my_list,first_index, partition_index)
        quicksort(my_list, partition_index+1, last_index)




