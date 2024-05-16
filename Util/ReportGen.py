from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.pdfgen import canvas as canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from io import BytesIO
# from 

class ReportGen:

    date = str(datetime.now().date())

    def createReport(self, data, baseName):
        self.fileName = f"{baseName}_report_{self.date}.pdf"
        # can = canvas.Canvas(self.fileName)
        pdf = SimpleDocTemplate(
                    self.fileName,
                    pageSize=A4,
                    )
        
        #Creating a table for the report
        table = Table(data)

        #Setting the style of the table
        style = [
                    ('BACKGROUND', (0,0), (-1,0), colors.green),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                    ('ALIGN',(0,0),(-1,0),'CENTER'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,0), 12),
                ]
        
        rownum = len(data)
        for row in range(1, rownum):
            if len(data) % 2 == 0:
                bc = colors.lightgrey
            else:
                bc = colors.whitesmoke
            style.append( ('BACKGROUND', (0,row), (-1,row), bc) )

        tableStyle = TableStyle(style)
        table.setStyle(tableStyle)
        elems = []
        elems.append(table)
        pdf.build(elems)
        print(f"Report generated successfully. File: {self.fileName}")
        



