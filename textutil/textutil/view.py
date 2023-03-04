
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, 'index.html')

def analayze(request):
    djtext= request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitals = request.POST.get('capitals', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')


    if removepunc == "on":
        punctuatios=''' ! () - {} [] ; : ' " \ , <> . / ? @ # $ % ^&*~ '''
        analyzed = ""
        for char in djtext:
            if char not in punctuatios:
                analyzed= analyzed + char
        param={'purpose': 'remove punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyaze.html', param)

    elif capitals=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyaze.html', param)

    elif newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        param = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        return render(request, 'analyaze.html', param)

    elif spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        param = {'purpose': 'space removal', 'analyzed_text': analyzed}
        return render(request, 'analyaze.html', param)

    elif charcount == "on":
        analyzed = ""
        count = 0
        for i in djtext:
            count = count + 1
            analyzed = count
        param = {'purpose': 'Char counter', 'analyzed_text': analyzed}
        return render(request, 'analyaze.html', param)

    else:
        return HttpResponse("....Error....")

