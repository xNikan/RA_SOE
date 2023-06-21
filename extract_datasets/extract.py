import tabula 

# Using Raw File Content link (copy path) in GitHub
pdf_path = "extract_datasets/statistical_detail_report_february_2023.pdf"

# Grabs county information using area - [y1, x1, y2, x2]
county = tabula.read_pdf(pdf_path, area=[40, 80, 100, 200], stream=True, pages = 2)
data = tabula.read_pdf(pdf_path, area = [110, 10, 1000, 1000], stream=True, pages=2)

print(len(county))


print(county[0].columns[0])
print(data[0])