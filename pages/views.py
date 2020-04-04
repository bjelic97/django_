from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
  #  return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html",{})


def contact_view(request,*args, **kwargs):

    my_context = {
        "my_text" : "this is about me",
        "my_number":123,
        "my_list":[123,422,"Abc"],
        "my_html":"<h5>Render me proper way</h5>"
    }
    return render(request,"contact.html",my_context)