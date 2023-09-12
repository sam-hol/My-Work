import sys

# To convert a list of people in to dictionary in python using custom logic
def listToDict(list):
    dict = {}
    for sublist in list:
        innerList = [[] for i in range(1, noOfPeople+1)]
        for item in range(1, len(sublist)):
            innerList[item-1] = sublist[item]
        dict[sublist[0]] = innerList
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
def engagePair(man, woman, manNumber):
    husband[woman] = man
    wife[manNumber] = woman
    freeMen.remove(man)
    print('Man is =>',man)
    print('woman is =>',woman)
    print('Free Men are =>',freeMen)

# To obtain the stable pairs using the gale shapely algorithm
def obtainStablePairs(data):
    print('received data is =>',data)
    # while(len(freeMen) > 0):
    for man in freeMen:
            # print('free man is =>',man)
            for i in range(noOfPeople):
                # print('man particular preference =>',data[man][i])
                # print('husband of i is =>',husband[i])
                print('value 1 =>',husband[data[man][i] - 1], 'value 2 =>',wife[husband[data[man][i] - 1]])
                print('Truth value 2 =>',husband[data[man][i] - 1] == 0)
                if(husband[data[man][i] - 1] not in wife[husband[data[man][i] - 1]] and husband[data[man][i] - 1] == 0):
                    print('Woman is free and we will engage them !')
                    engagePair(man, data[man][i], husband[data[man][i] - 1])


# To Get the input file name from the command line arguments
inputFileName = sys.argv[1]

# To Open the input file and read the contents of the input file
file = open(inputFileName, 'r')
data = file.readlines()
noOfPeople = int(data[0])

# To create empty lists to poulate them from the input file later
mList = [[] for i in range(noOfPeople)]
wList = [[] for i in range(noOfPeople)]
freeMen = [0 for i in range(noOfPeople)]
husband = [0 for i in range(noOfPeople)]
wife = [0 for i in range(noOfPeople)]
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
mensPreferences = createPreferences(mensDict)
womensPreferences = createPreferences(womensDict)
print('Mens Preferences =>',mensPreferences)
print('womens Preferences =>',womensPreferences)
inverse = createInverse(womensPreferences)
print('Inverse is =>',inverse)
obtainStablePairs(mensPreferences)