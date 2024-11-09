from django.urls import path
from gerenciamento_estudantes import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.LoginPage, name='login')
]