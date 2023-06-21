import tabula 

pdf_path = "https://github.com/xNikan/RA_SOE/blob/main/extract_datasets/statistical_detail_report_february_2023.pdf"

dfs = tabula.read_pdf(pdf_path, stream=True)

print(len(dfs))
#print(dfs[0])