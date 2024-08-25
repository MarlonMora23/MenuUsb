import hashlib
from django.db import models

# Create your models here.
class Usuario(models.Model):  #nombre de la tabla en la Base de Datos
    id_usuario = models.CharField(max_length=100, default='DEFAULT VALUE',unique=True,primary_key=True)
    nombre = models.CharField(max_length=128, default='DEFAULT VALUE')
    clave = models.CharField(max_length=128, default='DEFAULT VALUE')
    correo = models.CharField(max_length=128, default='DEFAULT VALUE')
    
 #super().save(*args, **kwargs) para guardar en esta tabla
    def save(self, *args, **kwargs):
        self.clave = hashlib.md5(self.clave.encode('utf-8')).hexdigest()
        super(Usuario, self).save(*args, **kwargs)

    def autenticarUsuario(self, *args, **kwargs):
        auth = Usuario.objects.filter(correo=self.correo,
                                    clave=self.clave).exists()

        print(auth)
        return auth

    def buscarUsuario(self, *args, **kwargs):
        aux = list(Usuario.objects.filter(correo=self.correo,
                                    clave=self.clave))
        print(aux[0])
        return aux[0]


class Meta:
     db_table = 'usuarios' #nombre de instancia con la que llamamos la tabla en la Base de Datos