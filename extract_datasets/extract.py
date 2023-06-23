# %%
import tabula
from collections import  defaultdict

# Using Raw File Content link (copy path) in GitHub
pdf_path = "extract_datasets/statistical_detail_report_february_2023.pdf"
# "extract_datasets/statistical_detail_report_february_2023.pdf" if running via Run Python


# Reads all pages - keep summary to remove later
all_pages = tabula.read_pdf(pdf_path, pages="1-4", multiple_tables=True)

tables_by_county = defaultdict(list)


for i, table in enumerate(all_pages):
    if set(['Child By Ages', 'Children']) <= set(table.columns):
        # Grabbing county name to combine with table in dictionary
        county = tabula.read_pdf(pdf_path, pages=i+1, area=[40, 80, 100, 200], stream=True)[0].columns[0]
        

        tables_by_county[county].append(table)


print(tables_by_county)

