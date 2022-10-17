def max_num(x,y,z):
    return max([x,y,z])

print(max_num(1,2,3))

# Could also be written as below(not really a function though):

# numbers = [1,2,3]
# max_num = max(numbers)
# print(max_num)

def mult_list(list):
    if len(list) == 0:
        return 0
    mult = list[0]
    
    if len(list) > 1:
        for i in list[1:]:
            mult = mult * i

    return mult

print(mult_list([1,2,3]))



def rev_string(string):
    return string[::-1]

print (rev_string("python"))



def num_within(a,b,c):
  return a in range(b,c+1)

# True from given values:     
print(num_within(1,1,1))
# True from added c value:
print(num_within(2,1,3))
# False example:
print(num_within(1,2,3))



triangle = [[1], [1,1]]
def pascal(n):
	#your code here
    if n < 1:
        print("invalid")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)
pascal(1)
# '''
# output:
# 1
# '''

pascal(5)
# '''
# output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# '''                                                              