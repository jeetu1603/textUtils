# I have created this file - Jeetu 

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h1>TextUtils is a tool for analyzing text data in django backend</h1>")

def analyze(request):
    # get the text 
    djText = request.POST.get('text', 'default')

    # check checkox values 
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # check which checkbox is on 
    if removepunc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punc:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djText = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djText:
            analyzed += char.upper()
        params = {'purpose': 'changed to UPPERCASE', 'analyzed_text': analyzed}
        djText = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djText:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djText = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djText):
            if not(djText[index] == " " and djText[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djText = analyzed

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("<h1>Plz Select any Operation and try again</h1>")

    return render(request, "analyze.html", params)