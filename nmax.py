f = open('nmax.inp','r')
g = open('nmin.out','w')



string = f.readline()
newstring = ''.join(i for i in string if i.isdigit())
n = len(newstring) - 5

stack = []
removed = 0

for digit in newstring:
    while stack and removed < n and stack[-1] < digit:
        stack.pop()
        removed += 1
    stack.append(digit)

stack = stack[:-n] if removed < n else stack

largest_num = int(''.join(stack))
print("Số lớn nhất sau khi xóa {} chữ số là: {}".format(n, largest_num))