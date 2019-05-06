# _*_ coding: utf-8 _*_

from django.forms import ModelForm
from dashboard.models import UserProfile
from models import Licience,Zyid 


class LicienceForm(ModelForm):
    class Meta:
        model = Licience
        fields = "__all__"

#class AuthorForm(ModelForm):
#    class Meta:
#        model = Author
#        fields = "__all__"

class ZyidForm(ModelForm):
    class Meta:
        model = Zyid
        fields = "__all__"

