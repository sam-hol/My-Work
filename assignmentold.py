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

freeMList = {}
freeWList = {}
engagedPair = {}

# To convert a dict of engaged people in to list in python using some built in functions
def dictToList(dict):
    print(engagedPair)
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
    print('Value 1 in update lists is =>',val1)
    print('Value 2 in update lists is =>',val2)
    for key, value in freeMList.items():
        for subkey, subvalue in value.items():
            # print(f"{key}.{subkey} = {subvalue}")
            if(f"{subkey}" == val1):
                if(freeMList[key][subkey] == 1):
                        freeMList[key][subkey] = 0
                else:
                        freeMList[key][subkey] = 1
    for key, value in freeWList.items():
        for subkey, subvalue in value.items():
            # print(f"{key}.{subkey} = {subvalue}")
            # print('Subkey from free womens list =>',subkey)
            if(f"{subkey}" == val2):
                if(freeWList[key][subkey] == 1):
                        freeWList[key][subkey] = 0
                else:
                        freeWList[key][subkey] = 1
    # print('\nUpdated mlist =>',freeMList)
    # print('Updated wlist =>',freeWList)

# To delete an engagement from stable pair
def deformEngagement(val):
    key_list = list(engagedPair.keys())
    val_list = list(engagedPair.values())
    position = val_list.index(val)
    key = key_list[position]
    print('in deform engagement =>',key)
    if(val in engagedPair.values()):
        engagedPair.pop(key)
        updateLists(val, key)

# To get the preference values of a particular person from a certain list
def getPreferenceValues(val, name):
    # print(freeWList.items())
    print(name)
    for i, value in freeWList.items():
            # print('key =>', i)
            # print('value =>', value)
            if(name == i):
                for j, subvalue in enumerate(value):
                    if(subvalue == val):
                        # print(' ',subvalue,'index is => ',j)
                        return j

def checkPreference(val1, val2, name):
    print('Check preference value 1 is =>',val1)
    print('Check preference value 2 is =>',val2)
    # print('Name in check pref =>',name)
    # print('Free Men List =>',freeMList)
    # print('Free Women List =>',freeWList)
    pref1 = getPreferenceValues(val1, name)
    pref2 = getPreferenceValues(val2, name)
    print('Pref 1 =>',pref1)
    print('Pref 2 =>',pref2)
    if(pref1 < pref2):
            print('high preference')
            return 1
    else:
            print('Low Preference')
            return 0

def checkValInDict(val):
        key_list = list(engagedPair.keys())
        val_list = list(engagedPair.values())
        for i in key_list:
                if(i == val):
                    print('found')
                    return 1
        for j in val_list:
                if(j == val):
                    print('found')
                    return 1
        return 0
        # print('engaged pair is =>',engagedPair)
        # print('Val in checkdict =>',val)
        # for key,value in engagedPair.items():
        #     print('Key is =>',key,', Value is =>',val)
        #     print(key == val or value == val)
        #     if(val == key):
        #             print('found')
        #             return 1
        #     if(val == value):
        #             print('found')
        #             return 1
        #     else:
        #             print('Not found')
        #             return 0

def getPartner(val):
        print(engagedPair)
        key_list = list(engagedPair.keys())
        val_list = list(engagedPair.values())
        position = val_list.index(val)
        key = key_list[position]
        return key

def obtainStablePairs(wList, mList):
    # print('\nIn obtain stable pairs')
    # print('LEN OF ENGAGED PAIR =>',len(engagedPair))
    while(len(engagedPair) != n):
        print('Enagged pairs =>',engagedPair)
        print('Free men list =>',freeMList)
        print('Free women list =>',freeWList)
        for key, value in mList.items():
            for subkey, subvalue in value.items():
                # print('\nKey is =>',key)
                # print('Value is =>',value)
                # print('Sub Key is =>',subkey)
                # print('Sub Value is =>',subvalue)
                print(f"\n{key}.{subkey} = {subvalue}")
                if(f"{subvalue}" == "0" and (key not in engagedPair) and (checkValInDict(subkey) != 1)):
                    stablePair(key, f"{subkey}")
                    updateLists(f"{subkey}", key)
                # print('\nTRUTH VALUE =>',f"{subvalue}" == "1" and (checkValInDict(subkey) != 1))
                if(f"{subvalue}" == "1" and (key not in engagedPair)):
                    partner = getPartner(subkey)
                    # print(partner)
                    # print('engaged pair =>',engagedPair)
                    # print('TRUTH VALUE =>',(checkPreference(key, partner) == 1 and (checkValInDict(subkey) == 1)))
                    if(checkPreference(key, partner, subkey) == 1 and (checkValInDict(subkey) == 1)):
                        # if(key in engagedPair):
                        deformEngagement(subkey)
                        print('Engaged pairs now =>',engagedPair)
                        stablePair(key, f"{subkey}")
                        updateLists(f"{subkey}", key)

def compareStability(couplesList, pairList):
    print('\nIn compare stability function')
    print('PairList =>',pairList)
    print('Are both the same ?', set(couplesList) == set(pairList))

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
# Output (Xavier, Amy), (Yancey, Bertha), (Zeus, Clare) or 
# (Yancey, Amy), (Xavier, Bertha), (Zeus, Clare)
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

# OUTPUT (A, X), (B, Y), (C, Z) if m, w
# (X, A), (Y, B), (Z, C) w, m
# mList = [
#             ['A', 'X', 'Y', 'Z'],
#             ['B', 'Y', 'Z', 'X'],
#             ['C', 'Z', 'X', 'Y']
#         ]

# wList = [
#             ['X', 'A', 'B', 'C'],
#             ['Y', 'B', 'C', 'A'],
#             ['Z', 'C', 'A', 'B']
#         ]

# OUTPUT (A, X), (B, Y), (C, Z) if m, w
# (X, A), (Y, B), (Z, C) w, m
# mList = [
#             ['A', 'X', 'Y', 'Z'],
#             ['B', 'X', 'Y', 'Z'],
#             ['C', 'X', 'Y', 'Z']
#         ]

# wList = [
#             ['X', 'A', 'B', 'C'],
#             ['Y', 'A', 'B', 'C'],
#             ['Z', 'A', 'B', 'C']
#         ]

# 5 people
# Output (Victor, Amy), (Wyatt, Clare), (Xavier, Bertha), (Yancey, Erika), (Zeus, Diane)
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

# 10 people
# mList = [
#             ['abe', 'abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
#             ['bob', 'cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
#             ['col', 'hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
#             ['dan', 'ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
#             ['ed', 'jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
#             ['fred', 'bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
#             ['gav', 'gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
#             ['hal', 'abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
#             ['ian', 'hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
#             ['jon', 'abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']
#         ]

# wList = [
#             ['abi', 'bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
#             ['bea', 'bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
#             ['cath', 'fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
#             ['dee', 'fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
#             ['eve', 'jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
#             ['fay', 'bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
#             ['gay', 'jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
#             ['hope', 'gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
#             ['ivy', 'ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
#             ['jan', 'ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']
#         ]

# 2 people
pairList = [
                ['Alice', 'Zeus'], 
                ['Carol', 'Xavier']
            ]

# pairList = [
#                 ['Carol', 'Xavier'], 
#                 ['Alice', 'Zeus']
#             ]

n = len(mList)
freeWList = listToDict(wList)
freeMList = listToDict(mList)
obtainStablePairs(freeWList, freeMList)
couplesList = dictToList(engagedPair)
print('\nCouples List =>',couplesList, "\n")
list1 = couplesList
list2 = pairList
print(all(list1[i][j] == list2[i][j] for i in range(len(list1)) for j in range(len(list1[0]))))
# compareStability(couplesList, set(pairList))