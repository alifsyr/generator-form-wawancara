# Create Document
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.lib.pagesizes import portrait, A5
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def docs(document, title, nama, panggilan, fakultas, alasan, keunikan, bukti, deskripsi):
    document.append(Paragraph(title, ParagraphStyle(name = 'title',fontName = 'Times-New-Roman-Bold',fontSize = 11, alignment = TA_CENTER)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('1. Nama Lengkap\t: '+nama, ParagraphStyle(name = 'nama',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('2. Nama Panggilan\t: '+panggilan, ParagraphStyle(name = 'panggilan',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('3. Fakultas\t: '+fakultas, ParagraphStyle(name = 'fakultas',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('4. Alasan Masuk US\t: '+alasan, ParagraphStyle(name = 'alasan',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('5. Keunikan Diri\t: '+keunikan, ParagraphStyle(name = 'keunikan',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('6. Bukti Wawancara\t: ', ParagraphStyle(name = 'bukti',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Image('foto/'+bukti+'.png', 11*cm,7*cm))
    document.append(Spacer(0*cm,0.5*cm))
    document.append(Paragraph('7. Deskripsi Singkat\t: '+deskripsi, ParagraphStyle(name = 'keunikan',fontName = 'Times-New-Roman',fontSize = 11)))
    document.append(Spacer(0*cm,0.5*cm))


    return document

endprogram = False
while (not endprogram):
    pdfmetrics.registerFont(TTFont('Times-New-Roman', 'font/LiberationSerif-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Times-New-Roman-Bold', 'font/LiberationSerif-Bold.ttf'))
    document                = []

    title                   = 'Wawancara PROSUS 2020'
    nama                    = input("Nama lengkap narasumber : ")
    panggilan               = input("Nama panggilan narasumber : ").capitalize()
    fakultas                = input("Fakultas narasumber : ").upper()
    alasan                  = input("Alasan Masuk US : ").capitalize()
    keunikan                = input("Keunikan Diri : ").capitalize()
    deskripsi               = input("Deskripsi Singkat : ").capitalize()
    bukti                   = input("nama file bukti wawancara (.jpg) : ")

    document = docs(document, title, nama, panggilan,fakultas,alasan,keunikan,bukti,deskripsi)
    fileName    = nama+'_'+fakultas+'.pdf'
    SimpleDocTemplate(fileName, pagesize = portrait(A5), rightMargin = 1.27*cm, leftMargin = 1.27*cm, topMargin = 1.27*cm, bottomMargin = 1.27*cm).build(document)
    makenew                    = input("Apakah ingin memasukan data lagi ? (Y/N) :").upper()
    if (makenew == "N"):
        exit()