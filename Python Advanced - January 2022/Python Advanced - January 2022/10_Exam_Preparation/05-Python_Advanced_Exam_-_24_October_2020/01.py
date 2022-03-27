jobs = [int(x) for x in input().split(', ')]
task_index = int(input())

sorted_jobs = sorted(
    [(v, i) for (i, v) in enumerate(jobs)]
)
# print(jobs)
# print(sorted_jobs)
cycles = 0
for (job, index) in sorted_jobs:
    cycles += job
    if index == task_index:
        break
print(cycles)