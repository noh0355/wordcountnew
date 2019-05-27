from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
@csrf_exempt
def result(request):
    text = request.POST['fulltext']
    words = text.split()

    word_dictionary = {}
    for word in words :
        if word in word_dictionary:
            word_dictionary[word]+=1
        else :
            word_dictionary[word]=1

    return render(request, 'result.html',{'total':text, 'split':len(words), 'dictionary':word_dictionary.items})

def result2(request):
    lotto = random.sample(range(1,50),5)
    text = request.GET['count']
    texts = text.split()

    see=[]
    seee=[]
    i=0
    j=0

    for i in range(0,5):
        for j in range(i,4):
            if texts[i] == str(lotto[j]) :
                if len(see) < i+1:
                    see += [None] * (i+1 - len(see))
                    see[i] = lotto[j]
            else:
                if len(seee)< i+1:
                    seee += [None] * (i+1 - len(seee))
                    seee[i] = texts[j]
    return render(request, 'result2.html', {'lotto':lotto, 'text':text, 'see':see, 'see2':seee})

def result3(request):
    lotto = random.sample(range(0,9),4)
    text = request.GET['count1']
    texts = text.split()

    tr_cnt=0 #몇번 게임 시도
    st_cnt=0 #스트라이크 개수
    bl_cnt=0 #볼의 개수

    for i in range(0,3):
        for j in range(0,3):
            if(texts[i] == str(lotto[j]) and i==j):
                st_cnt +=1
            elif(texts[i] == str(lotto[j]) and i!=j):
                bl_cnt +=1

    return render(request, 'result3.html', {'lo':lotto, 'st':st_cnt,'bl':bl_cnt})   
