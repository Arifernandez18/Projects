#import the necessary libraries to run the program
import stdarray
import stdrandom
import stdio

#THIS PROGRAM USES STANDARD INPUT IMPORTED FROM DATA/MOZART.TXT
#sets minuet measure to a 2d list of 11 rows and 16 columns
minuetMeasures= stdarray.create2D(11,16)

#populates the minuet lists with the values obtained from the standrad input
for i in range(11):
    for j in range(16):
        minuetMeasures[i][j]= stdio.readInt()

#sets trio to a 2D list of 6 rows and 16 columns
trioMeasures= stdarray.create2D(6,16)

#populates trio with values from standard input
for i in range(6):
    for j in range(16):
        trioMeasures[i][j]= stdio.readInt()

#rolls the dice twice, sums the number and selects the minuet that corresponds, according to its jth colum position
for j in range(16):
    num1 = stdrandom.uniformInt(1, 7)
    num2 = stdrandom.uniformInt(1, 7)
    i= num1+num2
    stdio.write(str(minuetMeasures[i-2][j])+" ") #writes the minuet to standard output
#rolls the die only once and selects the corresponding trio for its jth column position
for j in range(16):
    i= stdrandom.uniformInt(1,7)
    stdio.write(str(trioMeasures[i-1][j])+" ") #writes the trio to standard output

stdio.writeln() #writes a new line

...
