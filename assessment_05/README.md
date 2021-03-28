# Data Science: EA5 - R and Julia
Assignment #5 to the module *Data Science* from *Computer Science and Media* course of study at *Beuth University of Applied Sciences*.

### Author
-----------
* **Name**<br />Dominic Schiller<br />
* **University**<br />Brandenburg University of Applied Sciences<br />
* **E-Mail**<br />dominic.schiller@th-brandenburg.de

---------
### Tasks
> 1. (R) <br /> Write a program to guess a number in between0 and 100.<br /><br />  
> 2. (R)<br />Analyse the **esoph** dataset. Can you derive some useful statements from it? Use *data()* to see all available datasets.<br /><br />
>3. (Julia)<br />Create a 2x4 two dimensional matrix with random floats in it and in the next step determine the biggest element.<br /><br />
>4. (Julia)<br />1. Create two matrices of the same layout and test if addition and subtraction of the matrix works as expected: C = A + B<br />2. Now compare matrix multiplication either this way A * B and this way A .* B. Whats the difference?!<br />3. What about matrix division with "/" or "\"?!<br />4. Create a 3x3 integer matrix A with useful numbers. Now try A+1, A-1, A*2, A/2.<br />5. Now multiply a 3x4 matrix with a suitable (4)vector.

-----
### Solutions
#### Task 1
Please have a look at this R script: [***guess_a_number.R***](https://github.com/dominicSchiller/DataScience_EA5_R_and_Julia/blob/develop/R/guess_a_number.R)

#### Task 2
The *esoph* data set consists of 88 records organized by 5 columns from a medical case-control study of esophageal cancer showing age-alcohol-tobacco combinations. <br/>
The most cancer cases (the last 4 records when ordered by cases: 43 from 88) occurred with people in an age between 55 and 74 who drunk between 40 and 119mg alcohol and smoked between 0-9 or 10-19mg tobacco a day. <br/><br />But literally, the most amount of cancer cases in sum occured with people in an age between 55 and 64 who drunk more than 40mg alcohol and additionally smoked more than 19mg tobacco a day in general. This leads to the result, that people who drunk and smoked a lot in combination, have the highest cancer risk.<br /><br />
Also, please have a look at the following R script used to analyze the esoph data set: [***esoph_exploration.R***](https://github.com/dominicSchiller/DataScience_EA5_R_and_Julia/blob/develop/R/esoph_exploration.R)

#### Task 3
Please have a look at this Julia script: [***random_matrix_with_maximum.jl***](https://github.com/dominicSchiller/DataScience_EA5_R_and_Julia/blob/develop/Julia/random_matrix_with_maximum.jl)

#### Task 4
Please have a look at this Julia script: [***matrix_operations.jl***](https://github.com/dominicSchiller/DataScience_EA5_R_and_Julia/blob/develop/Julia/matrix_operations.jl)
