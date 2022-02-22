from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Vote, Choice
from django.http import JsonResponse

# Create your views here.

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)
    #context = {'polls', polls}
    #return render (request, 'polls.html', context)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)
    #poll = Poll.objects.get(id = pk)
    #context = {'poll', poll}
    #return render (request, 'polls-detail.html', context)
    
