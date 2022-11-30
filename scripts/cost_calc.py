"""
Simple script to calculate costs for different countries.

Parameter: val.
Can be list or int.
Asks for currency type and number of semesters.

Example 1 :
conv(1)
1. for EUR
2. for Cad
3. for USD
Input:1
Number of Semester:1
84.32

Example 2:
conv([144, 790*6])
1. for EUR
2. for Cad
3. for USD
Input:1
Number of Semester:4
1647275.52
"""

eur = 84.32
cad = 58.35
usd = 74.47

def conv(val):
    c = int(input("1. for EUR\n2. for Cad\n3. for USD\nInput:"))
    ct = [eur,cad,usd]
    ctu = ct[c-1]
    month = int(input("Number of Semester:"))
    try:
        if isinstance(val,list):
            return round(sum(ctu*i for i in val)*month,2)
        else:
            return round(ctu*val*month,2)
        
    except:
        print("Not yay")


# print(conv(8511.21))