# init_hours = int(input())
#
# init_minutes = int(input())
#
# new_minutes = int(init_minutes + 15)
#
# output_hours = 0
#
# output_minutes = int(new_minutes % 60)
#
# if 0 <= init_minutes <= 44 and 0 <= init_hours <= 23:
#     output_hours = init_hours
#
# elif 45 < init_minutes and 0 <= init_hours < 23:
#     output_hours = init_hours + 1
#
# elif 45 < init_minutes and init_hours == 23:
#     output_hours = 0
#
# elif 45 == init_minutes and 0 <= init_hours < 23:
#     output_hours = init_hours + 1
#
# elif 45 == init_minutes and init_hours == 23:
#     output_hours = 0
#
# print(f"{output_hours}:{output_minutes:02d}")

# newcode

init_hours = int(input())

init_minutes = int(input())

sum_minutes = int(init_minutes + 15)

output_hours = 0

output_minutes = int(sum_minutes % 60)

if 59 < sum_minutes:
    output_hours = init_hours + 1
else:
    output_hours = init_hours

if 23 < output_hours:
    output_hours = output_hours - 24
else:
    output_hours = output_hours

print(f"{output_hours}:{output_minutes:02d}")
