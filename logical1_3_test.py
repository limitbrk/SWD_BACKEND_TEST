"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
โดยห้ามใช้ math.factorial 
เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
"""
def main():
    print("หาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial.")
    num = int(input("กรอกเลขของคุณ: "))
    print(f'{num} มีเลข 0 ต่อท้าย {find_trail_zero(num)} ตัว')

# src: https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
def find_trail_zero(n: int) -> int:
    if(n < 0):
        return -1
 
    # Initialize result
    count = 0
 
    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n
 
    return count

main()
    