from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(metrics, chart_file='views.png', output_file='report.pdf'):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height-50, "Telegram Channel Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    for key, value in metrics.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20

    # Добавляем график
    try:
        c.drawImage(chart_file, 50, y-250, width=500, height=250)
    except:
        pass

    c.save()
