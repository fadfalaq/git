data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    }
}

print("Seluruh data panen:")
for lokasi, data in data_panen.items():
    print(f"{lokasi}: {data}")

jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print("\nJumlah hasil panen jagung dari lokasi2:", jagung_lokasi2)

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print("\nNama lokasi dari lokasi3:", nama_lokasi3)

hasil_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}
print("\nJumlah hasil panen padi per lokasi:", hasil_padi)
print("Jumlah hasil panen kedelai per lokasi:", hasil_kedelai)

for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {data['nama_lokasi']} dalam kondisi baik.")

# konflik