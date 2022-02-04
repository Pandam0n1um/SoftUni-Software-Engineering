lost_fights_count=int(input())
helmet_price=float(input())
sword_price=float(input())
shield_price=float(input())
armor_price=float(input())


helmet_repair_count=lost_fights_count//2

sword_repair_count=lost_fights_count//3

shield_repair_count=lost_fights_count//6

armor_repair_count=lost_fights_count//12

repair_cost=(helmet_repair_count*helmet_price+sword_repair_count*sword_price+shield_repair_count*shield_price+armor_repair_count*armor_price)

print(f"Gladiator expenses: {repair_cost:.2f} aureus")
