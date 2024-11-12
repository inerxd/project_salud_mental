from django.db import models


# modelos creado a partir de la base de datos mysql 

# nombre del modelo
class TypeUser(models.Model):
    tipo_usuario = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    permisos = models.ManyToManyField('Permisos', related_name='type_users')

# devuelve una cadena de datos de TypeUser y poder trabajar con ellos en el
# panel de administracion
    def __str__(self):
        return self.tipo_usuario  

# para que  coincidan el nombre del la tabla tipo de usario del modelo
# y la bade de datos 
    class Meta:
        db_table = 'type_user'

# nombre del modelos
class Indentificador(models.Model):
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    TypeUserId = models.ForeignKey(TypeUser , on_delete=models.CASCADE , db_column='type_user_id',default=3)

# devuelve una cadena de datos de Indentificador y poder trabajar con ellos en el
# panel de administracion
    def __str__(self):
        return self.email  
    
# para que  coincidan el nombre del la tabla indentificador del modelo
# y la bade de datos 
    class Meta:
        db_table = 'indentificador'
    
# modelos de DatosUsuarios
class DatosUsuarios(models.Model):
    name = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=245)
    url_image = models.CharField(max_length=540)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    identificador  = models.ForeignKey(Indentificador , on_delete=models.CASCADE,db_column='indentificador_id')

# devuelve una cadena de datos de DatosUsuarios y poder trabajar con ellos en el
# panel de administracion
    def __str__(self):
        return f"{self.name} {self.apellidos} ({self.identificador.email})"

# para que  coincidan el nombre del la tabla DatosUsuarios del modelo
# y la bade de datos     
    class Meta:
        db_table = 'datos_usuarios'


class Permisos(models.Model):
    permiso = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)

# devuelve una cadena de datos de Permisos y poder trabajar con ellos en el
# panel de administracion   
    def __str__(self):
        return self.permiso
    
# para que  coincidan el nombre del la tabla DatosUsuarios del modelo
# y la bade de datos   
    class Meta:
        db_table = 'permisos'

# modelos de tabla intermedia de tipos de usuarios y permisos
class TypePermisosUser(models.Model):
    type_user_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE)
    permisos_id = models.ForeignKey(Permisos, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tipo_permisos_usuarios'  # Nombre exacto de la tabla intermedia en la base de datos
        unique_together = ('type_user_id', 'permisos_id')  # Asegura que la combinación sea única

class Preguntas(models.Model):
    categoria = models.CharField(max_length=45)
    nombreEncuesta = models.CharField(max_length=45)
    pregunta = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    idEmail = models.ForeignKey(Indentificador,on_delete=models.CASCADE)
 

    def __str__(self):
        return f"{self.categoria} {self.nombreEncuesta} {self.pregunta} {self.fecha_creacion}"
    
class Respuesta(models.Model):
    respuesta = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)
    idPreguntas = models.ForeignKey(Preguntas,on_delete=models.CASCADE)
    idEmail = models.ForeignKey(Indentificador,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.respuesta} {self.fecha_creacion} ({self.idPreguntas.pregunta})"
    

        



