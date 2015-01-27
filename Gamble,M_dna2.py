from __future__ import division

code = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
at = code.replace('A', 't')
print(at)
ta = at.replace('T', 'a')
print(ta)
cg = ta.replace('C', 'g')
print(cg)
gc = cg.replace('G', 'c')
print(gc)
print(gc.upper())
