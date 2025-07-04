from django.db import models
from apps.usuarios.models import UsuarioCustom
from apps.clientes.models import Cliente

class ItemCotizacion(models.Model):
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    @property
    def subtotal(self):
        return self.cantidad * self.valor_unitario

    @property
    def total_impuesto(self):
        return self.subtotal * (self.impuesto / 100)

    @property
    def total(self):
        return self.subtotal + self.total_impuesto

    def __str__(self):
        return f"{self.descripcion} x {self.cantidad}"

class Cotizacion(models.Model):
    ESTADOS = [
        ('B', 'Borrador'),
        ('E', 'Enviada'),
        ('A', 'Aprobada'),
        ('R', 'Rechazada'),
    ]
    
    usuario = models.ForeignKey(UsuarioCustom, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_validez = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='B')
    items = models.ManyToManyField(ItemCotizacion)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        ordering = ['-fecha_creacion']

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.items.all())

    @property
    def total_impuestos(self):
        return sum(item.total_impuesto for item in self.items.all())

    @property
    def total(self):
        return self.subtotal + self.total_impuestos

    def __str__(self):
        return f"Cotización #{self.id} - {self.cliente}"

# Create your models here.
