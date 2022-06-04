def bubleSort(nums):
    """Function to Demonstrate Buble Sort"""
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
		# Swapping value if first number is greater than second number
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
               # print(numbers)


numbers = [5, 3, 8, 6, 7, 2]
bubleSort(numbers)
print("Sorted Array is", numbers)
