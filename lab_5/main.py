def angry_beaver(binary_in, x):
    binary_x = []
    power = 0
    insert_string = ""
    while len(insert_string) <= len(binary_in):
        insert_string = "{0:b}".format(pow(x, power))
        binary_x.insert(0, insert_string)
        power += 1

    def solution(input, counter=0):
        for i in range(0, len(binary_in)):
            if input[i:] in binary_x:
                counter += 1
                counter = solution(input[:i], counter)
                break
        return counter

    return solution(binary_in)


binary_in = "101101101"
x = 5

print(angry_beaver(binary_in, x))
