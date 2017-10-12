def gcd(num1, num2):
    gcd = 1
    count = 1
    num = min(num1, num2)
    if min(num1, num2) % max(num1, num2) == 0:
        return min(num1, num2)
    while count <= num:
        if num1 % count == 0 and num2 % count == 0:
            gcd = count
        count += 1
    return gcd

def restaurant():
    tc = input()
    while tc > 0:
        num1, num2 = map(int, raw_input().strip().split(' '))
        tc -= 1
        g_c_d = gcd(num1, num2)
        print (num1 * num2) / (g_c_d ** 2)
    
def main():
    restaurant()

if __name__ == "__main__":
    main()