def Check_S(s, adat_szam):
    if s.endswith("km"):
        mertekek[adat_szam] = "km"
        return False
    elif s.endswith("m"):
        mertekek[adat_szam] = "m"
        return False
    else:
        print("Hibás adat")
def Format_S(s):
    if s.endswith("km"):
        s = s.replace("km", "")
    elif s.endswith("m"):
        s = s.replace("m", "")
    s = s.split("=")
    return s
def Check_T(t, adat_szam):
    if t.endswith("h"):
        mertekek[adat_szam] = "h"
        return False
    elif t.endswith("m"):
        mertekek[adat_szam] = "m"
        return False
    elif t.endswith("s"):
        mertekek[adat_szam] = "s"
        return False
    else:
        print("Hibás adat")
def Format_T(t):
    if t.endswith("h"):
        t = t.replace("h", "")
    elif t.endswith("m"):
        t = t.replace("m", "")
    elif t.endswith("s"):
        t = t.replace("s", "")
    t = t.split("=")
    return t
def Check_V(v, adat_szam):
    if v.endswith("km/h"):
        mertekek[adat_szam] = "km/h"
        return False
    elif v.endswith("m/s"):
        mertekek[adat_szam] = "m/s"
        return False
    elif v.endswith("km/s"):
        mertekek[adat_szam] = "km/s"
        return False
    else:
        print("Hibás adat")
def Format_V(v):
    if v.endswith("km/h"):
        v = v.replace("km/h", "")
    elif v.endswith("m/s"):
        v = v.replace("m/s", "")
    elif v.endswith("km/s"):
        v = v.replace("km/s", "")
    v = v.split("=")
    return v
def Lower(adat):
    adat = list(adat)
    adat[0] = adat[0].lower()
    adat = "".join(adat)
    return adat

mertekek = [0,0]
cik1 = True
cik2 = True
while cik1:
    adat1 = input("Első adat: ")
    adat1 = Lower(adat1)
    if adat1[0:2] == "s=":
        cik1 = Check_S(adat1,0)
        adat1 = Format_S(adat1)
    elif adat1[0:2] == "t=":
        cik1 = Check_T(adat1,0)
        adat1 = Format_S(adat1)
    elif adat1[0:2] == "v=":
        cik1 = Check_V(adat1,0)
        adat1 = Format_S(adat1)
    else:
        print("Hiba")

while cik2:
    adat2 = input("Második adat: ")
    adat2 = Lower(adat2)
    if adat2[0:2] == "s=":
        cik2 = Check_S(adat2,1)
        adat2 = Format_S(adat2)
    elif adat2[0:2] == "t=":
        cik2 = Check_T(adat2,1)
        adat2 = Format_S(adat2)
    elif adat2[0:2] == "v=":
        cik2 = Check_V(adat2,1)
        adat2 = Format_S(adat2)
    else:
        print("Hiba")
print(mertekek)
print(adat1,adat2)