# Fungsi pencarian linear (sequential search)
def sequential_search(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:   # Jika ditemukan, kembalikan indeks
            return i
    return -1    # Jika tidak ditemukan, kembalikan -1
