# Mengimpor modul-modul yang diperlukan
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bunker.write import write_data
from bunker.write import write_all_page
from time import sleep
import pandas
import os
from bs4 import BeautifulSoup

# Fungsi untuk menggabungkan data dari semua halaman


def data_all_page(pieces, all_data_page, page):
    all_data_page += pieces
    # Jika halaman terakhir dicapai (halaman 51), panggil fungsi untuk menulis semua data
    if page == 51:
        write_all_page(all_data_page)

# Fungsi untuk mengambil data dari card


def take_data(link_card, page, all_data_page):
    # Inisialisasi list untuk menyimpan hasil data dari setiap card
    result_data = []
    nomor = 1
    for card_link in link_card:

        # Membuka page yang diakses menggunakan driver Chrome
        driver2.get(card_link)
        # Mengambil seluruh sumber code page
        sc = driver2.page_source

        all_data = BeautifulSoup(sc, 'html.parser')

        div = all_data.find('div', attrs={'class': 'infozin'})

        data = div.find_all('p')
        # Menggunakan list unpacking untuk memisahkan data
        [judul, japanese, score, produser, tipe, status, total, durasi,
         tanggal, studio, genre] = data

        # Menambahkan data ke dalam dictionary result_data
        result_data.append({
            f'Judul   ': judul.get_text()[7:],
            u'Japanese': japanese.get_text()[10:],
            f'Score   ': score.get_text()[6:],
            f'Produser': produser.get_text()[10:],
            f'Tipe    ': tipe.get_text()[6:],
            f'Status  ': status.get_text()[8:],
            f'Total   ': total.get_text()[15:],
            f'Durasi  ': durasi.get_text()[8:],
            f'Tanggal ': tanggal.get_text()[15:],
            f'Studio  ': studio.get_text()[8:],
            f'Genre   ': genre.get_text()[7:]
        })

        print(f'Card {nomor} : done')
        print('='*50)
        nomor += 1
        driver2.close()

    # Menulis data hasil scraping ke dalam file dan menggabungkan data dari semua halaman
    write_data(result_data, page)
    data_all_page(result_data, all_data_page, page)
