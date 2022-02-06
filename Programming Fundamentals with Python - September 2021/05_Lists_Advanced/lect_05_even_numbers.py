nums_as_string = input().split(", ")

nums = [int(elem) for elem in nums_as_string]

# nums_map = list(map(lambda el: int(el), nums_as_string))
#
# nums_map_ref=list(map(int,nums_as_string))

filtered_nums = [index for index in range(len(nums)) if nums[index] % 2 == 0]

filtered_num_filter = list(map(lambda el: nums.index(el), list(filter(lambda el: el % 2 == 0, nums))))

print(filtered_nums)

# print(nums)
