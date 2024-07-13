#bai 1: 2,6,12,20,30, 
#Đáp số: 42
#Giải thích: các số lần lượt sẽ tăng thêm 1 giá trị chẵn tăng dần. Bắt đầu ở số 2 và tăng thêm 4 
# --> 2+4 = 6
# --> 6 + 6 (số chắn tiếp theo) = 12
# --> 12 + 8 (số chẵn liền sau 6) = 20
# --> 20 + 10 (số chẵn liền sau 8) = 30
# --> Số chắn tiếp theo là 12. Vậy ta lấy số trước là 30 + 12 = 42


#Bài 2:
#Đáp số: 20*(1-10%)^3 = 14.580000000000002
#print("Đáp án câu 2: ",20*pow((1-0.1),3))
#Giải thích: Giá trị của xe năm sau sẽ = giá trị của xe năm đang xét - (giá trị của năm đang xét * 10%). Và sau n năm ta có công thức:
# giá trị của xe sau n năm = giá trị của xe năm đầu * (1 - số phần trăm giảm)^n

#Bài 3:
#Đáp án: 10 (Tổ hợp C của 2 ,5)
#Giải thích: vì khi bắt tay phải chọn ra 2 trong 5 người. Và mỗi người không bắt tay những người mình đã bắt tay.
# Người thứ nhất bắt tay với 4 người còn lại
# Người thứ hai bắt tay với 3 người còn lại (trừ người 1)
# ...............................................
# Công thức: (n!) / (k!*(n-k)!) => kết quả của các trường hợp (không quan tâm đến thứ tự) có thể xảy ra.

def factorial(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

print(factorial(5))

def check_palindrome(s):
    if(s == s[::-1]):
        print(s, "là chuỗi đối xứng")
    else:
        print(s, "không phải là chuỗi đối xứng")

check_palindrome("tomato")


def sort_list(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if(nums[j] < nums[i]):
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(sort_list([1,5,8,3,4,2])) 