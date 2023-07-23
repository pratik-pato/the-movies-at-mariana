from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    return render(request, 'moviemania/homepage.html')