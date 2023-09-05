import sys

# To Get the input file name from the command line arguments
inputFileName = sys.argv[1]

# To Open the input file and read the contents of the input file
file = open(inputFileName, 'r')
data = file.readlines()
noOfPeople = int(data[0])

# To read the men preference lists
for i in range(1, noOfPeople+1):
    print('men =>',data[i])

# To read the women preference lists
for j in range(noOfPeople+1, len(data)):
    print('women =>',data[j])