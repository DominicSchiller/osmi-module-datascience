# 3x3 matrix A
a = [5 -3 11; 5 6 22; 8 19 0]
println("Matrix A = ", a)

# 3x3 matrix B
b = [12 3 -4; 5 16 9; 8 -3 4]
println("Matrix B = ", b)

# Task 1: addition and subtraction
println("\n============ Task 1: matrix addition and subtraction ============\n")
# expected results
c_add_exp = [17 0 7; 10 22 31; 16 16 4]
c_sub_exp = [-7 -6 15; 0 -10 13; 0 22 -4]

c_add = a + b
print("A+B = ", c_add)
c_sub = a - b
print("A-B = ", c_sub)

println("Does addition work as expected? ", c_add == c_add_exp)
println("Does subtracttion work as expected? ", c_sub == c_sub_exp)

# Task 2: matrix multiplications
println("\n============ Task 2: matrix multiplication ============\n")
c_mult_ab = a * b
c_mult_ba = b * a

println("A * B = ", c_mult_ab)
println("B * A = ", c_mult_ba)
println("==> A*B != B*A because rows from the first matrix will be multiplied with the columns from the seconds matrix. If those rows and columns are in different order, different values will result.")

# Task 3: matrix division
println("\n============ Task 3: matrix division ============\n")
c_diff_1 = a / b
println("A/B = ", c_diff_1)
c_diff_2 = a \ b
println("A\\B = ", c_diff_2)
println("==> A/B != A\\B, because the '\\' operator divides inverse which means that A\\B == B/A")

# Task 4: Single matrix operations
println("\n============ Task 4: single matrix operations ============\n")
a_incr = a + 1
println("A+1 = ", a_incr)
a_decr = a - 1
println("A-1 = ", a_decr)
a_double = a * 2
println("A*2 = ", a_double)
a_half = a / 2
println("A/2 = ", a_half)

# Task 5: matrix and vector multiplication
println("\n============ Task 5: matrix and vector multiplication ============\n")
# 3x4 matrix D
d = [5 -3 11 5; 6 22 8 19; 1 5 8 11]
println("Matrix D = ", d)
# 4x vector V
v = [2, 6, 9, 12]
println("Vector V = ", v)
result = d * v
println("D*V = ", result)
println("==> The result from the multiplication of a 3x4 matrix with a 4-dimensional vector is a 3-dimensional vector!")
