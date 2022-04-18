from project.controller import Controller


controller=Controller()
print(controller.add_aquarium('FreshwaterAquarium','Seaworld'))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.insert_decoration('Seaworld','Plant'))
print(controller.insert_decoration('Seaworld','Ornament'))
print(controller.add_fish('Seaworld','FreshwaterFish','Nemo','species',2.6))
print(controller.add_fish('Seaworld','FreshwaterFish','Nemo1','species',2.6))
print(controller.add_fish('Seaworld','FreshwaterFish','Nemo2','species',2.6))
# print(controller.add_fish('Seaworld','SaltwaterFish','Nemo','species',2.6))
# print(controller.add_fish('Seaworld','Fish','Nemo','species',2.6))
print(controller.calculate_value('Seaworld'))

print(controller.add_aquarium('SaltwaterAquarium','Saltworld'))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.insert_decoration('Saltworld','Plant'))
print(controller.insert_decoration('Saltworld','Ornament'))

print(controller.add_fish('Saltworld','SaltwaterFish','Nemo11','species',52.6))
print(controller.add_fish('Saltworld','SaltwaterFish','Nemo22','species',12.6))
print(controller.calculate_value('Saltworld'))
print(controller.report())
