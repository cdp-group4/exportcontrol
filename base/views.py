from django.views.generic import TemplateView
from regulations.forms import SearchForm
from django.urls import reverse

from django.contrib.flatpages import models


class FrontPageView(TemplateView):
    template_name = "base/front_page.html"

    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)
        context["search_form"] = SearchForm(self.request.GET)
        context["form_action"] = reverse("search")
        context["flatpage"] = models.FlatPage.objects.get(url='/home/').title
        return context
