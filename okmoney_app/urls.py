from django.urls import path

from .views import index

urlpatterns = [
    # inclua aqui as rotas
    path('', index, name='index'),  # index é o template html
    # path(nome do caminho da pag html ex:'pedidos/', pedido,  name='pedido'),
]
