length_input_value = float(input())

length_input_unit = str(input().lower())

length_output_unit = str(input().lower())

length_output_value=0

if length_input_unit == str('m'):
    length_input_value = length_input_value

elif length_input_unit == str('cm'):
    length_input_value = length_input_value * 0.01

elif length_input_unit == str('mm'):
    length_input_value = length_input_value * 0.001

if length_output_unit == str('m'):
    length_output_value=length_input_value

elif length_output_unit==str('cm'):
    length_output_value=length_input_value*100

elif length_output_unit==str('mm'):
    length_output_value=length_input_value*1000

print(f"{length_output_value:.3f}")
