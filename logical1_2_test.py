"""
2. เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python 
เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 
โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
"""
def main():
    print("Find maximum index.")
    nums = [int(i) for i in input("Enter your numbers(no space): ")]
    print("Your nums array is: ",nums)
    print("Your result is: ", max_index(nums))

# src: https://stackoverflow.com/a/14448729
def max_index(array = []) -> int:
    max_index = None
    max_value = None
    i = 0
    for n in array:
        if max_value is None or array[i] > max_value: 
            max_index = i
            max_value = array[i]
        i += 1
    return max_index

main()
    