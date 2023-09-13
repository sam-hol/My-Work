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
    # print('Man is =>',man)
    # print('woman is =>',woman)
    # print('Husband array =>',husband)
    # print('Wife array =>',wife)
    # print('Free Men are =>',freeMen)

# To do the men women matching
def beginMatching(man):
    # print('received man is =>',man)
    # print('Inverse is =>',inverse)
    for item, value in mensDict.items():
        if(item == man):
            for subKey, subValue in value.items():
                # print('Value =>',subKey)
                woman = subKey
                menPropCount[man] = menPropCount[man] + 1
                if(husband[woman] == None and wife[man] == None):
                    engagePair(man, woman)
                elif(husband[woman] != None and wife[man] == None):
                    # print('woman is engaged with =>',husband[woman])
                    currPartner = husband[woman]
                    propPartner = man
                    if(inverse[woman][propPartner] < inverse[woman][currPartner]):
                        # print('Prop partner is =>',propPartner)
                        engagePair(propPartner, woman)
                        wife[currPartner] = None
                        freeMen.append(currPartner)

def getItems(data):
    for item in data:
        return item

# To obtain the stable pairs using the gale shapely algorithm
def obtainStablePairs():
    # for (index, item) in enumerate(freeMen):
    #         print('\nCounter =>',index)
    #         print('MAN IS =>',item)
    # print('received data is =>',data)
    # freeMen.sort()
    # print('Free men =>',freeMen.sort())
    while(len(freeMen) != 0):
        # for item in freeMen:
            item = getItems(freeMen)
            # print('\nITEM =>',item)
            # print('Updated free men array is =>',freeMen)
            # print('\nCounter =>',index)
            # print('\nMAN IS =>',item)
            beginMatching(item)

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
# print('Husband =>',husband)
# print('wife =>',wife)
# print('Mens Preferences =>',mensDict)
# print('womens Preferences =>',womensDict)
inverse = createInverse(womensDict)
# print('Inverse is =>',inverse)
obtainStablePairs()
print('Couples are =>',wife)
# print('Couples are =>',husband)