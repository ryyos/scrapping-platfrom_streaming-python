# Fungsi untuk membuat daftar tautan halaman
def make_link_page(tautan):
    # Membuat list kosong untuk menampung tautan-tautan halaman
    list_link = []

    # Melakukan perulangan dari 1 hingga 51
    for num_page in range(1, 52):
        # Membuat string 'page/nomor_halaman' menggunakan f-string
        page = f'page/{num_page}'

        # Menggabungkan tautan utama dengan string halaman yang dibuat
        link_page = tautan + page

        # Menambahkan tautan halaman yang sudah dibuat ke dalam list_link
        list_link.append(link_page)

    # Mengembalikan list tautan halaman yang telah dibuat
    return list_link
