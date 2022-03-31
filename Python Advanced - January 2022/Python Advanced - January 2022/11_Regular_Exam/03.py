def start_spring(**example_objects):
	spring_objects = dict()

	for object_type, spring_object in example_objects.items():
		if spring_object not in spring_objects:
			spring_objects[spring_object] = []
		spring_objects[spring_object].append(object_type)
	sorted_spring_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))

	result = []
	for item_type, item_collection in sorted_spring_objects:
		curr_result = f"{item_type}:"
		curr_result += ''.join([f"\n-{x}" for x in sorted(item_collection, key=lambda x: x)])
		result.append(curr_result)

	return '\n'.join(result)



example_objects = {"Water Lilly": "flower",
				   "Swifts": "bird",
				   "Callery Pear": "tree",
				   "Swallows": "bird",
				   "Dahlia": "flower",
				   "Tulip": "flower", }

print(start_spring(**example_objects))
print()
example_objects = {"Swallow": "bird",
				   "Thrushes": "bird",
				   "Woodpeckers": "bird",
				   "Swallows": "bird",
				   "Warblers": "bird",
				   "Shrikes": "bird", }
print(start_spring(**example_objects))
print()
example_objects = {"Magnolia": "tree",
				   "Swallow": "bird",
				   "Thrushes": "bird",
				   "Pear": "tree",
				   "Cherries": "tree",
				   "Shrikes": "bird",
				   "Butterfly": "insect"}

print(start_spring(**example_objects))
