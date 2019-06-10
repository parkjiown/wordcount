from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aobut.html')

def result(request):
    text=request.GET.get('fulltext')
    words = text.split()
    word_dictionary = {}
    print('=========================')
    print(text)
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    
    print(word_dictionary.items())
    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})
