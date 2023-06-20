import tabula 

pdf_path = "https://ncchildcare.ncdhhs.gov/Portals/0/documents/pdf/S/statistical_detail_report_january_2023.pdf?ver=riAf-R0YKU1jM35CmNtYdQ%3d%3d"

dfs = tabula.read_pdf(pdf_path, stream=True)

print(len(dfs))
print(dfs[0])