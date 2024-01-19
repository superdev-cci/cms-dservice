from django import forms
from django.contrib.admin import widgets


class MemberHoldPvActionForm(forms.Form):
    member = forms.CharField(label='Member', widget=widgets.AdminTextInputWidget(attrs={'value': ''}))
    hpv = forms.CharField(label='Hold PV', widget=widgets.AdminTextInputWidget(attrs={'value': ''}))
