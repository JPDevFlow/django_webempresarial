from django.contrib import admin
from .models import Link

# Configuración personalizada para el modelo Link en el panel de administración
class LinkAdmin(admin.ModelAdmin):
    # Los campos 'created' y 'updated' serán de solo lectura por defecto
    readonly_fields = ('created', 'updated')

    # Método para definir campos de solo lectura según el grupo del usuario
    def get_readonly_fields(self, request, obj=None):
        # Si el usuario pertenece al grupo 'Personal', solo puede ver 'key' y 'name' como solo lectura
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            # Para otros usuarios, los campos de solo lectura son 'created' y 'updated'
            return ('created', 'updated')

# Registro del modelo Link en el panel de administración con la configuración personalizada
admin.site.register(Link, LinkAdmin)
