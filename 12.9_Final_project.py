import pandas
import matplotlib.pyplot as plt


def read_sales_data(file_path='./data_for_chapter_12.xlsx'):
    excel_data = pandas.read_excel(file_path, usecols=['id', 'title', 'quantity', 'price', 'date'])
    normal_data = excel_data.to_dict(orient='records')
    return normal_data


def total_sales_per_product(sales_data):
    total_sales_product = dict()
    for row in sales_data:
        if row['title'] in total_sales_product:
            total_sales_product[row['title']] += (row['quantity'] * row['price'])
        else:
            total_sales_product[row['title']] = (row['quantity'] * row['price'])
    return total_sales_product


def sales_over_time(sales_data):
    total_sales_date = dict()
    for row in sales_data:
        if row['date'] in total_sales_date:
            total_sales_date[row['date']] += (row['quantity'] * row['price'])
        else:
            total_sales_date[row['date']] = (row['quantity'] * row['price'])
    return total_sales_date

def dict_to_lists(dict):
    keys = []
    values = []
    for key, value in dict.items():
        keys.append(key)
        values.append(value)
    return keys, values


if __name__ == '__main__':
    sales_data = read_sales_data()

    product_sales = total_sales_per_product(sales_data)
    max_key_product_sales = max(product_sales, key=product_sales.get)
    print(f'Товар с наибольшей выручкой: {max_key_product_sales}, '
          f'выручка составила {product_sales[max_key_product_sales]}')

    data_sales = sales_over_time(sales_data)
    max_key_data_sales = max(data_sales, key=data_sales.get)
    print(f'Наибольшая выручка была {max_key_data_sales}, '
          f'она составила {data_sales[max_key_data_sales]}')

    product, sales = dict_to_lists(product_sales)
    day, day_sales = dict_to_lists(data_sales)

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(product, sales, 'g--')
    axs[1].plot(day, day_sales, 'b-')
    plt.show()