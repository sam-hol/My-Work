import copy

# guyprefers ={
#             'Xavier' : ['Amy', 'Bertha', 'Clare'], 
#             'Yancey' : ['Bertha', 'Amy', 'Clare'],
#             'Zeus' : ['Amy', 'Bertha', 'Clare']
#     }
# galprefers = {
#             'Amy' : ['Yancey', 'Zeus', 'Xavier'], 
#             'Bertha' : ['Xavier', 'Yancey', 'Zeus'],
#             'Clare' : ['Xavier', 'Yancey', 'Zeus']
#     }

guyprefers ={
            'Albert' : ['Diane', 'Emily', 'Fergie'], 
            'Bradley' : ['Emily', 'Diane', 'Fergie'],
            'Charles' : ['Diane', 'Emily', 'Fergie']
    }
galprefers = {
            'Diane' : ['Albert', 'Bradley', 'Charles'], 
            'Emily' : ['Albert', 'Bradley', 'Charles'],
            'Fergie' : ['Albert', 'Bradley', 'Charles']
    }

# guyprefers ={
#             'Victor': ['Bertha', 'Amy', 'Diane', 'Erika', 'Clare'],
#             'Wyatt': ['Diane', 'Bertha', 'Amy', 'Clare', 'Erika'],
#             'Xavier': ['Bertha', 'Erika', 'Clare', 'Diane', 'Amy'],
#             'Yancey': ['Amy', 'Diane', 'Clare', 'Bertha', 'Erika'],
#             'Zeus': ['Bertha', 'Diane', 'Amy', 'Erika', 'Clare']
#     }
# galprefers = {
#             'Amy': ['Zeus','Victor', 'Wyatt', 'Yancey', 'Xavier'],
#             'Bertha': ['Xavier', 'Wyatt', 'Yancey', 'Victor', 'Zeus'],
#             'Clare': ['Wyatt', 'Xavier', 'Yancey', 'Zeus', 'Victor'],
#             'Diane': ['Victor', 'Zeus', 'Yancey', 'Xavier', 'Wyatt'],
#             'Erika': ['Yancey', 'Wyatt', 'Zeus', 'Xavier', 'Victor']
#     }

guys = sorted(guyprefers.keys())
gals = sorted(galprefers.keys())


def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = galprefers[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = guyprefers[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = guyprefers[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guysgirl))
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = galprefers[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, girlsguy))
                return False
    return True

def matchmaker():
    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
            print("  %s and %s" % (guy, gal))
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged


print('\nEngagements:')
engaged = matchmaker()

print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')

print('\n\nSwapping two fiances to introduce an error')
engaged[gals[0]], engaged[gals[1]] = engaged[gals[1]], engaged[gals[0]]
for gal in gals[:2]:
    print('  %s is now engaged to %s' % (gal, engaged[gal]))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')