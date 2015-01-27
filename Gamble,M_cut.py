code = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cut1 = code.find("GAATTC") + 1
cut2 = len(code) - cut1
print("Fragment1 length = " + str(cut1))
print("Fragment2 length = " + str(cut2))
