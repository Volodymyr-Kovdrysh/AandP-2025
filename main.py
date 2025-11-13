from fpdf import FPDF
import qrcode

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FONTS_DIR = BASE_DIR / "fonts"
IMAGES_DIR = BASE_DIR / "images"

print(BASE_DIR)

def make_qr(text, filename= IMAGES_DIR / "qr.png"):
    qr = qrcode.QRCode(
        version=None,      # автоматично підбере розмір
        box_size=10,       # розмір "квадратика"
        border=2,          # рамка навколо коду
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="yellow")
    img.save(filename)
    return filename


qr_path = make_qr("https://github.com/Volodymyr-Kovdrysh/AandP-2025")

pdf = FPDF(orientation='P', unit='mm', format='a4')
pdf.set_auto_page_break(False,0)

pdf.add_font("Myfont",'', FONTS_DIR / "Times New Roman Regular.ttf")
pdf.add_font("Kobzar",'', FONTS_DIR / "KobzarKS_v1-020.otf")


df=pd.read_csv('topics.csv')

total_pages = 0
for index, row in df.iterrows():
    topic = row['Topic']
    topic_pages=row['Pages']

    pdf.add_page()
    total_pages += 1

    #header
    pdf.set_font("Times", 'I', 26)
    pdf.set_text_color(0, 100, 100)
    pdf.cell(w=0, h=12, text=topic, align='L')
    pdf.line(10, 20, 200, 20)

    #lines
    with pdf.local_context(stroke_opacity=0.3):  # прозорі лінії
        pdf.set_draw_color(220, 220, 220)
        pdf.set_line_width(0.1)
        for y in range(20, 290, 10):
            pdf.line(10, y, pdf.w - pdf.r_margin, y)


    #watermark
    with pdf.local_context(fill_opacity=0.1):
        pdf.image(IMAGES_DIR / "CE.png", x=pdf.w / 2 - 70, y=pdf.h / 2 - 70, w=140)


    #footer
    pdf.ln(275)

    pdf.set_dash_pattern(dash=3, gap=4)
    pdf.set_line_width(1)
    pdf.line(10, 285, 200, 285)
    pdf.set_dash_pattern()
    pdf.set_line_width(0.2)


    pdf.set_font("Times", 'I', 12)
    pdf.set_text_color(0,0,200)
    pdf.cell(w=0, h=12, text=f"{topic} {1}/{topic_pages}", align='R', new_x="LMARGIN")
    pdf.set_font("Times", 'B', 18)
    pdf.cell(w=0, h=12, text=f"{total_pages}", align='C')


    for i in range(topic_pages - 1):
        pdf.add_page()
        total_pages += 1

        # lines
        with pdf.local_context(stroke_opacity=0.3):  # прозорі лінії
            pdf.set_draw_color(220, 220, 220)
            pdf.set_line_width(0.1)
            for y in range(20, 290, 10):
                pdf.line(10, y, pdf.w - pdf.r_margin, y)

        # footer
        pdf.ln(275)

        pdf.set_dash_pattern(dash=3, gap=4)
        pdf.set_line_width(1)
        pdf.line(10, 285, 200, 285)
        pdf.set_dash_pattern()
        pdf.set_line_width(0.2)

        pdf.set_font("Times", 'I', 12)
        pdf.set_text_color(0, 0, 200)
        pdf.cell(w=0, h=12, text=f"{topic} {i+2}/{topic_pages}", align='R', new_x="LMARGIN")
        pdf.set_font("Times", 'B', 18)
        pdf.cell(w=0, h=12, text=f"{total_pages}", align='C')

        # watermark
        with pdf.local_context(fill_opacity=0.1):
            pdf.image(IMAGES_DIR / "CE.png", x=pdf.w / 2 - 70, y=pdf.h / 2 - 70, w=140)

pdf.add_page()

pdf.set_font("Myfont",'', 14)
pdf.cell(w=0, h=12, text=f"Розміри A4: ширина-{round(pdf.w,2)}мм, висота-{round(pdf.h,2)}мм", align='L', new_x="LMARGIN", new_y="NEXT")
pdf.cell(w=0, h=12, text=f"Поля A4: ліве-{round(pdf.l_margin,2)}мм, верхнє-{round(pdf.t_margin,2)}мм, праве-{round(pdf.r_margin)}, нижнє-{round(pdf.b_margin,2)}", align='L', new_x="LMARGIN", new_y="NEXT")
pdf.cell(w=0, h=12, border=1, text=f"1pt={round(1 / pdf.k,2)}мм, 1mm={round(pdf.k,2)}pt", align='L', new_x="LMARGIN", new_y="NEXT")
pdf.multi_cell(w=0, h=7, border=1, text=f"{'Дуже довгий текст. '* 10}", new_x="LMARGIN", new_y="NEXT")

lines = [
    "Як умру, то поховайте",
    "Мене на могилі,",
    "Серед степу широкого,",
    "На Вкраїні милій ..."
]

pdf.set_font("Kobzar", '', 32)
pdf.ln(25)

for line in lines:
    pdf.cell(w=0, h=8, text=line, align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.cell(w=0, h=12, text="Тарас ШЕВЧЕНКО", align='R', new_x="LMARGIN", new_y="NEXT")


pdf.image(IMAGES_DIR / "qr.png", x=pdf.w - pdf.r_margin - 140, y=pdf.h - pdf.b_margin - 140, w=140)

pdf.output("notebook.pdf")
