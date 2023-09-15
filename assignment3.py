'''
    @Author VAMSIKRISHNA NEELAM
    EMAIL ID: neelam.11@wright.edu
    UID: U01074399
    CS7200 FALL 2023 Assignment1
'''

# To import the packages from the python to perform various operations
import sys

# To convert a list of people in to dictionary in python using custom logic
def listToDict(list):
    dict = {}
    for sublist in list:
        inner_dict = {}
        count = 1
        for item in range(1, len(sublist)):
            inner_dict[sublist[item]] = count
            count = count + 1
        dict[sublist[0]] = inner_dict
    return dict

# To create free men list
def createFreeMen(data):
    count = 0
    for key,value in data.items():
        freeMen[count] = key
        count = count + 1
    return freeMen

# To Create numerlss for mens preference list
def createPreferences(original_dict):
    nameToNumeric = {}
    counter = 1
    for names in original_dict.values():
        for name in names:
            if name not in nameToNumeric:
                nameToNumeric[name] = counter
                counter += 1
    numericDict = {}
    for name, preferences in original_dict.items():
        newPreferences = [nameToNumeric[person] for person in preferences]
        numericDict[name] = newPreferences
    
    return numericDict

# To create inverse lists for women
def createInverse(data):
    result_dict = {}
    for key, values in data.items():
        inner_dict = {value: index for index, value in enumerate(values, 1)}
        result_dict[key] = inner_dict
    return result_dict

# To from the engagement
def engagePair(man, woman):
    husband[woman] = man
    wife[man] = woman
    freeMen.remove(man)

# To Retrieve the highest ranked woman on mens preference list
def getHighRankWoman(man):
    index = menPropCount[man]
    keys = list(mensDict[man].keys())
    return keys[index]

# To do the men women matching
def beginEngagements(man):
    # here we will pickup the highest preferred woman from man's preference list and check if she is free to engage, if she is free we will
    # engage both of them else if she is not free we will check her preference to the already engaged partner and proposed partner. If she 
    # prefers current partner more than proposed partner then proposing man will propsoe to the next highest ranked women, else woman prefers 
    # propsed partner over current partner then we will disengage the current partner and make that current partner free and engage the woman
    # to the new partner. This is how we are doing the here in the program.
    index = menPropCount[man]
    keys = list(mensDict[man].keys())
    woman = keys[index]
    menPropCount[man] = menPropCount[man] + 1
    if(husband[woman] == None and wife[man] == None):
        engagePair(man, woman)
    elif(husband[woman] != None and wife[man] == None):
        currPartner = husband[woman]
        propPartner = man
        if(inverse[woman][propPartner] < inverse[woman][currPartner]):
            engagePair(propPartner, woman)
            wife[currPartner] = None
            freeMen.append(currPartner)

# To return a man from free men array
def getMan(data):
    for man in data:
        return man

# To obtain the stable pairs using the gale shapely algorithm
def obtainStablePairs():
    # Checking for free men and if there are free men we will continue matching people
    while(len(freeMen) != 0):
            man = getMan(freeMen)
            beginEngagements(man)

# To create husband and wife arrays to engage the pairs
def createPairDicts(data):
    dict = {}
    for item, value in data.items():
        dict[item] = None
    return dict

# To create a counter which keeps tract track of men proposals count
def createMenProposalCount(data):
    counter = {}
    for item in data:
        counter[item] = 0
    return counter

# To Create a new file and write data to the output file
def writeToOutputFile(data):
    counter = 1
    if(inputFileName == "Input.txt"):
        outputFileName = "Output.txt"
    else:
        outputFileName = inputFileName.replace("In","Out")

    # To write data to output file     
    with open(outputFileName, 'w') as f:
        for key, value in data.items():
            if(counter != 1):
                f.writelines('\n')
            f.writelines([key, ' ', value])
            counter = counter + 1

# """Program starts from here.""""
if __name__ == "__main__":
    # To Get the input file name from the command line arguments
    if(len(sys.argv) > 2):
        print('Sorry You must enter only one argument ! You cannot enter more than one argument ! \nHave Good Luck next time !')
    elif(len(sys.argv) == 2):
        # To read the name of the input file from the Command line arguments
        inputFileName = sys.argv[1]
        # To Open the input file and read the contents of the input file
        file = open(inputFileName, 'r')
        data = file.readlines()
        noOfPeople = int(data[0])

        # To create empty lists to poulate them from the input file later
        mList = [[] for i in range(noOfPeople)]
        wList = [[] for i in range(noOfPeople)]
        freeMen = [0 for i in range(noOfPeople)]
        count = [[] for i in range(noOfPeople)]

        # To read the men preference lists
        for i in range(1, noOfPeople+1):
            mList[i-1] = data[i].split()

        # To read the women preference lists
        for j in range(noOfPeople+1, len(data)):
            wList[j-(noOfPeople + 1)] = data[j].split()

        mensDict = listToDict(mList)
        womensDict = listToDict(wList)
        freeMen = createFreeMen(mensDict)
        menPropCount = createMenProposalCount(freeMen)
        husband = createPairDicts(womensDict)
        wife = createPairDicts(mensDict)
        inverse = createInverse(womensDict)
        obtainStablePairs()
        writeToOutputFile(husband)
    else:
        print('Sorry You must enter atleast one argument ! You cannot start without arguments ! \nHave Good Luck next time !')