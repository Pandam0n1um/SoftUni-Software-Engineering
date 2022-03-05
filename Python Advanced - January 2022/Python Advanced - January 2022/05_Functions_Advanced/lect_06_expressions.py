def expression(nums, curr_result=0, current_expression=''):
    if not nums:
        print(f"{current_expression}={curr_result}")
        return
    expression(nums[1:], curr_result + nums[0], f'{current_expression}+{nums[0]}')
    expression(nums[1:], curr_result - nums[0], f'{current_expression}-{nums[0]}')


nums = [int(el) for el in input().split(", ")]
expression(nums)
