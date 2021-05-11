from django.urls import path
from .views import displayDetail, DetailAdd, DetailUpdate, PrintStv, GeneratePdf, CreatePdf, render_pdf_view1

app_name = "stv"

urlpatterns = [
    path('', displayDetail.as_view(), name="home"),
    path('Detail/add/', DetailAdd.as_view(), name='detailAdd'),
    path('Detail/update/<int:pk>', DetailUpdate.as_view(), name='DetailUpdate'),
    path('print/', PrintStv.as_view(), name='print'),
    # path('showprint1/', GeneratePdf.as_view(), name='show1'),
    # path('showprint2/', render_pdf_view1, name='show2'),
]
