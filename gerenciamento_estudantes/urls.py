from django.urls import path
from gerenciamento_estudantes import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.redirect_to_login, name='redirect_login'),
    path('test', views.test, name='test'),
    path('profile', views.profile, name='profile'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
]