from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Data
import csv, io

class IndexView(generic.list.ListView):
    model = Data
    paginate_by = 50
    context_object_name = 'data_entries'
    template_name = 'index.html'

def csv_upload(request):
    data_entries = Data.objects.all()
    template = "index.html"
    prompt = {'order': 'CSV must have 14 columns', \
            'data_entries': data_entries}
    if request.method == "GET":
        return render(request, template, prompt)
    if request.method == "POST":
        csv_file=request.FILES.get('csv', None).read().decode('UTF-8')
        io_string = io.StringIO(csv_file)
        next(io_string)
        for row in csv.reader(io_string, delimiter=';', quotechar='"'):
            # Bulk variable declaration from row (14 pieces)
            code, name, level1, level2, level3, price, priceSP, quantity, \
                    value_fields, joint_purchases, measurment_unit, picture, \
                    show_on_mainpage, description = row[:]
            # Creating object with variables as Data model fields
            Data.objects.create(code=code, name=name,
                    #level1=level1, level2=level2, level3=level3,
                    price=price, priceSP=priceSP, quantity=quantity,
                    value_fields=value_fields, #joint_purchases=joint_purchases,
                    measurment_unit=measurment_unit, picture=picture,
                    show_on_mainpage=show_on_mainpage, description=description)

        context = {'data_entries': data_entries}
        #response = render(request, "csv_upload.html")
        response = render(request, template, context)
        #response = redirect(IndexView.as_view())
        #response = HttpResponseRedirect('')
        #response = HttpResponse('')
        return response
