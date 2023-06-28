# %%
import tabula
import pandas as pd
from collections import  defaultdict

# Using Raw File Content link (copy path) in GitHub
pdf_path = "extract_datasets/statistical_detail_report_february_2023.pdf"
# "extract_datasets/statistical_detail_report_february_2023.pdf" if running via Run Python


# Reads all pages - keep summary to remove later
all_pages = tabula.read_pdf(pdf_path,pages="1-4",area=[60, 0, 1000, 1000], stream=True) # area=[95, 0, 1000, 1000]
print(all_pages)
tables_by_county = defaultdict(list)
new_columns = ["ID", "operation_name", "ind_month", "infant", \
               "age1", "age2", "age3", "age4", "age5", \
               "age5_12", "enrollment_total", "licensed_capacity", "max_capacity",\
               "no_emp", "category_operation", "operation_site", "scc"]

#print(all_pages[0])
for i, table in enumerate(all_pages):
    print(table.columns)
    if all(col.startswith('Unnamed') for col in table.columns):
        continue
    else:
        #print(table)
        # Grabbing county name to combine with table in dictionary
       # table.columns = table.iloc[0]
        
        #table = table.iloc[1:]
        print("here")
        #table.reset_index(drop=True, inplace=True)
     #   print(table)
       # print(table['Emp. Operation'].str)
      #  table['Emp. Operation'] = table['Emp. Operation'].fillna('NA NA')
        #print(table)

     #   table_str = table.iloc()

       # table[['p1', 'p2']] = table_str.split(" ", expand=True)


    #    table.columns = new_columns
        county = tabula.read_pdf(pdf_path, pages=i+1, area=[40, 80, 100, 200], stream=True)[0].columns[0]
        table.loc[:, 'county'] = county
        #table = table[1:]


        tables_by_county[county].append(table)

#print(tables_by_county)

#print(len(tables_by_county))

# # Grab all dfs, add to one list to easily transfer into excel
all_tables = [table for tables in tables_by_county.values() for table in tables]
df = pd.concat(all_tables)

df.to_excel('yrly_pdf_data.xlsx', engine='xlsxwriter')


