volume_pool = int(input())

pipe_1_inflow = int(input())

pipe_2_inflow = int(input())

time_absent = float(input())

pipe_1_inflow_total = float(pipe_1_inflow * time_absent)

pipe_2_inflow_total = float(pipe_2_inflow * time_absent)

total_inflow = float(pipe_1_inflow_total + pipe_2_inflow_total)

if total_inflow<=volume_pool:
    volume_pool_percentage=float(total_inflow/volume_pool*100)
    pipe_1_inflow_participation=float(pipe_1_inflow_total/total_inflow*100)
    pipe_2_inflow_participation=float(pipe_2_inflow_total/total_inflow*100)
    print(f"The pool is {volume_pool_percentage:.2f}% full. Pipe 1: {pipe_1_inflow_participation}%. Pipe 2: {pipe_2_inflow_participation}%.")

else:
    total_overflow=float(total_inflow-volume_pool)
    print(f"For {time_absent} hours the pool overflows with {total_overflow:.2f} liters.")