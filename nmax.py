# Mở file đầu vào để đọc và file đầu ra để ghi
f = open('nmax.inp', 'r')
g = open('nmin.out', 'w')

# Đọc dòng đầu tiên từ file đầu vào và loại bỏ các ký tự không phải số
string = f.readline()
newstring = ''.join(i for i in string if i.isdigit())

# Tính số lượng chữ số cần loại bỏ
n = len(newstring) - 5

# Khởi tạo danh sách và biến đếm
stack = []
removed = 0

# Duyệt qua từng chữ số trong newstring
for digit in newstring:
    # Nếu stack không rỗng và số chữ số đã loại bỏ chưa đủ và chữ số hiện tại lớn hơn chữ số cuối cùng trong stack
    while stack and removed < n and stack[-1] < digit:
        removed += 1    # Tăng số chữ số đã loại bỏ lên 1
        stack = stack[:-1]  # Loại bỏ chữ số cuối cùng trong stack
    stack.append(digit)  # Thêm chữ số hiện tại vào stack

# Nếu số chữ số đã loại bỏ chưa đủ, loại bỏ thêm chữ số để chỉ giữ lại 5 chữ số lớn nhất
while removed < n:
    removed += 1
    stack = stack[:-1]

# Ghép các chữ số lại để tạo thành số lớn nhất
largest_num = int(''.join(stack))

# In ra kết quả
print("Số lớn nhất sau khi xóa {} chữ số là: {}".format(n, largest_num))

# Ghi kết quả vào file đầu ra
g.write(str(largest_num))

# Đóng file
f.close()
g.close()
