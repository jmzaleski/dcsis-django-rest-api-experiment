# Create your views here.
from django.shortcuts import render, get_object_or_404
from try_mysql.models import Person
     
def index(request):
    people_list = Person.objects.all()
    # now return the rendered template
    # is the try_mysql dir needed?? templates wind up in:
    # /Users/mzaleski/Dropbox/CSC/eclipse-workspace-teaching/d3/try_mysql/templates
    # on the other hand, a bunch of refs to just "index.html" is bound to be confusing too(?)
    # (the dictionary is added to the context the template is rendered with)
    return render(request, 'try_mysql/index.html', {'people_list': people_list})
 
def person(request): #, first_name):
    # TODO: i wimpled out from parsing the URL properly
    first_name = request.GET.get("first_name")
    print("first_name",first_name)
    p = get_object_or_404(Person, first_name=first_name)
    # now return the rendered template
    return render(request, 'try_mysql/person.html', {'person': p})

def person2(request,first_name=None): #, first_name):
    #grrrrrrr can't form the URL for this guy
    print("person2: first_name",first_name)
    p = get_object_or_404(Person, first_name=first_name)
    # now return the rendered template
    return render(request, 'try_mysql/person.html', {'person': p})
