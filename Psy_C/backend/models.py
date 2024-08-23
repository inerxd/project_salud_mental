from django.db import models




class TypeUser(models.Model):
    tipo_usuario = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)

class Indentificador(models.Model):
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    TypeUserId = models.ForeignKey(TypeUser , on_delete=models.CASCADE)

    def __str__(self):
        return self.email  



class DatosUsuarios(models.Model):
    name = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=245)
    url_image = models.CharField(max_length=540)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    identificador  = models.ForeignKey(Indentificador , on_delete=models.CASCADE)

    def __str__(self):
        return self.name


