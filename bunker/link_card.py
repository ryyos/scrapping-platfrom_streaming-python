# Mengimpor modul-modul yang diperlukan
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bunker.steal import take_data
from bs4 import BeautifulSoup

# Fungsi untuk mengambil data dari semua page


def take_all_sc(link_page):
    # Menginisialisasi variabel page dan all_data_page
    page = 1
    all_data_page = []

    # Iterasi melalui setiap tautan page dalam link_page
    for create_link_page in link_page:
        # Mengatur layanan Chrome WebDriver
        apk = Service(executable_path='bunker/chromedriver.exe')

        # Membuat objek opsi Chrome WebDriver
        setting = Options()

        # Menonaktifkan logging dan mengatur Chrome dalam mode headless
        setting.add_experimental_option("excludeSwitches", ["enable-logging"])
        setting.add_argument('--headless')

        # Inisialisasi objek driver Chrome dengan pengaturan yang telah ditentukan
        driver = webdriver.Chrome(service=apk, options=setting)

        # Membuka page yang diakses menggunakan driver Chrome
        driver.get(create_link_page)

        # Mengambil seluruh sumber code page
        all_sc = driver.page_source

        # Menampilkan pesan bahwa page sedang di-scrapping
        print(f'scrapping page {page}')

        # Memanggil fungsi take_link_card untuk mengambil data card dari page
        [all_data, nomor] = take_link_card(all_sc, page)

        # Memanggil fungsi take_data untuk memproses data yang diambil
        take_data(all_data, page, all_data_page)

        # Menaikkan nomor page dan menutup driver Chrome
        page += 1
        driver.close()

# Fungsi untuk mengambil tautan card dari page


def take_link_card(all_sc, page):
    card = 1
    sc = BeautifulSoup(all_sc, 'html.parser')

    # Mengambil elemen <ul> ke-3 dari sumber code page
    ul = sc.find_all('ul')[2]

    link_card = []
    # Iterasi melalui setiap elemen <li> dalam elemen <ul>
    for li in ul.find_all('li'):
        # Mengambil tautan dari elemen <a>
        link = li.find('a').get('href')

        # Menambahkan tautan ke dalam list link_card
        link_card.append(link)

        # Menaikkan nomor card
        card += 1
    return [link_card, page]
