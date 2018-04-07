# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):

    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter']+=1


    print 'counter is: {}'.format(request.session['counter'])

    data = {
        'rand_word': get_random_string(length=14),
    }
        
    return render(request,'random_app/index.html',data)

def random_word(request):
    return redirect('/')

def reset(request):
    print 'got here!'
    try:
        # print "got here!"
        del request.session['counter']
    except KeyError:
        print 'sorry, cannot reset counter'
        pass
    
    return redirect('/')


