# Fungsi pengurutan bubble sort
def bubble_sort(data, key=None, ascending=True):
    n = len(data)
    result = data.copy()   # Salin data agar tidak merusak aslinya

    for i in range(n):
        for j in range(0, n - i - 1):
            # Ambil nilai yang akan dibandingkan
            a = result[j][key] if key else result[j]
            b = result[j + 1][key] if key else result[j + 1]
            
             # Tukar jika tidak urut (menyesuaikan ascending/descending)
            if (ascending and a > b) or (not ascending and a < b):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result
