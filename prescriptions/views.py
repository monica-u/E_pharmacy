from django.views import generic
from django.urls import reverse_lazy
from .models import Prescription

class IndexView(generic.ListView):
    template_name = 'prescriptions/index.html'
    context_object_name = 'prescription_list'

    def get_queryset(self):
        """Return the all prescriptions."""
        return Prescription.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'prescriptions/create.html'
    model = Prescription
    fields = ['message']
    success_url = reverse_lazy('prescriptions:index') # more robust than hardcoding to /prescriptions/; directs user to index view after creating a prescription

class UpdateView(generic.edit.UpdateView):
    template_name = 'prescriptions/update.html'
    model = Prescription
    fields = ['message']
    success_url = reverse_lazy('prescriptions:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'prescriptions/delete.html' # override default of prescriptions/prescription_confirm_delete.html
    model = Prescription
    success_url = reverse_lazy('prescriptions:index')
