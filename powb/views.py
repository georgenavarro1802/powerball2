from __future__ import unicode_literals

from collections import defaultdict

import operator
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from powb.forms import PlayersForm
from powb.functions import bad_json, ok_json
from powb.models import Player


def generate_winning_numbers(players):
    general_numbers_list = []
    general_powerball_ist = []
    if players:
        for elem in players:
            general_numbers_list.append(elem.n1)
            general_numbers_list.append(elem.n2)
            general_numbers_list.append(elem.n3)
            general_numbers_list.append(elem.n4)
            general_numbers_list.append(elem.n5)
            general_powerball_ist.append(elem.powb)

        appearances = defaultdict(int)
        appearances_powb = defaultdict(int)
        for curr in general_numbers_list:
            appearances[curr] += 1
        favorites_numbers = dict(sorted(appearances.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
        for curr in general_powerball_ist:
            appearances_powb[curr] += 1
        favorite_powerball = dict(sorted(appearances_powb.iteritems(), key=operator.itemgetter(1), reverse=True)[:1])
        return ",".join(str(n) for n in favorites_numbers.keys()) + ',{}'.format(favorite_powerball.keys().pop())
    return ""


def index(request):
    players = Player.objects.all()
    list = generate_winning_numbers(players)
    if list:
        favorite_numbers = sorted(list.split(',')[:5])
        powerball_number = list.split(',')[-1:][0]
    else:
        favorite_numbers = ['', '', '', '', '']
        powerball_number = ['']
    return render(request, 'index.html',
                  {
                      'title': 'Python Code Sample Project',
                      'players': players,
                      'favorite_numbers': favorite_numbers,
                      'powerball_number': powerball_number
                  })


def add_player(request):
    if request.method == 'POST':
        f = PlayersForm(request.POST)
        temp = []
        if f.is_valid():
            try:
                with transaction.atomic():
                    n1 = f.cleaned_data['n1']
                    n2 = f.cleaned_data['n2']
                    n3 = f.cleaned_data['n3']
                    n4 = f.cleaned_data['n4']
                    n5 = f.cleaned_data['n5']
                    temp.append(n1)
                    temp.append(n2)
                    temp.append(n3)
                    temp.append(n4)
                    temp.append(n5)
                    if len(temp) != len(set(temp)):
                        return bad_json(mensaje='ALERT: DUPLICATE NUMBERS ON YOUR LIST')
                    player = Player(firstname=f.cleaned_data['firstname'],
                                    lastname=f.cleaned_data['lastname'],
                                    n1=n1, n2=n2, n3=n3, n4=n4, n5=n5,
                                    powb=f.cleaned_data['powb'])
                    player.save()
                    return ok_json()
            except:
                return bad_json(error=1)
        else:
            return bad_json(error=1)

    return render(request, 'players/add.html',
                  {
                      'title': 'Add Player',
                      'form': PlayersForm()
                  })


def clean_data(request):
    Player.objects.all().delete()
    return HttpResponseRedirect('/')
