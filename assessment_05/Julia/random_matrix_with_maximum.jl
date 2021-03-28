# generate a random 2x4 matrix
# with values between 1 and 20
matrix = rand(1:20, 2, 4)

# determines the greates value within
# the previously generated matrix
max = maximum(matrix)

println("The randomly generated matrix is: ", matrix)
println("... and has the maximum: ", max)
