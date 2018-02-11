import fuzzy
soundex = fuzzy.Soundex(4)
print(soundex('fuzzy'))
print(soundex('fizzy'))
print(soundex('fuzy'))
print(soundex('fissy'))

dmeta = fuzzy.DMetaphone()
print(dmeta('fuzzy'))

print(fuzzy.nysiis('fuzzy'))
