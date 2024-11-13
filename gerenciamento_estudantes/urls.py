from django.urls import path
from gerenciamento_estudantes import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.redirect_to_login, name='redirect_login'),
    path('test', views.test, name='test'),
    path('profile', views.profile, name='profile'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('lista-alunos', views.AlunosView.as_view(), name='lista-alunos'),
    path('lista-professores', views.ProfessoresView.as_view(), name='lista-professores'),
]