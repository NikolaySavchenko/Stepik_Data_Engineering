import pandas
import openpyxl

def read_sales_data(file_path='./data_for_chapter_12.xlsx'):
    excel_data = pandas.read_excel(file_path)
    json_data = excel_data.to_json(orient='records', force_ascii=False)
    return json_data



def total_sales_per_product(sales_data):
    pass


def sales_over_time(sales_data):
    pass


if __name__ == '__main__':
    print(read_sales_data())