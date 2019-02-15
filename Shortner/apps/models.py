from django.db import models

# Create your models here.


class Site(models.Model):
    texto_original = models.CharField(max_length=255, null = False)
    texto_encurtado = models.CharField(max_length=100, null = False)
    


#Pensando em formas de diminuir ou eliminar o bug da duplicidade nos textos encurtados
    """
    def encurta(self):
        tamanho = len(self.texto_original)
        encurtada = 'http://localhost:8000/'
        
        while len(encurtada) < (tamanho//5):
            x = self.texto_original[int(randon.randint(0, tamanho-1))]
            if x != '/':
                encurtada += x

        return encurtada"""