# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from .csv_cleanup import csv_handler
from .models import Data

class IndexView(generic.list.ListView):
    model = Data
    paginate_by = 50
    context_object_name = 'data_entries'
    template_name = 'index.html'

def csv_upload(request):
    template = "index.html"
    data_entries = Data.objects.all()
    prompt = {'order': 'CSV must have 14 columns', \
            'data_entries': data_entries}

    if request.method == "GET":
        return render(request, template, prompt)

    if request.method == "POST":
        return csv_handler(request, template, data_entries)

# This piece of code has been moved to another file, csv_cleanup.py
#        csv_file=request.FILES.get('csv', None).read().decode('UTF-8')
#        io_string = io.StringIO(csv_file)
#        next(io_string)
#        for row in csv.reader(io_string, delimiter=';', quotechar='"'):
#
#            # Bulk variable declaration from row (14 pieces)
#            code, name, level1, level2, level3, price, priceSP, quantity, \
#                    value_fields, joint_purchases, measurment_unit, picture, \
#                    show_on_mainpage, description = row[:]
#
#            # Converting comma separated price and priceSP into floats;
#            # priceSP string may also contain double cuotes "
#            price = float(".".join(price.split(",")))
#            priceSP = priceSP.replace('"', '')
#            priceSP = float(".".join(priceSP.split(",")))
#
#            # Handling fucked up floating quantity
#            quantity = int(round(float(quantity)))
#
#            # measurment_unit may have double double quotes, fixing this
#            measurment_unit = measurment_unit.replace('"', '')
#
#            # Cleaning up description
#            description = description.replace('"', '')
#            description = description.replace(',', ', ')
#            description = description.replace(':', ': ')
#
#            # Creating object with variables as Data model fields
#            Data.objects.create(code=code, name=name,
#                    level1=level1, level2=level2, level3=level3,
#                    price=price, priceSP=priceSP, quantity=quantity,
#                    value_fields=value_fields, #joint_purchases=joint_purchases,
#                    measurment_unit=measurment_unit, picture=picture,
#                    show_on_mainpage=show_on_mainpage, description=description)
#
#        context = {'data_entries': data_entries}
#        #response = render(request, "csv_upload.html")
#        response = render(request, template, context)
#        #response = redirect(IndexView.as_view())
#        #response = HttpResponseRedirect('')
#        #response = HttpResponse('')
#        return response
