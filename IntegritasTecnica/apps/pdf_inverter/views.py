from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFUploadForm
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import io


def invert_pdf_colors(pdf_path):
    writer = PdfWriter()

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_image = page.extract_text()
        writer.add_page(page)

    # Guardar el nuevo PDF en un archivo en memoria
    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)

    return output_pdf


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            # Invertir los colores del PDF
            inverted_pdf = invert_pdf_colors(pdf_file)

            response = HttpResponse(inverted_pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="inverted.pdf"'
            return response
    else:
        form = PDFUploadForm()

    return render(request, 'pdf_inverter/upload.html', {'form': form})
