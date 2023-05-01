from django.db import models

# Create your models here.
class Contato(models.Model):
     nome = models.CharField(verbose_name='Nome', max_length=50)
     email = models.EmailField(verbose_name='E-mail')
     observacao = models.TextField(verbose_name='observação', blank=True)
     enviado_em = models.DateTimeField(verbose_name='Enviado em', auto_now=True)
     modeificado_em = models.DateTimeField(verbose_name='Modeificado em', auto_now=True)