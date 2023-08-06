import math
def isprime(num):
    try:
        if num <= 1:
            return False
        if num == 2:
            return True
        if num>2 and num%2 == 0:
            return False
        sqrt_num = int(math.sqrt(num))
        for i in range(3, sqrt_num+1, 2):
            if num%i == 0:
                return False
        return True
    except:
        return None


def uptoprime(num):
    try:
        if num < 2:
            return None
        ans = []
        for i in range(num+1):
            x = isprime(i)
            if x:
                ans.append(i)
        return ans
    except:
        return None


def uptoprimecount(num):
    try:
        if num < 2:
                return 0
        count = 0
        for i in range(num+1):
            x = isprime(i)
            count += x
        return count
    except:
        return None

print(isprime(7))