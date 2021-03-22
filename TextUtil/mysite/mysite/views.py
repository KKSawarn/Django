from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return  HttpResponse('Django Landing Pange')
    return render(request,'index.html')

    
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover', 'off')

    params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : djtext}
    result = ''
    if removepunc =='on':
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punctuation:
                result = result + i
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : result}
        return render(request, 'analyze.html', params)
    elif fullcaps =='on':
        analyzed = ""
        for i in djtext:
            analyzed = analyzed+ i.upper()
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover =="on"):
        analyzed = ''
        for i in djtext:
            if i != "\n" and i != "\r":
                analyzed = analyzed + i
            else:
                analyzed = analyzed+' '
        params = {'purpose' : 'Remove New Line', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    
    elif spaceremover == 'on':
        analyzed =''
        for index, val in enumerate(djtext):
            if djtext[index] ==' ' and djtext[index+1] == ' ':
                pass 
            analyzed = analyzed + djtext[index]
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error : Can not perform remove punctuation !')
    params['analyzed_text'] = result
    return render(request, 'analyze.html', params)

