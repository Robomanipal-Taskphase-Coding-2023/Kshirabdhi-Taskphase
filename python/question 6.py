strings="aaabbbbccccc"
def replace(strings, ch):
    new_str = []
    l = len(strings)
     
    for i in range(len(strings)):
        if (strings[i] == ch and i != (l-1) and
           i != 0 and strings[i + 1] != ch and strings[i-1] != ch):
            new_str.append(s[i])
             
        elif strings[i] == ch:
            if ((i != (l-1) and strings[i + 1] == ch) and
               (i != 0 and strings[i-1] != ch)):
                new_str.append(strings[i])
                 
        else:
            new_str.append(strings[i])
         
    return ("".join(i for i in new_str))

char = 'c'
print(replace(strings, char))
