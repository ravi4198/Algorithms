pos = -1


def search(list, number):
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] == number:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < number:
                lower = mid + 1
            else:
                upper = mid - 1
    return False


list = [4, 7, 8, 12, 45, 99, 100, 115]
n = 45

if search(list, n):
    print("Value found at", pos)
else:
    print("Value is not found")
