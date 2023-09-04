# to open the input file and read all the data
# f = open("input.txt", "r")
# print(f.read())

# for i in f:
#     if(i == 1):
#         n = f(i)
#         print("no of men & women: ",n)
#     if(i == 2):
#         m = f(i)
#         print("no of pairs: ",m)

n = 2
freeMList = {}
freeWList = {}
engagedPair = {}

# to convert a list of people in to dictionary in python using custom logic
def listToDict(list):
    # print('List is =>',list)
    dict = {}

    for sublist in list:
        inner_dict = {}
        for item in range(1, len(sublist)):
            inner_dict[sublist[item]] = "0"
        dict[sublist[0]] = inner_dict
    # print("new dict is =>",dict)

    return dict

# To form the stable pair of men and women
def stablePair(key, value):
    # print('\nKey =>', key)
    # print('Val =>', value)
    engagedPair.update({key: value})
    # print('Updated engaged pair =>',engagedPair)
    # print('Engaged pair =>',engagedPair)

# To update the free men and free women status after every engagement
def updateLists(val1, val2):
    # print('Value 1 is =>',val1)
    # print('Value 2 is =>',val2)
    for key, value in freeMList.items():
        # if isinstance(value, dict):
            for subkey, subvalue in value.items():
                # print(f"{key}.{subkey} = {subvalue}")
                # print(f"{subvalue}" == "1")
                # if(f"{key}.{subkey}" == 0):
                if(f"{subkey}" == val1):
                    if(freeMList[key][subkey] == 1):
                            freeMList[key][subkey] = 0
                    else:
                            freeMList[key][subkey] = 1
        # else:
        #     print(f"{key} = {value}")
    for key, value in freeWList.items():
        # if isinstance(value, dict):
            for subkey, subvalue in value.items():
                # print(f"{key}.{subkey} = {subvalue}")
                # print(f"{subvalue}" == "1")
                # if(f"{key}.{subkey}" == 0):
                # print('Subkey from free womens list =>',subkey)
                if(f"{subkey}" == val2):
                    if(freeWList[key][subkey] == 1):
                            freeWList[key][subkey] = 0
                    else:
                            freeWList[key][subkey] = 1
        # else:
        #     print(f"{key} = {value}")
    # print('Updated mlist =>',freeMList)
    # print('Updated wlist =>',freeWList)

# to delete an engagement from stable pair
def deformEngagement(val):
    # print('val in deform engagement =>',val)
    if('Alice' in engagedPair):
        engagedPair.pop('Alice')
    # print('Engaged pairs now =>',engagedPair)

# to get the preference values of a particular person from a certain list
def getPreferenceValues(val):
    for i, value in freeWList.items():
            for j, subvalue in enumerate(value):
                if(subvalue == val):
                    # print(' ',subvalue,'index is => ',j)
                    return j
            

def checkPreference(val1, val2):
    # print('Check preference value is =>',val1)
    # print('Check preference value is =>',val2)
    # print('Free Men List =>',freeMList)
    # print('Free Women List =>',freeWList)
    if(getPreferenceValues(val2) == 0):
            return 1

def checkValInDict(val):
        for key, value in engagedPair.items():
            if value == val:
                    # print('found')
                    return 1
            else:
                    # print('Not found')
                    return 0

def obtainStablePairs(wList, mList):
    # print('\nIn obtain stable pairs')
    # for item in 
    # print('LEN OF ENGAGED PAIR =>',len(engagedPair))
    while(len(engagedPair) != n):
            for key, value in mList.items():
                # if isinstance(value, dict):
                    for subkey, subvalue in value.items():
                        # print('\nKey is =>',key)
                        # print('Value is =>',value)
                        # print('Sub Key is =>',subkey)
                        # print('Sub Value is =>',subvalue)
                        # print(f"\n{key}.{subkey} = {subvalue}")
                        # if(f"{key}.{subkey}" == 0):
                        if(f"{subvalue}" == "0" and (key not in engagedPair) and (checkValInDict(subkey) != 1)):
                        # if((key not in engagedPair)):
                            stablePair(key, f"{subkey}")
                            updateLists(f"{subkey}", key)
                        # print('\nTRUTH VALUE =>',f"{subvalue}" == "1" and (checkValInDict(subkey) != 1))
                        if(f"{subvalue}" == "1" and (key not in engagedPair)):
                            # print('is highest pref =>',checkPreference(f"{subkey}", key) == 1)
                            if(checkPreference(f"{subkey}", key) == 1 and (checkValInDict(subkey) == 1)):
                                # if(key in engagedPair):
                                deformEngagement(key)
                                # print('Engaged pairs now =>',engagedPair)
                                updateLists('Xavier', 'Alice')
                                stablePair(key, f"{subkey}")
                                updateLists(f"{subkey}", key)
                # else:
                #     print(f"{key} = {value}")

def compareStability(pairList):
    print('\nIn compare stability function')
    print('PairList =>',pairList)

# 2 people
# Output (Alice, Xavier), (Carol, Zeus)
mList = [
            ['Alice', 'Xavier', 'Zeus'], 
            ['Carol', 'Zeus', 'Xavier']
        ]

wList = [
            ['Xavier', 'Alice', 'Carol'], 
            ['Zeus', 'Alice', 'Carol']
        ]

# Swapped Alice & Carol for Xavier,
# Zeus & Xavier for Caol
# Output (Carol, Xavier), (Alice, Zeus)
# mList = [
#             ['Alice', 'Xavier', 'Zeus'], 
#             ['Carol', 'Xavier', 'Zeus']
#         ]

# wList = [
#             ['Xavier', 'Carol', 'Alice'], 
#             ['Zeus', 'Alice', 'Carol']
#         ]

# 3 people
# mList = [
#             ['Xavier', 'Amy', 'Bertha', 'Clare'], 
#             ['Yancey', 'Bertha', 'Amy', 'Clare'],
#             ['Zeus', 'Amy', 'Bertha', 'Clare']
#         ]

# wList = [
#             ['Amy', 'Yancey', 'Xavier', 'Zeus'], 
#             ['Bertha', 'Xavier', 'Yancey', 'Zeus'],
#             ['Clare', 'Xavier', 'Yancey', 'Zeus']
#         ]

# Xavier and Zeus swapped for Amy
# output (Xavier, Bertha), (Yancey, Amy), (Zeus, Clare)
# mList = [
#             ['Xavier', 'Amy', 'Bertha', 'Clare'], 
#             ['Yancey', 'Bertha', 'Amy', 'Clare'],
#             ['Zeus', 'Amy', 'Bertha', 'Clare']
#         ]

# wList = [
#             ['Amy', 'Yancey', 'Zeus', 'Xavier'], 
#             ['Bertha', 'Xavier', 'Yancey', 'Zeus'],
#             ['Clare', 'Xavier', 'Yancey', 'Zeus']
#         ]

# 5 people
# mList = [
#             ['Victor', 'Bertha', 'Amy', 'Diane', 'Erika', 'Clare'],
#             ['Wyatt', 'Diane', 'Bertha', 'Amy', 'Clare', 'Erika'],
#             ['Xavier', 'Bertha', 'Erika', 'Clare', 'Diane', 'Amy'],
#             ['Yancey', 'Amy', 'Diane', 'Clare', 'Bertha', 'Erika'],
#             ['Zeus', 'Bertha', 'Diane', 'Amy', 'Erika', 'Clare']
#         ]

# wList = [
#             ['Amy', 'Zeus','Victor', 'Wyatt', 'Yancey', 'Xavier'],
#             ['Bertha', 'Xavier', 'Wyatt', 'Yancey', 'Victor', 'Zeus'],
#             ['Clare', 'Wyatt', 'Xavier', 'Yancey', 'Zeus', 'Victor'],
#             ['Diane', 'Victor', 'Zeus', 'Yancey', 'Xavier', 'Wyatt'],
#             ['Erika', 'Yancey', 'Wyatt', 'Zeus', 'Xavier', 'Victor']
#         ]

# 2 people
pairList = [
                ['Alice', 'Xavier'], 
                ['Carol', 'Zeus']
            ]

# pairList = [
#                 ['Carol', 'Xavier'], 
#                 ['Alice', 'Zeus']
#             ]

freeWList = listToDict(wList)
freeMList = listToDict(mList)
obtainStablePairs(freeWList, freeMList)
print('\nEngaged pair =>',engagedPair, "\n")
# compareStability(pairList)