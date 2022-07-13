import csv
import io

from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import xlwt

from .models import Categoria, Produto


def exporta_para_xlsx(model, filename, queryset, columns):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(model)

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    default_style = xlwt.XFStyle()

    rows = queryset
    for row, row_data in enumerate(rows):
        row_num += 1
        for col, val in enumerate(row_data):
            ws.write(row_num, col, val, default_style)

    wb.save(response)
    return response


def exporta_categoria(request):
    MDATA = datetime.now().strftime("%Y-%m-%d")
    model = 'Categoria'
    filename = 'Categoria_exportada.xls'
    _fillename = filename.split('.')
    filename_final = f'{_fillename[0]}_{MDATA}.{_fillename[1]}'
    queryset = Categoria.objects.all().values_list('id', 'descricao')
    columns = ('ID', 'DESCRIÇÃO', )
    response = exporta_para_xlsx(model, filename_final, queryset, columns)
    return response

def exporta_produto(request):
    MDATA = datetime.now().strftime("%Y-%m-%d")
    model = 'Produto'
    filename = 'Produto_exportada.xls'
    _fillename = filename.split('.')
    filename_final = f'{_fillename[0]}_{MDATA}.{_fillename[1]}'
    queryset = Produto.objects.all().values_list('id', 'descricao', 'preco')
    columns = ('ID', 'DESCRIÇÃO', 'PREÇO')
    response = exporta_para_xlsx(model, filename_final, queryset, columns)
    return response


def save_data(data):
    print("data", data)
    aux = []
    for item in data:
        descricao = item.get('descricao')
        created_at = item.get('create_at')
        uc_id = item.get('uc_id')
        um_id = item.get('um_id')
        updated_at = item.get('updated_at')

        obj = Categoria(
            descricao=descricao,
            created_at=created_at,
            uc_id=uc_id,
            um_id=um_id,
            updated_at=updated_at,
        )
        aux.append(obj)

    Categoria.objects.bulk_create(aux)


def import_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']   
        file = myfile.read().decode('utf8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('categoria:categoria_list'))

    template_name = 'categoria_import.html'
    return render(request, template_name)