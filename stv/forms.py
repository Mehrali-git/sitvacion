from django import forms
from .models import Detail



class DetailForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        mande_y = kwargs.pop('mande_yesterday', None)
        super(DetailForms, self).__init__(*args, **kwargs)
        if mande_y != '012':
            self.fields['total_yesterday'].disable = True
            total_yesterday = forms.CharField(max_length=100, required=False,
                                              widget=forms.TextInput(attrs={'value': mande_y}))
        es_1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_5 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_10 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_20 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_50 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_100 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        es_far = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))

        n_1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        n_2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        n_5 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        n_10 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        n_li = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))

        ir_50 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'value': '0'}))
        ir_100 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'value': '0'}))
        ir_far = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'value': '0'}))

        t_m = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_va = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_ch_25 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_ch_50 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_ch_100 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_ch_hav = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_ch_taz = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_pard = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        t_saf = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))

        sek_t = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        sek_n = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        sek_r = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': '0'}))
        daryaft = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'value': '0'}))
        pardakht = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'value': '0'}))

        es_1.widget.attrs['onkeyup'] = "separateNum(this.value,this);sum_split_row('es_1_b','es_1_g','id_es_1','1000');"
        es_2.widget.attrs['onkeyup'] = "separateNum(this.value,this);sum_split_row('es_2_b','es_2_g','id_es_2','2000');"
        es_5.widget.attrs['onkeyup'] = "separateNum(this.value,this);sum_split_row('es_5_b','es_5_g','id_es_5','5000');"
        es_10.widget.attrs[
            'onkeyup'] = "separateNum(this.value,this);sum_split_row('es_10_b','es_10_g','id_es_10','10000');"
        es_20.widget.attrs[
            'onkeyup'] = "separateNum(this.value,this);sum_split_row('es_20_b','es_20_g','id_es_20','20000');"
        es_50.widget.attrs[
            'onkeyup'] = "separateNum(this.value,this);sum_split_row('es_50_b','es_50_g','id_es_50','50000');"
        es_100.widget.attrs[
            'onkeyup'] = "separateNum(this.value,this);sum_split_row('es_100_b','es_100_g','id_es_100','100000');"
        es_far.widget.attrs['onkeyup'] = "separateNum(this.value,this);"

        n_1.widget.attrs['onkeyup'] = "separateNum(this.value,this);"
        n_2.widget.attrs['onkeyup'] = "separateNum(this.value,this);"
        n_5.widget.attrs['onkeyup'] = "separateNum(this.value,this);"
        n_10.widget.attrs['onkeyup'] = "separateNum(this.value,this);"
        n_li.widget.attrs['onkeyup'] = "separateNum(this.value,this);"

        ir_50.widget.attrs[
            'onkeyup'] = "separateNum(this.value,this);sum_split_row('ir_50_b','ir_50_g','id_ir_50','500000');"
        ir_100.widget.attrs[
            'onkeyup'] = "separateNum(this.value,this);sum_split_row('ir_100_b','ir_100_g','id_ir_100','1000000');"
        ir_far.widget.attrs['onkeyup'] = "separateNum(this.value,this);"

        daryaft.widget.attrs['onkeyup'] = "separateNum(this.value,this);difference_sandogh()"
        pardakht.widget.attrs['onkeyup'] = "separateNum(this.value,this);difference_sandogh()"



    class Meta:
        model = Detail
        fields = [
            'es_1', 'es_2', 'es_5', 'es_10', 'es_20', 'es_50', 'es_100', 'es_far',
            'n_1', 'n_2', 'n_5', 'n_10','n_li',
            'ir_50', 'ir_100', 'ir_far',
            't_m', 't_va', 't_ch_25', 't_ch_50', 't_ch_100', 't_ch_hav', 't_ch_taz', 't_pard', 't_saf',
            'sek_t', 'sek_n', 'sek_r',
            'daryaft', 'pardakht', 'total_yesterday'
        ]


