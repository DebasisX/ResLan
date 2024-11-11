from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]  
else:
    print("No filename provided.")
pdf_path = filename
c = canvas.Canvas(pdf_path, pagesize=A4)

spacing = 730
flag = False
while flag == False:
    text = input(str()) 
    tokens = text.split()
    print(tokens)
    if "stop" in tokens:
        print("Saving and closing.")
        flag = True     
    if not flag == True:
        c.drawString(100, spacing, text)
    spacing = spacing - 15
c.save()
print("Done.")
# type: ignore