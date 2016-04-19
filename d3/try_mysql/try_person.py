'''
Created on Apr 18, 2016

@author: mzaleski
'''

from try_mysql.models import Person

if __name__ == '__main__':
    fred = Person(first_name = "fred", last_name = "smith", email = "fred@smith.com")
    fred.save()
    joe = Person(first_name = "joe", last_name = "smith", email = "joe@smith.com")
    joe.save()
    plist = Person.objects.all()
    print(plist)