import math

width=float(input())

height=float(input())

area_hall=float(width*height*100*100)

rows=math.floor((height-1)/0.7)

columns=math.floor(width/1.2)

seat_count=float(rows*columns-3)

print(seat_count)