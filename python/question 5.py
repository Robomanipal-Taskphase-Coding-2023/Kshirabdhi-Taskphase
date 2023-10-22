
 
def Decimal(binary, i = 0):
 
   
    n = len(binary) 
    if (i == n - 1) :
        return int(binary[i]) - 0
    
    return (((int(binary[i]) - 0) << (n - i - 1)) +
                        Decimal(binary, i + 1))
if __name__ == "__main__" :
     
    binary = "1010"
    print(Decimal(binary))