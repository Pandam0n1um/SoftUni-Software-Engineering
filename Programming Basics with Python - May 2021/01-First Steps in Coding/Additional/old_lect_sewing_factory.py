rect_cover_price = 7

square_cover_price = 9

usd_to_bgn = float(1.85)

amount_tables = int(input())

length_rect_tables = float(input())

width_rect_tables = float(input())

rect_cover_area_total = float((length_rect_tables + (2 * 0.3)) * (width_rect_tables + (2 * 0.3))*amount_tables)

square_cover_area_total = float((0.5 * length_rect_tables) * (0.5 * length_rect_tables)*amount_tables)

cover_total_price_usd = float(((rect_cover_area_total*rect_cover_price)+(square_cover_area_total*square_cover_price)))

cover_total_price_bgn = float(cover_total_price_usd * usd_to_bgn)

print(f"{cover_total_price_usd:.2f} USD")

print(f"{cover_total_price_bgn:.2f} BGN")

print(square_cover_area_total)

print(rect_cover_area_total)
