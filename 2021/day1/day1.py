# PART 1
with open("day1.in", "r") as f:
    nums = [int(i) for i in f.read().split("\n")]

count = 0


for i in range(len(nums) - 1):
    if nums[i + 1] > nums[i]:
        count += 1

print(count)

# PART 2
count2 = 0

for i in range(len(nums) - 3):
    if nums[i + 3] > nums[i]:
        count2 += 1

print(count2)