eur = 84.32
cad = 58.35
usd = 74.47

def conv(val):
    c = int(input("1. for EUR\n2. for Cad\n3. for USD\nInput:"))
    ct = [eur,cad,usd]
    ctu = ct[c-1]
    month = int(input("Number of Months:"))
    try:
        if isinstance(val,list):
            return round(sum(ctu*i for i in val)*month,2)
        else:
            return round(ctu*val*month,2)
        
    except:
        print("Not yay")
