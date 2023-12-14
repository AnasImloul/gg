def create_mapping(source, target):
    char_mapping = dict()
    for i in range(len(source)):
        if source[i] not in char_mapping:
            char_mapping[source[i]] = target[i]
    return char_mapping

def inverse_mapping(mapping):
    return {value: key for key, value in mapping.items()}

def apply_mapping(input_str, char_mapping):
    result = ""
    for char in input_str:
        result += char_mapping[char]
    return result

def solve_cipher():
    f1 = "JACKIE WILL BUDGET FOR THE MOST EXPENSIVE ZOOLOGY EQUIPMENT"
    f2 = "DAOFJK XJCC PVQNKW STH WUK RTBW KYZKLBJGK MTTCTNI KEVJZRKLW"
    s1 = "ZELDA MIGHT FIX THE JOB GROWTH PLANS VERY QUICKLY ON MONDAY"
    s2 = "XSFIY TANBD QAO DBS MPR NJPLDB GFYCK USJW HEAZVFW PC TPCIYW"
    target = "RDJV VZVJVFLR YBV UFRLYGZV M FVVH LD MFNVRLMCYLV JDBV"

    first_mapping = inverse_mapping(create_mapping(f1, f2))
    second_mapping = inverse_mapping(create_mapping(s1, s2))

    combined_mapping = dict()
    for key in first_mapping:
        combined_mapping[key] = second_mapping[first_mapping[key]]

    print(combined_mapping)

    result = apply_mapping(target, combined_mapping)
    return result

if __name__ == "__main__":
    print(solve_cipher())
