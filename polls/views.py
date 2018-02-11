from django.shortcuts import HttpResponse


def index(request, question_id):
    return HttpResponse("<h1>Hello, its last chance...</h2>")

def detail(request, question_id):
    return HttpResponse("U r looking for results %s" % question_id)

def vote(request, question_id):
    return HttpResponse("U r voting %s" % question_id)
    