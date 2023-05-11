import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

# Membaca citra dengan library imageio
img = imageio.imread("D:\Kuliah\Semester 6\Pengolah Citra Digital\Praktikum\Pertemuan 3 dan 4\image\citra.jpg")

# Membuat variabel
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

# Memubat variabel dengan array bernilai kosong
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)

# Membalik gambar secara horizontal

# memberi nilai pada y mulai dari 0 karena akan diisi pada array kosong sampai ukuran tinggi citra yang dipakai
for y in range(0, img_height):
# memberi nilai pada x mulai dari 0 karena akan diisi pada array kosong sampai ukuran lebar citra yang dipakai
    for x in range(0, img_width):
        for c in range(0, img_channel):
            # Varibel img flip ini mengisi nilai pixel baru y dan c tetap sesuai citra asli
            # [img_width-1-x] ini yang membuat gambar membalik secara horizontal
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]

# Membalik gambar secara vertical

# memberi nilai pada y mulai dari 0 karena akan diisi pada array kosong sampai ukuran tinggi citra yang dipakai
for y in range(0, img_height):
    # memberi nilai pada x mulai dari 0 karena akan diisi pada array kosong sampai ukuran lebar citra yang dipakai
    for x in range(0, img_width):
        for c in range(0, img_channel):
            # Varibel img flip ini mengisi nilai pixel baru x dan c tetap sesuai citra asli
            # [img_height-1-y] ini yang membuat gambar membalik secara vertikal
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]

# Menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal) # Menampilkan citra
plt.title("Flip Horizontal") # judul
plt.show()
plt.imshow(img_flip_vertical) # Menampilkan citra
plt.title("Flip Vertical") # judul
plt.show()