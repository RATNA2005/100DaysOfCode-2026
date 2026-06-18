nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))
k = k % len(nums)
nums = nums[-k:] + nums[:-k]
print("Rotated array:", nums)
#day 4 done by Abhyudaya 590025624