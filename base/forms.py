from django import forms
#from base.models import Contato, Reserva


class ContatoForm(forms.Form):
        nome = forms.CharField()
        email = forms.EmailField()
        mensagem = forms.CharField(widget=forms.Textarea)

#class ReservaForm(forms.ModelForm):
        #class Meta:
           # model = Contato
           # fields = ['nome', 'email', 'mensagem']
