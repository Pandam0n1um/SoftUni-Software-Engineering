from collections import deque


def mixing(magic, mat):
	total = magic + mat
	if total < 100:
		if total % 2 == 0:
			total = (2 * mat) + (3 * magic)
		else:
			total *= 2
	elif total > 499:
		total /= 2
	for el, data in gift_dict.items():
		if data['range'][0] <= total <= data['range'][1]:
			gift_dict[el]['count'] += 1
			return


gift_dict = {
	'Diamond Jewellery': {'range': [400, 499], 'count': 0},
	'Gemstone': {'range': [100, 199], 'count': 0},
	'Gold': {'range': [300, 399], 'count': 0},
	'Porcelain Sculpture': {'range': [200, 299], 'count': 0},
}

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

while True:
	if not (materials and magic_level):
		break
	mixing(magic_level.popleft(), materials.pop())

if (gift_dict['Gemstone']['count'] and gift_dict['Porcelain Sculpture']['count']) or (
		gift_dict['Gold']['count'] and gift_dict['Diamond Jewellery']['count']):
	print(f"The wedding presents are made!")
else:
	print("Aladdin does not have enough wedding presents.")

if materials:
	print(f"Materials left: {', '.join(str(mat) for mat in materials)}")
if magic_level:
	print(f"Magic left: {', '.join(str(mag) for mag in magic_level)}")

for el, data in gift_dict.items():
	if data['count']:
		print(f"{el}: {data['count']}")
