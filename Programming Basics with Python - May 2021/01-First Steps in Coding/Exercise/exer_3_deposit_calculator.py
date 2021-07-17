deposit_sum = float(input())

deposit_period = float(input())

yearly_interest_rate = float(input())

outcome_sum = float(deposit_sum + deposit_period * ((deposit_sum * yearly_interest_rate) / 100) / 12)

print(outcome_sum)





deposit_sum = float(input())

deposit_period = float(input())

yearly_interest_rate = float(input())

monthly_interest_ammount = float((deposit_sum * yearly_interest_rate / 100) / 12)

outcome_sum = float(deposit_sum + deposit_period * monthly_interest_ammount)

print(outcome_sum)
