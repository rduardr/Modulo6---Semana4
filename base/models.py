from django.db import models

class Contato(models.Model):

  PREFERENCIA_EVENTO_CHOICES = (
    ('todos', 'Todos'),
    ('musicais', 'Eventos Musicais'),
    ('esportivos', 'Eventos Esportivos'),
    ('educativos', 'Eventos Educativos'),
  )

  nome = models.CharField(verbose_name= 'Nome', max_length=50)
  email = models.EmailField(verbose_name= 'E-mail',max_length=100)
  preferencia_evento = models.CharField(
    verbose_name='Preferência de Evento', max_length=20, default='todos',
    choices=PREFERENCIA_EVENTO_CHOICES)
  mensagem = models.TextField(verbose_name= 'Mensagem')
  data = models.DateTimeField(verbose_name= 'Data Envio',auto_now_add=True)
  lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)

  def __str__(self):
    return f'{self.nome} [{self.email}]'
  class Meta:
    verbose_name = 'Formulário de Contato'
    verbose_name_plural = 'Formulários de Contatos'
    ordering = ['-data']