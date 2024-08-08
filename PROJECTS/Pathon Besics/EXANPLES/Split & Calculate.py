info = input("Enter info with " )

def get_dat(info):
    lst = info.split(" ")
    mes = [float(i) for i in lst]
    return  f"list to number {mes} "

print(get_dat(info))


