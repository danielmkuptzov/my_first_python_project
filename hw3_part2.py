def get_palindrom_dict(str):
    palindrom_dict = {}
    palindrom_dict[1] = [str[j] for j in len(str)]
    palindrom_dict[2] = [str[i:i+2] for i in range(len(str)-1) if str[i] == str[i+1]]
    even = [ i  for i in range(len(str)) if (i >= 4 and i % 2 == 0)]
    for i in even:
        polindroms = []
        for j in range(len(str)-i):
            if (str[j: j+(i/2)+1] == str[j+(i/2): j+i+1]):
                polindroms.append(str[j:j+i+1])
        palindrom_dict[i] = polindroms
    return palindrom_dict

def check_match(str):
