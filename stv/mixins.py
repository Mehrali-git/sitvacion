from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from stv.models import Detail
from jdatetime import datetime, timedelta


class FormValidAddMixin():
    def form_valid(self, form):
        self.frm = form.save(commit=False)
        self.frm.branch = self.request.user

        self.frm.date_persian = datetime.today()
        self.frm.ip = self.request.META.get('REMOTE_ADDR')

        esk = int(form.cleaned_data['es_1']) + int(form.cleaned_data['es_2']) + int(form.cleaned_data['es_5']) \
              + int(form.cleaned_data['es_10']) + int(form.cleaned_data['es_20']) + int(form.cleaned_data['es_50']) \
              + int(form.cleaned_data['es_100']) + int(form.cleaned_data['es_far'])

        nikl = int(form.cleaned_data['n_1']) + int(form.cleaned_data['n_2']) + int(form.cleaned_data['n_5']) \
               + int(form.cleaned_data['n_10'])+ int(form.cleaned_data['n_li'])

        ir_chk = int(form.cleaned_data['ir_50']) + int(form.cleaned_data['ir_100']) + int(form.cleaned_data['ir_far'])

        tabr = int(form.cleaned_data['t_m']) + int(form.cleaned_data['t_va']) + int(form.cleaned_data['t_ch_25']) \
               + int(form.cleaned_data['t_ch_50']) + int(form.cleaned_data['t_ch_100']) + int(
            form.cleaned_data['t_ch_hav']) + int(form.cleaned_data['t_ch_taz']) \
               + int(form.cleaned_data['t_pard']) + int(form.cleaned_data['t_saf'])

        try:
            self.frm.total_yesterday = (
                Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()).total
            print('**********************************************************')
            print(self.frm.total_yesterday)
        except:
            self.frm.total_yesterday = form.cleaned_data['total_yesterday']
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print(self.frm.total_yesterday)

        self.frm.total = (int(self.frm.total_yesterday) + int(form.cleaned_data['daryaft'])) - int(
            form.cleaned_data['pardakht'])
        self.frm.daryaft = form.cleaned_data['daryaft']
        self.frm.pardakht = form.cleaned_data['pardakht']
        nikl_ir_chk_esk = int(esk) + int(nikl) + int(ir_chk)

        if nikl_ir_chk_esk == self.frm.total:
            self.frm.save()
        else:
            context = {
                'diffrent': int(nikl_ir_chk_esk) - int(self.frm.total),
                'back': self.request.path,
            }
            return render(self.request, 'stv/diffrent.html', context)

        print(self.frm.branch)
        print(self.frm.total)
        print(self.frm.total_yesterday)
        return HttpResponseRedirect(reverse_lazy('stv:home'))


class FormValidUpdateMixin():
    def form_valid(self, form):
        self.frm = form.save(commit=False)
        self.frm.branch = self.request.user

        self.frm.date_persian = datetime.today()
        self.frm.ip = self.request.META.get('REMOTE_ADDR')

        esk = int(form.cleaned_data['es_1']) + int(form.cleaned_data['es_2']) + int(form.cleaned_data['es_5']) \
              + int(form.cleaned_data['es_10']) + int(form.cleaned_data['es_20']) + int(form.cleaned_data['es_50']) \
              + int(form.cleaned_data['es_100']) + int(form.cleaned_data['es_far'])

        nikl = int(form.cleaned_data['n_1']) + int(form.cleaned_data['n_2']) + int(form.cleaned_data['n_5']) \
               + int(form.cleaned_data['n_10'])+ int(form.cleaned_data['n_10'])

        ir_chk = int(form.cleaned_data['ir_50']) + int(form.cleaned_data['ir_100']) + int(form.cleaned_data['ir_far'])

        tabr = int(form.cleaned_data['t_m']) + int(form.cleaned_data['t_va']) + int(form.cleaned_data['t_ch_25']) \
               + int(form.cleaned_data['t_ch_50']) + int(form.cleaned_data['t_ch_100']) + int(
            form.cleaned_data['t_ch_hav']) + int(form.cleaned_data['t_ch_taz']) \
               + int(form.cleaned_data['t_pard']) + int(form.cleaned_data['t_saf'])

        try:
            self.frm.total_yesterday = (
                Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()).total_yesterday
        except:
            self.frm.total_yesterday = form.cleaned_data['total_yesterday']

        self.frm.total = (int(self.frm.total_yesterday) + int(form.cleaned_data['daryaft'])) - int(
            form.cleaned_data['pardakht'])
        self.frm.daryaft = form.cleaned_data['daryaft']
        self.frm.pardakht = form.cleaned_data['pardakht']
        nikl_ir_chk_esk = int(esk) + int(nikl) + int(ir_chk)

        if nikl_ir_chk_esk == self.frm.total:
            self.frm.save()
        else:
            context = {
                'diffrent': int(nikl_ir_chk_esk) - int(self.frm.total),
                'back': self.request.path,
            }
            return render(self.request, 'stv/diffrent.html', context)

        print(self.frm.branch)
        print(self.frm.total)
        print(self.frm.total_yesterday)
        return HttpResponseRedirect(reverse_lazy('stv:home'))


class NoAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دسترسی به صفحه را ندارید")


class GetCashYesterDayMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['mande_yesterday'] = (
                Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()).total
        except:
            context['mande_yesterday'] = '012'
        return context


class GetDetailDayMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['mande_yesterday'] = (
                Detail.objects.filter(branch=self.request.user).order_by('date_persian').last()).total_yesterday
        except:
            context['mande_yesterday'] = '012'
        return context
