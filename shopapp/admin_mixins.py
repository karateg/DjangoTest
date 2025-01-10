import csv
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.db.models.options import Options


class Export_goods_mixin:
    def export_csv(self, requst:HttpRequest, qveryset: QuerySet):
        meta: Options = self.model._meta
        fields_name = [field.name for field in meta.fields]

        response = HttpResponse(content_type= 'text/csv')
        response['Content-Disposition'] = f'attachment; filename= {meta}-export.csv'

        csv_writer = csv.writer(response)

        csv_writer.writerow(fields_name)

        for row in qveryset:
            csv_writer.writerow([getattr(row, field) for field in fields_name])
        return response
    export_csv.short_discription = 'Выгрузка в csv файл'