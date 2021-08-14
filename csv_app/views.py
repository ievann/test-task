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
    if request.method == "POST":
        csv_file=request.FILES.get('csv', None).read().decode('UTF-8')
        io_string = io.StringIO(csv_file)
        next(io_string)
        for row in csv.reader(io_string, delimiter=';', quotechar='"'):
            #print('ROW: ', row)
            code = row[0]
            name = row[1]
            level1 = row[2]
            level2 = row[3]
            level3 = row[4]
            price = row[5]
            priceSP = row[6]
            quantity = row[7]
            value_fields = row[8]
            joint_purchases = row[9]
            measurment_unit = row[10]
            picture = row[11]
            show_on_mainpage = row[12]
            description = row[13]
            Data.objects.create(code=code, name=name,
                    #level1=level1, level2=level2, level3=level3,
                    price=price, priceSP=priceSP, quantity=quantity,
                    value_fields=value_fields, #joint_purchases=joint_purchases,
                    measurment_unit=measurment_unit, picture=picture,
                    show_on_mainpage=show_on_mainpage, description=description)

        #response = render(request, "csv_upload.html")
        #response = render(request, "index.html")
        #response = redirect(IndexView.as_view())
        response = HttpResponseRedirect('')
        #response = HttpResponse('')
        return response
