from django.shortcuts import render

# Create your views here.


def requests(request):
    if request.method == "GET":
        # Check to see if user is admin, don or aux to redirect to the correct site
        return
    elif request.method == "POST":
        # Process the request correctly
        return
    return
