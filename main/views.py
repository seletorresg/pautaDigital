from django.db.models import query
from django.db.models.fields import SlugField
from django.shortcuts import render
from main.models.client import Client
from main.models.brand import Brand
from main.models.invoice import Invoice

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
# Import mimetypes module
import mimetypes
# import os module
import os
import datetime

# Create your views here.
# Functions Based Views.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> Son las %s </body></html>" % now
    return HttpResponse(html)

def home_page(request):
    template_name = 'home.html'
    return render(request,template_name=template_name)

def home_with_time(request):
    template_name = 'home_with_date.html'
    now = datetime.datetime.now()
    context = {'now': now}
    return render(request,template_name=template_name,context=context)

class show_clients(ListView):
    template_name = 'clients_list.html'
    query_set = Client.objects.all()
    paginate_by = 6

    def get_queryset(self):
        return self.query_set.order_by('id')

class show_brands(DetailView):
    template_name = 'brands_list.html'
    model = Client
    client_id:int

    def get(self, request, *args, **kwargs):
        self.client_id = int(kwargs['pk'])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.filter(client_id=self.client_id)
        return context

def show_invoices(request):
    template_name = 'invoice_list.html'
    invoices = Invoice.objects.all()
    context = {"invoices": invoices}
    return render(request, template_name=template_name, context=context)

def download_pdf_file(request, fileName=''):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\/media\/' + fileName
    path = open(filepath, 'rb')
    print(filepath)
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % fileName
    return response

