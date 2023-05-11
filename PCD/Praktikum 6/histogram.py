import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

# Membaca Gambar
img = imageio.imread("D:\Kuliah\Semester 6\Pengolah Citra Digital\Praktikum\Pertemuan 3 dan 4\image\citra.jpg")

# Membuat variabel y x dan channel
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

# Merubah gambar menjadi Grayscale

# Memubat variabel dengan array bernilai kosong
img_grayscale = np.zeros(img.shape, dtype=np.uint8)

for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        # Nilai intensitas RGB dijumlahkan lalu dibagi 3(karena terdapat 3 warna) untuk mendapat nilai rata2 yang akan dipakai untuk nilai grayscale
        gray = (int(red) + int(green) + int(blue)) / 3
        img_grayscale[y][x] = (gray, gray, gray)
        
plt.imshow(img_grayscale)
plt.title("Grayscale")
plt.show()

# Menampilkan Histogram Gambar Grayscale
# Membuat variabel untuk menyimpan data gambar

hg = np.zeros((256))

# Mengisi setiap nilai dalam array hg dengan 0

for x in range(0, 256):
    hg[x] = 0

# Menghitung nilai dari gambar

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hg[gray] += 1

# Menampilkan Histogram

plt.figure(figsize=(20, 6))
plt.plot(hg, color="black", linewidth=2.0)
plt.show()

bins = np.linspace(0, 256, 100)
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")
plt.show()

# Menampilkan Histogram Gambar RGB
# Membuat variabel untuk menyimpan data gambar
# Membuat ukuran 256 (Nilai intensitas pixel 0 - 255)
# perwarna 256
hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))

# Membuat ukuran 768 (nilai intensitas pixel 0-767) untuk kombinasi RGB
hgrgb = np.zeros((768))

# Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

# Menghitung nilai dari gambar
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

th = int(256/64)
temp = [0]
for y in range(0, img.shape[0]):
    for x in range(0, img.shape[1]):
        red = int(img[y][x][0])
        green = int(img[y][x][1])
        blue = int(img[y][x][2])
        green = green + 256
        blue = blue + 512
        temp.append(green)
        hgrgb[red] += 1
        hgrgb[green] += 1
        hgrgb[blue] += 1

binsrgb = np.linspace(0, 768, 100)
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5) # Mencetak histogram
plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")
plt.show()

# Menampilkan Histogram
for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

# Membuat range atau interval nilai pada histogram hingga 100 dengan intensitas nilai 0 - 256
bins = np.linspace(0, 256, 100)
plt.hist(hgr, bins, color="red", alpha=0.5)
plt.title("Histogram Red")
plt.show()

plt.hist(hgg, bins, color="green", alpha=0.5)
plt.title("Histogram Green")
plt.show()

plt.hist(hgb, bins, color="blue", alpha=0.5)
plt.title("Histogram Blue")
plt.show()

# Menampilkan Histogram Kumulatif

# Menghitung histogram untuk grayscale image
hgk = np.zeros((256))
c = np.zeros((256))

# Menginisialisasi nilai array hgk dan c dengan 0
for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0

# Looping untuk menghitung nilai histogram untuk setiap nilai intensitas gray pada citra grayscale
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgk[gray] += 1

# Looping untuk menghitung nilai kumulatif histogram
c[0] = hgk[0]
for x in range(1, 256):
    c[x] = c[x-1] + hgk[x]

hmaxk = c[255]
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk


plt.hist(c, bins, color="black", alpha=0.5) # Mencetak histogram
plt.title("Histogram Grayscale Kumulatif")
plt.show()

# Menampilkan Histogram Hequalisasi

# Inisialisasi array untuk histogram grayscale, distribusi kumulatif, dan hequalisasi
hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

# Set semua elemen array ke 0
for x in range(0, 256):
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

# Hitung histogram grayscale
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1
                
# Hitung distribusi kumulatif dan normalisasi
h[0] = hgh[0]
for x in range(1, 256):
     h[x] = h[x-1] + hgh[x]

for x in range(0, 256):
     h[x] = h[x] / img_height / img_width

# Buat citra baru dengan equalisasi histogram
for x in range(0, 256):
    hgh[x] = 0
    
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

# Hitung distribusi kumulatif dan normalisasi lagi
c[0] = hgh[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgh[x]

hmaxk = c[255]

# Skala hasil equalisasi ke 0-190
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk


plt.hist(c, bins, color="black", alpha=0.5) # Mencetak histogram
plt.title("Histogram Grayscale Hequalisasi")
plt.show()