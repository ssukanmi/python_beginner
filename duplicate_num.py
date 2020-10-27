def findDup(nums):
    tort = nums[0]
    hare = nums[0]
    while True:
        tort = nums[tort]
        hare = nums[nums[hare]]
        if tort == hare:
            break

    r1 = nums[0]
    r2 = tort
    while r1 != r2:
        r1 = nums[r1]
        r2 = nums[r2]

    return f"Your duplicate number is {r1}"


print(findDup([6, 2, 9, 4, 3, 1, 7, 1, 8, 5]))
