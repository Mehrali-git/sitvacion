from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from jdatetime import datetime, timedelta
from stv.mixins import NoAccessMixin, GetCashYesterDayMixin, GetDetailDayMixin, FormValidAddMixin, FormValidUpdateMixin
from . import models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.urls import reverse_lazy
from .forms import DetailForms
from stv.models import Detail, User

# for report pdf
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
from io import BytesIO
from django.template import Context

# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile

# Create your views here.

class displayDetail(LoginRequiredMixin, ListView):
    template_name = "stv/home.html"

    def get_queryset(self):
        return Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_date'] = datetime.today()
        return context


class DetailAdd(LoginRequiredMixin, GetCashYesterDayMixin, FormValidAddMixin, NoAccessMixin, CreateView):
    form_class = DetailForms
    template_name = "stv/monyh.html"

    def get_form_kwargs(self):
        kwargs = super(DetailAdd, self).get_form_kwargs()
        try:
            kwcontext = (Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()).total
        except:
            kwcontext = '012'
        kwargs.update({
            'mande_yesterday': kwcontext
        })
        return kwargs


class DetailUpdate(LoginRequiredMixin, GetDetailDayMixin, FormValidUpdateMixin, NoAccessMixin, UpdateView):
    form_class = DetailForms
    template_name = "stv/monyh.html"

    def get_queryset(self):
        return Detail.objects.filter(branch=self.request.user, date_persian=datetime.today())


class PrintStv(LoginRequiredMixin, NoAccessMixin, ListView):
    template_name = "stv/PrintStv.html"

    def get_queryset(self):
        return Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_date'] = datetime.today()
        return context


def render_pdf_view1(request):
    context = {'object_list': User.objects.all() }
    return render(request, 'stv/test.html', context)


def render_pdf_view(template_src, context_dict={}):
    response = HttpResponse(content_type='application/text')
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_src)
    html = template.render(context_dict)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

#
# class GeneratePdf(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         context = {'object_list': Detail.objects.filter(branch=request.user).order_by('date_persian').last(), }
#         pdf = render_to_pdf('stv/PrintStv', context)
#         return HttpResponse(pdf, content_type='application/pdf')


class CreatePdf(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {'object_list': Detail.objects.filter(branch=request.user).order_by('date_persian').last(), }
        pdf = render_pdf_view('stv/PrintStv.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

def GeneratePdf(request):
    """Generate pdf."""
    # Model data
    people = User.objects.all()

    # Rendered
    html_string = render_to_string('stv/pdf.html', {'people': people})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())
    return response