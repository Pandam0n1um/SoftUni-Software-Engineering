start_first_pair=int(input())
start_second_pair=int(input())
diff_first_pair_interval=int(input())
diff_second_pair_interval=int(input())
end_first_pair=start_first_pair+diff_first_pair_interval+1
end_second_pair=start_second_pair+diff_second_pair_interval+1

for first_pair in range (start_first_pair,end_first_pair):
    is_fp_prime = False
    fp_prime_counter=0
    for i in range(1,first_pair+1):
        if first_pair%i==0:
            fp_prime_counter+=1
    if fp_prime_counter==2:
            is_fp_prime=True
    else:
        continue

    for second_pair in range(start_second_pair,end_second_pair):
        is_sp_prime = False
        sp_prime_counter=0
        for j in range(1, second_pair+1):
            if second_pair % j == 0:
                sp_prime_counter += 1
        if sp_prime_counter == 2:
            is_sp_prime = True
        if is_fp_prime and is_sp_prime:
            print(f"{first_pair}{second_pair}")