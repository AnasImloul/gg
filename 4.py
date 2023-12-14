
f1 = "JACKIE WILL BUDGET FOR THE MOST EXPENSIVE ZOOLOGY EQUIPMENT"
f2 = "DAOFJK XJCC PVQNKW STH WUK RTBW KYZKLBJGK MTTCTNI KEVJZRKLW"
s1 = "ZELDA MIGHT FIX THE JOB GROWTH PLANS VERY QUICKLY ON MONDAY"
s2 = "XSFIY TANBD QAO DBS MPR NJPLDB GFYCK USJW HEAZVFW PC TPCIYW"
target = "RDJV VZVJVFLR YBV UFRLYGZV M FVVH LD MFNVRLMCYLV JDBV"

def mapping(first, second):
    map = dict()
    for i in range(len(first)):
        if first[i] not in map:
            map[first[i]] = second[i]
    return map

def inverse(mapp):
    return {v: k for k, v in mapp.items()}

def convert(mapp1, mapp2):
    mapp = dict()
    for key in mapp1:
        mapp[key] = mapp2[mapp1[key]]
    return mapp

def solve(f1, f2, s1, s2, target):
    mapp1 = inverse(mapping(f1, f2))
    mapp2 = inverse(mapping(s1, s2))

    mapp = convert(mapp2, mapp1)

    print(mapp)


    result = ""
    for c in target:
        result += mapp[c]
    return result

if __name__ == "__main__":
    print(solve(f1, f2, s1, s2, target))
# Ignore and do not change the code above
