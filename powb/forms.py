from __future__ import unicode_literals

from django import forms


class PlayersForm(forms.Form):
    firstname = forms.CharField(label='FirstName', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label='LastName', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    n1 = forms.IntegerField(initial=1, label='N1',
                            widget=forms.TextInput(attrs={'class': 'form-control input-20 atright'}))
    n2 = forms.IntegerField(initial=1, label='N2',
                            widget=forms.TextInput(attrs={'class': 'form-control input-20 atright'}))
    n3 = forms.IntegerField(initial=1, label='N3',
                            widget=forms.TextInput(attrs={'class': 'form-control input-20 atright'}))
    n4 = forms.IntegerField(initial=1, label='N4',
                            widget=forms.TextInput(attrs={'class': 'form-control input-20 atright'}))
    n5 = forms.IntegerField(initial=1, label='N5',
                            widget=forms.TextInput(attrs={'class': 'form-control input-20 atright'}))
    powb = forms.IntegerField(initial=1, label='PwB',
                              widget=forms.TextInput(attrs={'class': 'form-control input-20 atright'}))
