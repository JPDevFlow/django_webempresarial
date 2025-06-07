from .models import Link

def ctx_dict(requests): #extendiendo el diccionario de contexto
    ctx = {}
    links = Link.objects.all()  # Obtener todos los enlaces de la base de datos
    for link in links:
        ctx[link.key] = link.url
    return ctx