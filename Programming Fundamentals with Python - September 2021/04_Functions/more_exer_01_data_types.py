def data_types(cmnd,val):
    if cmnd=="int":
        val=int(val)*2
        print(val)
        return
    elif cmnd=="real":
        val=float(val)*1.5
        print(f"{val:.2f}")
        return
    elif cmnd=="string":
        print(f"${val}$")
        return

command=input()
value=input()

data_types(command,value)