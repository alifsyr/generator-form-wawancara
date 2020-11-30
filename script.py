# Create Document
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.lib.pagesizes import portrait, A5
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import csv

def docs(document,title,choice,nama,panggilan,fakultas,jurusan,alasan_pertanyaan,jawaban,keunikan,bukti,deskripsi_penjelasan):
    if (choice == "maus"):
        document.append(Paragraph(title, ParagraphStyle(name = 'title',fontName = 'Times-New-Roman-Bold',fontSize = 12, alignment = TA_CENTER)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('1. Nama Lengkap\t: '+nama, ParagraphStyle(name = 'nama',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('2. Nama Panggilan\t: '+panggilan, ParagraphStyle(name = 'panggilan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('3. Jurusan\t: '+jurusan, ParagraphStyle(name = 'fakultas',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('4. Keunikan Diri\t: '+keunikan, ParagraphStyle(name = 'alasan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('5. Pertanyaan Bebas\t: '+'('+alasan_pertanyaan+') '+jawaban, ParagraphStyle(name = 'keunikan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('6. Bukti Wawancara\t: ', ParagraphStyle(name = 'bukti',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Image('image/'+bukti+'.png', 11*cm,7*cm))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('7. Penjelasan Singkat/Rangkuman\t: '+deskripsi_penjelasan, ParagraphStyle(name = 'keunikan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
    elif (choice == "prosus"):
        document.append(Paragraph(title, ParagraphStyle(name = 'title',fontName = 'Times-New-Roman-Bold',fontSize = 12, alignment = TA_CENTER)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('1. Nama Lengkap\t: '+nama, ParagraphStyle(name = 'nama',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('2. Nama Panggilan\t: '+panggilan, ParagraphStyle(name = 'panggilan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('3. Fakultas\t: '+fakultas, ParagraphStyle(name = 'fakultas',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('4. Alasan Masuk US\t: '+alasan_pertanyaan, ParagraphStyle(name = 'alasan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('5. Keunikan Diri\t: '+keunikan, ParagraphStyle(name = 'keunikan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('6. Bukti Wawancara\t: ', ParagraphStyle(name = 'bukti',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Image('image/'+bukti+'.png', 11*cm,7*cm))
        document.append(Spacer(0*cm,0.5*cm))
        document.append(Paragraph('7. Deskripsi Singkat\t: '+deskripsi_penjelasan, ParagraphStyle(name = 'keunikan',fontName = 'Times-New-Roman',fontSize = 12)))
        document.append(Spacer(0*cm,0.5*cm))


    return document

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [row for row in reader]

for i in data:
    pdfmetrics.registerFont(TTFont('Times-New-Roman', 'font/LiberationSerif-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Times-New-Roman-Bold', 'font/LiberationSerif-Bold.ttf'))
    document                = []


    if (i[1] != "Nama Lengkap"):
        if (i[0] == "prosus"):
            title = "Wawancara PROSUS 2020"
            document = docs(document,title,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
            fileName    = i[1]+'_'+i[3]+'.pdf'
            SimpleDocTemplate(fileName, pagesize = portrait(A5), rightMargin = 1.27*cm, leftMargin = 1.27*cm, topMargin = 1.27*cm, bottomMargin = 1.27*cm).build(document)

        elif (i[0] == "maus"):
            title = "Wawancara MaUS 2020"
            document = docs(document,title,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
            fileName    = i[1]+'_'+i[3]+'.pdf'
            SimpleDocTemplate(fileName, pagesize = portrait(A5), rightMargin = 1.27*cm, leftMargin = 1.27*cm, topMargin = 1.27*cm, bottomMargin = 1.27*cm).build(document)
