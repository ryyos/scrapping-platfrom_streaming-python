import os
# Mengimpor fungsi make_link_page dari direktori bunker.create_link
from bunker.create_link import make_link_page

# Mengimpor fungsi take_all_sc dari direktori bunker.link_card
from bunker.link_card import take_all_sc

# Memeriksa apakah skrip ini sedang dijalankan sebagai main utama
if __name__ == '__main__':
    # Membuat direktori untuk menyimpan hasil scraping
    os.mkdir('result')
    # Memanggil fungsi make_link_page dengan parameter URL 'https://otakudesu.lol/complete-anime/'
    link = make_link_page('https://otakudesu.lol/complete-anime/')

    # Memanggil fungsi take_all_sc dengan parameter link (yang dihasilkan dari make_link_page)
    take_all_sc(link)
