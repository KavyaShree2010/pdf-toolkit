from pypdf import PdfWriter, PdfReader
import os

def merge_pdfs():
    files = []

    while True:
        name = input("Enter the pdf filename (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        if not os.path.isfile(name):
            print(f"Error: {name} not found. Try again.")
            continue
        if not name.endswith('.pdf'):
            print(f"Error: {name} is not a PDF file.")
            continue

        files.append(name)
    if not files:
        print("No PDF files to merge. Exiting.")
        return

    writer = PdfWriter()

    try:
     for f in files:
        writer.append(f)

     output = input("Enter output filename: ")
     if not output.ednswith('.pdf'):
         output += '.pdf'


     writer.write(output)
     writer.close()

     print(f"PDF files merged successfully into {output}")

    except Exception as e:
        print(f"Something went wrong: {e}")

def pdf_info():
    filename = input("Enter pdf filename: ")
    if not os.path.isfile(filename):
        print(f"Error: {filename} not found.")
        return
    try:
     reader = PdfReader(filename)
     size = os.path.getsize(filename)
     meta = reader.metadata

     print(f"\n--PDF INFO--")
     print(f"Pages     : {len(reader.pages)}")
     print(f"Size      :{round(size/1024, 2)}KB")
     print(f"Title     :{meta.title if meta.title else 'Not Available'}")
     print(f"Author     :{meta.author if meta.author else 'Not Available'}")
     print(f"Creator   :{meta.creator if meta.creator else 'Not Available'}")

    except Exception as e:
        print(f"Something went wrong: {e}")


def main():
    while True:
        print("\n1. Merge PDFs")
        print("\n2. Get PDF Info")
        print("\n3. Exit")

        choice = input(f"\nChoose an option: ").strip()
        if choice == '1':
           merge_pdfs()
        elif choice == '2':
            pdf_info()
        elif choice == '3':
            print("Bye.")
            break  
        else:
            print("Invalid choice. Enter 1, 2 or 3.") 

if __name__ == "__main__":
    main()
    

