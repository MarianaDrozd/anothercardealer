from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.
from src.apps.dealers.models import Dealer

from src.apps.cars.models import Car


class DealersListView(ListView):
    model = Dealer.objects.all()
    context_object_name = 'dealers'
    template_name = 'dealers/list.html'

    def get_queryset(self):
        return Dealer.objects.all()  # FIX ME!!!


class DealersDetailView(DetailView):
    model = Dealer
    context_object_name = 'dealers'
    pk_url_kwarg = 'dealer_pk'
    template_name = 'dealers/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.filter(dealer=self.object)
        return context


def serialized_dealers(request):
    data = serializers.serialize('json', Dealer.objects.all())
    return HttpResponse(request.method + '<br>' + data)
