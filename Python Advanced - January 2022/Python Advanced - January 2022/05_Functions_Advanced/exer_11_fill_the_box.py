def fill_the_box(height,length,width,*args):
    box_vol=height*length*width
    remaining=0
    failed=False

    for el in args:
        if el=="Finish":
            break
        if el>box_vol:
            failed=True
            remaining+=el-box_vol
            el=el-box_vol
            box_vol=0
        else:
            box_vol-=el
    if failed:
        return f"No more free space! You have {remaining} more cubes."
    else:
        return f"There is free space in the box. You could put {box_vol} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
