from django.urls import reverse_lazy
from django.views import generic

from .models import Task


class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    queryset = Task.objects.all()


class CreateView(generic.CreateView):
    model = Task
    fields = ['text']
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'


class DeleteView(generic.DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:index')
