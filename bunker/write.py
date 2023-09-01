import pandas
import json
import os

# Fungsi untuk menulis data hasil scraping ke dalam format JSON, CSV dan EXCEL


def write_data(result_data, page):
    # Membuat direktori untuk menyimpan hasil data per page
    os.mkdir(f'result/result_{page}')

    # Menulis data ke dalam file JSON
    with open(f'result/result_{page}/result_{page}.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, ensure_ascii=False)

    # Membaca data JSON dan menyimpannya sebagai file CSV
    pandas.read_json(f'result/result_{page}/result_{page}.json').to_csv(
        f'result/result_{page}/result_{page}.csv')

    # Membaca data JSON dan menyimpannya sebagai file Excel (XLSX)
    df = pandas.read_json(f'result/result_{page}/result_{page}.json')
    df.index = df.index.rename('No')
    df.index = df.index + 1
    df.to_excel(f'result/result_{page}/result_{page}.xlsx')

# Fungsi untuk menulis data hasil scraping dari semua page ke dalam format JSON, CSV dan EXCEL


def write_all_page(result_all_data):
    # Membuat direktori untuk menyimpan hasil data dari semua page
    os.mkdir(f'result/result_all_data')

    # Menulis data ke dalam file JSON
    with open(f'result/result_all_data/result_all_data.json', 'w', encoding='utf-8') as file:
        json.dump(result_all_data, file, ensure_ascii=False)

    # Membaca data JSON dan menyimpannya sebagai file CSV
    pandas.read_json(f'result/result_all_data/result_all_data.json').to_csv(
        f'result/result_all_data/result_all_data.csv')

    # Membaca data JSON dan menyimpannya sebagai file Excel (XLSX)
    df = pandas.read_json(f'result/result_all_data/result_all_data.json')
    df.index = df.index.rename('No')
    df.index = df.index + 1
    df.to_excel(f'result/result_all_data/result_all_data.xlsx')
