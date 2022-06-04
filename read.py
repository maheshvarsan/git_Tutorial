from docx import Document
doc = Document('F:/sampleprogram/New_Arrival_Cars/asserts/media/Mahesh_resume_chennai_Fs3ttbU.docx')
for para in doc.paragraphs:
    print(para.text)