import requests
import bs4
"""
Method = fungsi
Field / Atrribute = variabel
Constructor = method yang dipanggil pertama kali saat object diciptakan. Gunakan untuk mendeklarasikan semua field
 pada class ini
"""


class Bencana:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url

    def tampilkan_keterangan(self):
        print(self.description)

    def scraping_data(self):
        print('scraping_data not yet implemented')

    def tampilkan_data(self):
        print('tampilkan_data not yet implemented')

    def run(self):
        self.scraping_data()
        self.tampilkan_data()


class BanjirTerkini(Bencana):
    def __init__(self, url):
        super(BanjirTerkini, self).__init__(url,
                                            'NOT YET IMPLEMENTED, but it should return last flood in Indonesia')
    def tampilkan_keterangan(self):
        print(f'UNDER CONSTRUCTION {self.description}')

class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url,'To get the latest earthquake in Indonesia from BMKG.go.id')

    def scraping_data(self):
        """
        Tanggal: 24 Agustus 2021
        Waktu: 12:05:52 WIB
        Magnitudo: 4.0
        Kedalaman: 40 km
        Lokasi: LS=1.48  BT=134.01
        Pusat Gempa: Pusat gempa berada di darat 18 km barat laut Ransiki
        Dirasakan: Dirasakan (Skala MMI): II-III Manokwari, II-III Ransiki
        :return:
        """
        try:
            content = requests.get(self.url)
        except Exception:
            return None

        if content.status_code == 200:
            soup = bs4.BeautifulSoup(content.text, 'html.parser')

            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            tanggal = result[0]
            waktu = result[1]

            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')
            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            lokasi = None
            dirasakan = None

            for res in result:
                if i == 1:
                    magnitudo = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    lokasi = res.text
                elif i == 5:
                    dirasakan = res.text
                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini")
            return

        print('Gempa Terakhir berdasarkan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"Koordinat: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Dirasakan {self.result['dirasakan']}")


if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini('https://bmkg.go.id')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()

    banjir_di_indonesia = BanjirTerkini('NOT YET')
    banjir_di_indonesia.tampilkan_keterangan()
    banjir_di_indonesia.run()

    daftar_bencana = [gempa_di_indonesia, banjir_di_indonesia]
    print('\nSemua bencana yang ada')
    for bencana in daftar_bencana:
        bencana.tampilkan_keterangan()

    # gempa_di_dunia = GempaTerkini('https://bmkg.go.id')
    # print('Deskripsi class GempaTerkini', gempa_di_dunia.description)
    # gempa_di_dunia.run()
    # gempa_di_indonesia.ekstraksi_data()
    # gempa_di_indonesia.tampilkan_data()