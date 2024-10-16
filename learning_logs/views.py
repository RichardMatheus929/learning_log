from django.shortcuts import render
from django.views.generic import CreateView

from .models import Topic

# Create your views here.
class FirstView(CreateView):
    model = Topic  # Especifica o modelo a ser criado
    fields = ['title', 'text']  # Substitua pelos campos do modelo que deseja exibir
    template_name = 'index.html'
    success_url = '/'  # Redireciona após o sucesso

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()

        return context
