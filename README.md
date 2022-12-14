# Praktikum 1 Komputasi Numerik D Kelompok 14
## Anggota
* Muhamad Faiz Fernanda - 5025211186
* Farhan Dwi Putra - 5025211093
* Thoriq Afif Habibi - 5025211154
## Penjelasan hasil praktikum
Pertama, saya membuat fungsi bolzano yang akan menerapkan metode bolzano untuk mencari akar persamaan. Fungsi ini memiliki 3 parameter, yaitu a sebagai xn, b sebagai xn+1, dan n sebagai banyak iterasi yang ingin dilakukan. Saya membuat variabel xn dan xn+1 yang diisi nilai a dan b. Pada fungsi ini, diasumsikan terjadi perubahan tanda pada interval xn hingga xn+1. Saya kemudian menggunakan perulangan hingga n dan menghitung xt yang bernilai (xn+x(n+1))/2, f(xn), f(xn+1), serta f(xt). Penentuan apakah xt menggantikan xn atau xn+1 ditentukan dengan conditional statement yang dapat dilihat pada code di bawah:<br/>
![Fungsi Metode Bolzano](Screenshot_20221030_084113.png)

<br/>Pada solusi yang kami buat, fungsi, xn, xn+1, dan jumlah iterasi diletakkan pada source code dan tidak pada input user. Oleh karena itu, kami mendefinisikan mereka pada source code sebagi berikut:<br/>
![[fungsi](fungsi (1).png)](https://github.com/Thoriqaafif/P1_Komnum_D14/blob/main/fungsi%20(1).png) <br/>
![[variabel](fungsi (2).png)](https://github.com/Thoriqaafif/P1_Komnum_D14/blob/main/fungsi%20(2).png)

<br/>Untuk membuat kurva dan grafik, kami menggunakan bantuan library matplotlib dan numpy. Fungsi-fungsi pada library tersebut berguna untuk membuat grafis grafik, memplot nilai-nilai x dan y, serta menganimasikan penyempitan interval yang terjadi ketika melakukan setiap iterasi pada metode bolzano. Potongan code yang digunakan untuk melakukan beberapa hal tersebut sebagai berikut:<br/>
![code buat grafik.png](https://github.com/Thoriqaafif/P1_Komnum_D14/blob/main/code%20buat%20grafik.png)

<br/>Dengan menggunakan fungsi f(x) = x^3-3x+1, xn=1, xn+1=2, dan jumlah iterasi sebbanyak 10, program kami akan memberi output animasi grafik dan nilai x sebagai berikut:<br/>
![grafik](https://github.com/Thoriqaafif/P1_Komnum_D14/blob/main/Screenshot_20221030_084139.png)<br/>
![output](https://github.com/Thoriqaafif/P1_Komnum_D14/blob/main/Screenshot_20221030_084154.png)
