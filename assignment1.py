import sys

# To convert a dict of engaged people in to list in python using some built in functions
def dictToList(dict):
    list = []
    list = [i for i in dict.items()]
    return list

# To convert a list of people in to dictionary in python using custom logic
def listToDict(list):
    dict = {}
    for sublist in list:
        inner_dict = {}
        for item in range(1, len(sublist)):
            inner_dict[sublist[item]] = "0"
        dict[sublist[0]] = inner_dict
    return dict

# To form the womens preference list 
def formPreferenceList(data):
    final_dict = {}
    for key, inner_dict in data.items():
        final_inner_dict = {}
        count = 1
        for subkey, value in inner_dict.items():
            final_inner_dict[subkey] = str(count)
            count += 1
        final_dict[key] = final_inner_dict

    print(final_dict)
    return final_dict

# To find the inverse list for the women's preferences
def formInverseList(data):
    sortedDict = {}
    for outer_key, inner_dict in data.items():
        sorted_inner_dict = {key: inner_dict[key] for key in sorted(inner_dict)}
        sortedDict[outer_key] = sorted_inner_dict

    return sortedDict

# To update the free men and free women status after every engagement
def updateLists(val1, val2):
    for key, value in freeMList.items():
        for subkey, subvalue in value.items():
            if(f"{subkey}" == val1):
                if(freeMList[key][subkey] == 1):
                        freeMList[key][subkey] = 0
                else:
                        freeMList[key][subkey] = 1
    for key, value in freeWList.items():
        for subkey, subvalue in value.items():
            if(f"{subkey}" == val2):
                if(freeWList[key][subkey] == 1):
                        freeWList[key][subkey] = 0
                else:
                        freeWList[key][subkey] = 1

# To check if a particular value exists in a dict or not
def checkValInEngPairs(val):
        key_list = list(engagedPair.keys())
        val_list = list(engagedPair.values())
        for i in key_list:
                if(i == val):
                    return 1
        for j in val_list:
                if(j == val):
                    return 1
        return 0

# To delete an engagement from stable pair
def deformEngagement(val):
    key_list = list(engagedPair.keys())
    val_list = list(engagedPair.values())
    position = val_list.index(val)
    key = key_list[position]
    if(val in engagedPair.values()):
        engagedPair.pop(key)
        updateLists(val, key)

# To check the preference values of a particular person from a other list
def checkPreference(val1, val2):
    print('Val 1 =>',val1)
    print('Val 2 =>',val2)
    for i, value in invList.items():
            if(val1 == i):
                for j, subvalue in enumerate(value):
                    if(subvalue == val1):
                        pref1 = j
                    if(subvalue == val2):
                        pref2 = j
    if(pref1 < pref2):
            return 1
    else:
            return 0
    
def obtainStablePairs(freeMList, freeWList):
    print('free Men list =>',freeMList)
    print('free women list =>',freeWList)
    while(len(engagedPair) != noOfPeople):
        for key, value in freeMList.items():
            for subkey, subvalue in value.items():
                if(f"{subvalue}" == "0" and (key not in engagedPair) and (checkValInEngPairs(subkey) != 1)):
                    engagedPair.update({key: subkey})
                    updateLists(f"{subkey}", key)
                if(f"{subvalue}" == "1" and (key not in engagedPair)):
                        if(checkPreference(key, subkey) == 1 and (checkValInEngPairs(subkey) == 1)):
                            deformEngagement(subkey)
                            engagedPair.update({key: subkey})
                            updateLists(f"{subkey}", key)


# To Get the input file name from the command line arguments
inputFileName = sys.argv[1]

# To Open the input file and read the contents of the input file
file = open(inputFileName, 'r')
data = file.readlines()
noOfPeople = int(data[0])

# To create empty lists to poulate them from the input file later
mList = [[] for i in range(noOfPeople)]
wList = [[] for i in range(noOfPeople)]
engagedPair = {}

# To read the men preference lists
for i in range(1, noOfPeople+1):
    mList[i-1] = data[i].split()

# To read the women preference lists
for j in range(noOfPeople+1, len(data)):
    wList[j-(noOfPeople + 1)] = data[j].split()

# print('Mens List =>',mList)
# print('womens List =>',wList)

freeMList = listToDict(mList)
freeWList = listToDict(wList)
prefList = formPreferenceList(freeWList)
invList = formInverseList(prefList)
obtainStablePairs(freeMList, invList)