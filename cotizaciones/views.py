from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Cotizacion

def generar_pdf_cotizacion(request, cotizacion_id):
    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    template_path = 'cotizaciones/pdf_template.html'
    context = {'cotizacion': cotizacion}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cotizacion_{cotizacion.id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error al generar PDF')
    return response

# Create your views here.
