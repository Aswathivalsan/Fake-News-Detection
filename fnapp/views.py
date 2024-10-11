from django.http import HttpResponse
from django.shortcuts import render
from .sp import Yahoo
from .sp2 import onmanorama
from .webscrapping import ongoogle
from .scrappbing import Onbing
from .sn_new import fetch_news_articles
from .simscore import simcheck

from .prediction import predict_fakenews_fn
from fnapp.models import *


import re

WORD = re.compile(r'\w+')
from nltk.stem import PorterStemmer


ps = PorterStemmer()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def sr(text):
    stop_words = set(stopwords.words('english')) | {'use', 'a'}

    word_tokens = word_tokenize(text.replace('.', ' '))

    filtered_sentence = []
    print("sw", stop_words)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    print(filtered_sentence)
    return ' '.join(filtered_sentence)

def login(request):
    return render(request,"loginindex.html")

def logincode(request):
    Uname = request.POST['uname']
    pwrd = request.POST['pwrd']
    ob= login_table.objects.get(username=Uname,password= pwrd)
    if ob.type=='admin':
        return HttpResponse('''<script>alert("Successfully logined");window.location="/check"</script>''')
    elif ob.type=='user':
        return HttpResponse('''<script>alert("Successfully logined");window.location="/check"</script>''')
    else:
        return HttpResponse('''<script>alert("invalid ");window.location="/</script>''')

def register(request):
    return render(request,"registerindex.html.html")




def check(request):
    return render(request, "homeindex.html")

def checkfn(request):
    try:
        tt = request.POST['textfield']
        rr=[]
        t=tt
        t=sr(tt)
        res = ongoogle(t)
        rr1=res
        print(res)
        rr.append(sum(res)/len(res))
        res = sum(res)

        res1 =  Yahoo(t)
        print(res1)
        rr.append(res1[0])
        res1 = sum(res1)


        res2 = fetch_news_articles(t)
        print(res2)
        rr.append(res2[0])
        res2 = sum(res2)


        res3 = onmanorama(t)
        print(res3)

        rr.append(res3[0])
        res3 = sum(res3)
        
        print("rr====>",rr)
        print("rr====>",rr1)
        avg=sum(rr)/len(rr)
        r = (res + res1 + res2 + res3) / 4
        fs,rs=simcheck(t)
        print(avg,fs,rs)
        result=predict_fakenews_fn([avg,rs,fs])
        print(result,"result")
        return render(request, "homeindex.html", {"val": res, "val1": res1, "val2": res2, "val3": res3, "Avg": r,"result":result,"txt":t})
    except:
        return HttpResponse('''<script>alert('Fake News No Scrapped Result');window.location='/check'</script>''')

#
# return render(request, "googleCheck.htmlCheck.html",{"val":res})
