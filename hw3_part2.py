def get_pal_new(str):
    dc = {num + 1: [str[i:i + num + 1] for i in range(len(str) - num)
                    if str[i:i + num + 1] == str[i:i + num + 1][::-1]] for num in range(len(str))}
    return {num + 1: dc[num + 1] for num in range(len(str)) if len(dc[num+1]) > 0}

def check_match(str):
    if(len(str) ==0):
        return True
    fir_str = str[1::2]
    sec_str = str[2::2]
    for i in range(len(fir_str)):
        if(fir_str.replace(fir_str[i],sec_str[i]) == sec_str):
            return True
    return False