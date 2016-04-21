'''
Created on Apr 21, 2016

@author: mzaleski
'''

#    url(r'^person/first_name/[a-zA-Z]+/$', try_mysql.views.person, name="person_details"),

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
#     url(r'^$', try_mysql.views.index), # http://127.0.0.1:8000/
#     url(r'^persons/$', try_mysql.views.index), # http://127.0.0.1:8000/persons/
#     
#     #this url turns out weird. http://127.0.0.1:8000/person/first_name/a/?first_name=Mathew
#     url(r'^person/first_name/[a-zA-Z]+/$', try_mysql.views.person, name="person_details"),
#     
#     #I guess I have no idea what i'm doing? 
#     url(r'^person/first_name/?(P<first_name>[a-zA-Z]+)/$', try_mysql.views.person2),
# 
#     #REST framework works as I guessed it would    
#     url(r'^apipersons/$', views.LegacyPersonListRestView.as_view()),
#     url(r'^apiperson/?(P<first_name>[a-zA-Z]+)/$', views.LegacyPersonDetailsRestView.as_view()),
# ]

# I enter URL:
# note the x
# http://127.0.0.1:8000/personx/first_name/mathew/
# django error message says:
# Request URL: http://127.0.0.1:8000/personx/first_name/mathew/
# then, at the end it says "The current URL, personx/first_name/mathew/ didn't match

import re
if __name__ == '__main__':
    print("hello from futz-with-regexp-for-urls.py")
    #http://127.0.0.1:8000/person/first_name/a/?first_name=Mathew
    #person/first_name/first_name=Mathew
    #'^person/first_name/?(P<first_name>[a-zA-Z]+)/$'
    #
    #m = re.search(r'^foo/$', r"foo/")
    #m = re.search(r'^(foo)/$', r"foo/")
    #m = re.search(r'^(?P<first_name>[a-z]+)/$', r"foo/")
    m = re.search(r'^(?P<first_name>\w+)/$', r"Foo/")
    
#    m = re.search(
#                  "^personx/first_name/?(P<first_name>[a-zA-Z]+)/:",
#                  "^personx/first_name/mathew/:",
#                  r"^personx\w+/",
                   
#                   "personx/first_name/mathew/"
 #                  )
    if m:
        print("matched")
        print("first_name", m.group("first_name"))
    else:
        print("didn't match")
    