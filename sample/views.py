from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView

from .models import Sample
from .forms import SampleForm


class IndexView(ListView):
    template_name = 'sample/index.html'
    queryset = Sample.objects.all()


class UploadView(CreateView):
    template_name = 'sample/upload.html'
    form_class = SampleForm
    success_url = reverse_lazy('sample:index')

    def form_valid(self, form):
        print('Form is valid.')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Form is not valid!')
        return super().form_invalid(form)
