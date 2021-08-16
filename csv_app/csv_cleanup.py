from django.shortcuts import render
from .models import Data
import csv, io

def csv_handler(csv_file):
    io_string = io.StringIO(csv_file)
    next(io_string)
    for row in csv.reader(io_string, delimiter=';', quotechar='|'):

        # Some entries have ';' in their description, omitting this
        while len(row) > 14:
            popped = row.pop()
            row[-1] += '; ' + popped

        # row[13] = row[13] + (';'.join(row[14:]) if len(row)>14 else '')
        # row = row[:14]


        # Bulk variable declaration from row (14 pieces)
        code, name, level1, level2, level3, price, priceSP, quantity, \
                value_fields, joint_purchases, measurment_unit, picture, \
                show_on_mainpage, description = row[:]

        # Removing commas from code variable
        code = code.replace('"', '')

        # Converting comma separated price and priceSP into floats;
        # priceSP string may also contain double cuotes "
        if price:
            price = price.replace('"', '')
            price = float(".".join(price.split(",")))
        else: price = 0

        if priceSP:
            priceSP = priceSP.replace('"', '')
            priceSP = float(".".join(priceSP.split(",")))
        else: priceSP = 0

        # Handling fucked up floating quantity
        quantity = int(round(float(quantity)))

        # measurment_unit may have double double quotes, fixing this
        measurment_unit = measurment_unit.replace('"', '')

        # Cleaning up description
        description = description.replace('"', '')
        description = description.replace(',', ', ')
        description = description.replace(':', ': ')

        # Creating object with variables as Data model fields
        Data.objects.create(code=code, name=name,
                level1=level1, level2=level2, level3=level3,
                price=price, priceSP=priceSP, quantity=quantity,
                value_fields=value_fields, #joint_purchases=joint_purchases,
                measurment_unit=measurment_unit, picture=picture,
                show_on_mainpage=show_on_mainpage, description=description)

#    context = {'data_entries': data_entries}
#    response = render(request, template, context)
#
#    return response
