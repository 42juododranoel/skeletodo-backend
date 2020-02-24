from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Task


@method_decorator(login_required, name='dispatch')
class ListView(generic.ListView):  # noqa: D101
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.all()


@method_decorator(login_required, name='dispatch')
class CreateView(generic.CreateView):  # noqa: D101
    model = Task
    fields = ['text']
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        """Set user from request and call super."""
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):  # noqa: D101
    model = Task
    template_name = 'tasks/detail.html'


@method_decorator(login_required, name='dispatch')
class DeleteView(generic.DeleteView):  # noqa: D101
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')
