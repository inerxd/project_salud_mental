from django.db import models




class TypeUser(models.Model):
    tipo_usuario = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    permisos = models.ManyToManyField('Permisos', related_name='type_users')

    def __str__(self):
        return self.tipo_usuario  
    
    class Meta:
        db_table = 'type_user'

class Indentificador(models.Model):
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    TypeUserId = models.ForeignKey(TypeUser , on_delete=models.CASCADE , db_column='type_user_id')

    def __str__(self):
        return self.email  
    class Meta:
        db_table = 'indentificador'
    

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
    
    class Meta:
        db_table = 'datos_usuarios'

class Permisos(models.Model):
    permiso = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.permiso
    
    class Meta:
        db_table = 'permisos'

class TypePermisosUser(models.Model):
    type_user_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE)
    permisos_id = models.ForeignKey(Permisos, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tipo_permisos_usuarios'  # Nombre exacto de la tabla intermedia en la base de datos
        unique_together = ('type_user_id', 'permisos_id')  # Asegura que la combinación sea única



