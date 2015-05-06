def prime(n):
    if n <= 0:
        return

    prime = []
    if n == 1:
        prime = []
    elif n == 2:
        prime = [2]
    else:
        prime = [2]
        for i in range(3, 100):
            j = 2
            while j < i:
                
                if i % j == 0:
                    break
                j += 1
            else:   
                prime.append(i)
                
    return prime


print prime(1)

print prime(100)
print prime(-8)
print prime(0)
print prime(99)

print len(prime(100))