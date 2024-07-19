passwd = input("Enter you password")
result = {}
if len(passwd) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for s in passwd:
    if s.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for s in passwd:
    if s.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)

if all(result.values()):
    print(f" Strong password {all(result.values())}")
else:
    print(f"week passwd {all(result.values())}")