from django.db import models
from django.utils import timezone

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200, blank=True)
    fecha_nacimiento = models.IntegerField(null=True)
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    IDIOMAS = [
        ('ES', 'Español'),
        ('EN', 'Inglés'),
        ('FR', 'Francés'),
        ('IT', 'Italiano'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default='ES',
    )
    
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE, null=True)
    autores =   models.ManyToManyField(Autor)
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    puntos = models.FloatField(default=5.0, db_column='puntos_biblioteca')
    libros = models.ManyToManyField(Libro, through='Prestamos')
    def __str__(self):
        return self.nombre
    
class DatosCliente(models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    cliente= models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True)
    
class Prestamos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)
    