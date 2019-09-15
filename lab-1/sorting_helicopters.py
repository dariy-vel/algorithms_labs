import time

comparison_counter = 0


def sort_by_max_height(list_of_helicopters):  # Selection sort
    print("- - - - - - - - - - -")
    print("Algorithm name: " + "\033[1m" + "Selection Sort" + "\033[0m")  # Bold algorithm name
    start_time = time.time()
    global comparison_counter
    comparison_counter = 0
    swap_counter = 0
    for a in range(len(list_of_helicopters)):
        min_height = 0
        min_position = 0
        for i in range(a, len(list_of_helicopters)):
            if min_height == 0:
                min_position = i
                min_height = list_of_helicopters[i].max_height
            elif list_of_helicopters[i].max_height < min_height:
                min_height = list_of_helicopters[i].max_height
                min_position = i
            comparison_counter += 1

        # Swapping
        if min_position != 0 and min_height != 0 and min_position != a:
            temp_helicopter = list_of_helicopters[a]
            list_of_helicopters[a] = list_of_helicopters[min_position]
            list_of_helicopters[min_position] = temp_helicopter
            swap_counter += 1

    print("Time of execution: %f s" % (time.time() - start_time))
    print("Comparison was made %d times" % comparison_counter)
    print("Swap was made %d times" % swap_counter)
    for i in list_of_helicopters:
        print(i)
    print("- - - - - - - - - - -")


def sort_by_max_mass(list_of_helicopters):
    print("- - - - - - - - - - -")
    print("Algorithm name: " + "\033[1m" + "Merge Sort" + "\033[0m")  # Bold algorithm name
    start_time = time.time()
    global comparison_counter
    comparison_counter = 0

    def split(input_list):
        if len(input_list) <= 1:
            return input_list

        middle_point = len(input_list) // 2

        left_part = input_list[0:middle_point]
        right_part = input_list[middle_point:]
        return merge(split(left_part), split(right_part))

    def merge(left_part, right_part):
        if left_part is None or right_part is None:
            return

        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index].max_mass >= right_part[right_index].max_mass:
                result.append(left_part[left_index])
                left_index += 1
            else:
                result.append(right_part[right_index])
                right_index += 1
            global comparison_counter
            comparison_counter += 1
        result = result + left_part[left_index:] + right_part[right_index:]
        return result

    list_of_helicopters = split(list_of_helicopters)
    print("Time of execution: %f s" % (time.time() - start_time))
    print("Comparison was made %d times" % comparison_counter)
    for i in list_of_helicopters:
        print(i)
    print("- - - - - - - - - - -")
