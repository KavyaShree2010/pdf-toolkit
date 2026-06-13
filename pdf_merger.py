from pypdf import PdfWriter

pdf1 = input("Enter first pdf name: ")
pdf2 = input("Enter second pdf name: ")

merger = PdfWriter()

merger.append(pdf1)
merger.append(pdf2)

merger.write("merged_pdf.pdf")

merger.close()

print("PDF files merged successfully into 'merged_pdf.pdf'.")