from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

from contacts.forms import ContactForm
from contacts.models import Contact
from base.models import ExtendedFlatPage


class AddContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contacts/consult.html"
    success_url = reverse_lazy("success")

    def get_context_data(self, *args, **kwargs):
        context = super(AddContactView, self).get_context_data(**kwargs)
        context["flatpage"] = ExtendedFlatPage.objects.get(url="/consult/")
        return context
