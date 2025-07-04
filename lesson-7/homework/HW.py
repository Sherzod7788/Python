## Homework Lesson 7
# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

def is_prime(n):
    if n <= 1:
        return False  # 0 va 1 tub emas

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))


# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum(k):
    return sum(int(digit) for digit in str(abs(k)))  

print(digit_sum(24)) 
print(digit_sum(502))  
print(digit_sum(-123)) 

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def powers_of_two(N):
    k = 0
    result = []
    while 2 ** k <= N:
        result.append(2 ** k)
        k += 1
    return result

print(powers_of_two(20))   
print(powers_of_two(1))    
print(powers_of_two(100))  

