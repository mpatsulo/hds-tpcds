import os
import re

def replace_words_in_file(input_path, output_path, words, prefix):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()
    for word in words:
        pattern = rf'\b{word}\b'
        print(pattern)
        replacement = f'{prefix}{word}'
        print(replacement)
        content = re.sub(pattern, replacement, content)
        if word == "template_db.":
            _content = content.replace("template_db.", "")
        else:
            _content=content
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(_content)

def process_sql_files(input_directory, output_directory, words, prefix):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
   # ,49,51,78
    print(os.listdir(input_directory))
    for filename in os.listdir(input_directory):
        if filename.endswith('.sql'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            if  (filename in ["q31.sql","q49.sql", "q51.sql", "q78.sql"]):
                replace_words_in_file(input_path, output_path, ["template_db."], prefix)
            else:    
                replace_words_in_file(input_path, output_path, words, prefix)


input_directory = './queries'
output_directory = './patch' 
words = [
 'date_dim',
 'catalog_sales',
 'catalog_returns',
 'inventory',
 'store_sales',
 'store_returns',
 'web_sales',
 'web_returns',
 'call_center',
 'catalog_page',
 'customer',
 'customer_address',
 'customer_demographics',
 'household_demographics',
 'income_band',
 'item',
 'promotion',
 'reason',
 'ship_mode',
 'store',
 'time_dim',
 'warehouse',
 'web_page',
 'web_site'
]
prefix = "tpcds_sf1."

if __name__ == "__main__":
    process_sql_files(input_directory, output_directory, words, prefix)
    print("patch complete")
