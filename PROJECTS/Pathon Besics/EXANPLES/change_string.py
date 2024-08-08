lsts = ["1.ecom","2.business","3.education"]

libs = [ lst.replace('.','-') + '.txt' for lst in lsts]

print(libs)