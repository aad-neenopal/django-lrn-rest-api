from django.shortcuts import render, get_object_or_404
from .models import Poll, Vote, Choice
from django.http import JsonResponse

# Create your views here.

def polls_list(request):
    polls = Poll.objects.all()
    data = {
        "results": list(
            polls.values("question", "created_by__username", "pub_date")
        )
    }
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
        }
    }

    return JsonResponse(data)

