import csv
import datetime
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("calendar.pdf",pagesize=A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

w, h = A4

def get_activities(dates):
    activities = []
    with open('archivo.csv', newline='') as File:  
        reader = csv.DictReader(File, delimiter=';')
        for activity in reader:
            date_ = activity['date'].split('/')
            date_ = datetime.date(int(date_[2]), int(date_[1]), int(date_[0]))
        
            if(date_ in dates):
                #print("{} \t {} \t {} \t {} \t {}\n".format(activity['area'], activity['title'], activity['date'], activity['color'], activity['desc']))
                activity = Activity_(activity['area'], activity['title'], activity['date'], activity['color'], activity['desc'])
                activities.append(activity)
    return activities



class Activity_:
    def __init__(self, area_, title_, date_, color_, desc_):
        self.area = area_
        self.title = title_
        self.date = date_
        self.color = color_
        self.desc = desc_



activities = get_activities([datetime.date(2020, 9, 14), datetime.date(2020, 9, 15)])
Story = []
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
for a in activities:
    
    ptext = '<font size="12">{}: {}</font>'.format(a.area, a.title)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = "{}".format(a.desc)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

doc.build(Story)