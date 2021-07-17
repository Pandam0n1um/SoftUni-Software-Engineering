aq_length = float(input())

aq_width = float(input())

aq_height = float(input())

aq_percentage_occupied = float(input())

aq_volume = float(aq_length * aq_width * aq_height*0.001)

aq_volume_water = float((aq_volume * (100 - aq_percentage_occupied) *0.01))

print(aq_volume_water)
