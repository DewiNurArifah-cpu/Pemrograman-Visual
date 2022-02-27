#PRAKTIKUM 1

print("Develop by : Dewi Nur Arifah/MI-2020A/20051397079")
print("             ~~ ENKRIPSI DATA ~~")

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

kata = input('Masukkan kata sebelum di enkripsi :  ')
kunci = int(input('Masukkan kode kunci (misal 3) :  '))

def encode(kata, chiper):
    kata = kata.lower()
    hasil_enkripsi = ''
    for karakter in kata:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama + chiper) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_enkripsi = hasil_enkripsi + abjad_baru
        else:
            hasil_enkripsi = hasil_enkripsi + ' '
    return hasil_enkripsi

#ENKRIPSI
kalimat_hasil = encode(kata, kunci)

print('Kata setelah di enkripsi :  ' , kalimat_hasil)
