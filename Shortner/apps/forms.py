from django import forms
from .models import *


class SiteForm(forms.Form):
    texto_original = forms.CharField(required=True)

class DesencurtarForm(forms.Form):
    texto_encurtado = forms.CharField(required=True)