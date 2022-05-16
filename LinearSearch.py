pos = -1    # -1 represents initially no index

def LinearSearch(list, n):
    '''LinearSearch(list, number) takes list and number as a arguments and return boolean value'''
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1

    return False


list = [5, 8, 4, 6, 9, 2]
n = 9

if LinearSearch(list, n):
    print("Item Found at ", pos)
else:
    print("Not Found")