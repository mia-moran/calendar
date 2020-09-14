import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("form_letter.pdf",pagesize=A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story=[]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '<font size="12">We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.</font>' % ('jaja', 
                                                                                                'jaja',
                                                                                                'jaja',
                                                                                                'jaja',
                                                                                                'jaja')
Story.append(Paragraph(ptext, styles["Justify"]))
doc.build(Story)