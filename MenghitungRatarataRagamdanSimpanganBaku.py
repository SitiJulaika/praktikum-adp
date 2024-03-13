import math

# Fungsi untuk menghitung rata-rata
def hitung_rata_rata(data):
    return sum(data) / len(data)

# Fungsi untuk menghitung ragam
def hitung_ragam(data):
    rata_rata = hitung_rata_rata(data)
    jumlah = 0
    for nilai in data:
        jumlah += (nilai - rata_rata) ** 2
    return jumlah / len(data)

# Fungsi untuk menghitung simpangan baku
def hitung_simpangan_baku(data):
    return math.sqrt(hitung_ragam(data))

# Input data dari keyboard
def input_data():
    data = []
    jumlah_data = int(input("Masukkan jumlah data: "))
    for i in range(jumlah_data):
        nilai = float(input(f"Masukkan data ke-{i+1}: "))
        data.append(nilai)
    return data

def main():
    data = input_data()
    rata_rata = hitung_rata_rata(data)
    ragam = hitung_ragam(data)
    simpangan_baku = hitung_simpangan_baku(data)
    
    print("\nHasil:")
    print("Rata-rata:", rata_rata)
    print("Ragam:", ragam)
    print("Simpangan baku:", simpangan_baku)

if __name__ == "__main__":
    main()

    