# helper functions
# read input from the user
readGuess <- function()
{ 
  n <- readline(prompt="Enter your guessed number: ")
  # checks if the user entered a valid integer
  if(!grepl("^[0-9]+$",n))
  {
    return(readGuess())
  }
  return(as.integer(n))
}

# main starting point of the program
targetNumber <- round(runif(1) * 100, digits = 0)
guess <- -1

cat("Guess a number between 0 and 100.\n")

while(guess != targetNumber)
{ 
  guess <- readGuess()
  if (guess == targetNumber)
  {
    cat("Congratulations,", targetNumber, "is right.\n")
  }
  else if (guess < targetNumber)
  {
    cat("The number is bigger! ... try again ...\n")
  }
  else if(guess > targetNumber)
  {
    cat("The number is smaller! ... try again ...\n")
  }
}