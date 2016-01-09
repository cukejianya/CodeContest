n = int(raw_input())
phonebook = {}
for idx in range(n):
    person = raw_input()
    phonebook[person] = raw_input()

person = raw_input()
while person:
    if person in phonebook:
        print "%s=%s" % (person, phonebook[person])
    else:
        print "Not found"
    person = raw_input()
