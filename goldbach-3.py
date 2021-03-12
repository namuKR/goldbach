# Script by ast.08. Github @namuKR

# Script for getting sum of 3 prime numbers.

number = 26 # a(prime number) + b(prime number) + c(prime number) = 26

for i in range(2, number-3):
    for v in range(2, number-3):
        for _ in range(2, number-3):
            for i_ in range(2, int(i/2)+1):
                if (i % i_) == 0:
                    break
            else:
                i__ = i
                
                for i_ in range(2, int(v/2)+1):
                    if (v % i_) == 0:
                        break
                else:
                    v__ = v
                    for i_ in range(2, int(_/2)+1):
                        if (_ % i_) == 0:
                            break
                    else:
                        a__ = _
                        if (i__ + v__ + a__ == 26):
                            print(i__, v__, a__)
                    
