from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='a4')
pdf.add_font("Myfont",'', "Times New Roman Regular.ttf")

df=pd.read_csv('topics.csv')


for index, row in df.iterrows():
    topic = row['Topic']
    topic_pages=row['Pages']

    pdf.add_page()

    pdf.set_font("Times", 'B', 14)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, text=topic, align='L')
    pdf.line(10, 22, 200, 22)

    for i in range(topic_pages - 1):
        pdf.add_page()




pdf.output("notebook.pdf")
