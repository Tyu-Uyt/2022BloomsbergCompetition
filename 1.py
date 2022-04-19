from statistics import mean
from math import ceil

nums = [int(x) for x in input("Enter net worth for the people: ").split(" ")]
avg = mean(nums)

print("Needed for happiness: " + ' '.join([str(0 if x >= avg else avg - x) for x in nums]))