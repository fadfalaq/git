import pandas as pd

def buat_dataframe():
    data = {
        "Kabupaten/Kota": [
            "Bandung", "Bogor", "Bekasi", "Cimahi", "Depok",
            "Bandung", "Bogor", "Bekasi", "Cimahi", "Depok",
        ],
        "Tahun": [2021, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2022],
        "Produksi Sampah (ton)": [500000, 450000, 600000, 150000, 300000, 520000, 470000, 610000, 160000, 310000],
    }
    return pd.DataFrame(data)

def hitung_total_tahun_tertentu(df, tahun):
    total = df[df["Tahun"] == tahun]["Produksi Sampah (ton)"].sum()
    print(f"\nTotal produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun {tahun}: {total} ton")
    return total

def hitung_total_per_tahun(df):
    total = df.groupby("Tahun")["Produksi Sampah (ton)"].sum()
    print("\nTotal produksi sampah per tahun:")
    print(total)
    return total

def hitung_total_per_kota_per_tahun(df):
    total = df.groupby(["Kabupaten/Kota", "Tahun"])["Produksi Sampah (ton)"].sum()
    print("\nTotal produksi sampah per Kabupaten/Kota per tahun:")
    print(total)
    return total

if __name__ == "__main__":
    df = buat_dataframe()
    print("DataFrame:")
    print(df)
    
    tahun_tertentu = 2021
    hitung_total_tahun_tertentu(df, tahun_tertentu)
    hitung_total_per_tahun(df)
    hitung_total_per_kota_per_tahun(df)
