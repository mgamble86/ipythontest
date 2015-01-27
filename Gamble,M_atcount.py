from __future__ import division

code = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
size = len(code)
a_count = code.count('A')
t_count = code.count('T')

at_count = (a_count + t_count) / size
print("AT count = " + str(at_count))
