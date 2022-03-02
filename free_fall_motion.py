"""

Algoritma gerak jatuh bebas dengan metode penyelesaian numerik
dibuat oleh Ubaidillah pada 02/03/2022

"""

#########################################################
## 			       Inisiasi Variabel				   ##
#########################################################

vt = 0 # kecepatan pada saat t, untuk kecepatan awal adalah 0 m/s
a = -9.8 # percepatan gravitasi (konstanta 9.8 m/s^2), negatif karena 
         # arah menuju ke bawah
xt = 10 # posisi objek pada saat t, ganti nilai variabel sesuai posisi 
		 # benda kalian
deltaT = 0.0001 # delta t adalah t1 - t0 atau selisih waktu per iterasi
				 # semakin kecil maka semakin akurat
t = 0 # waktu yang dibutuhkan objek untuk jatuh ke tanah, waktu awal
	  # adalah 0s

#########################################################
## 			     Nilai Awal Variabel Acuan		       ##
#########################################################	

print('\n-----------------=Nilai Awal=--------------------\n')
print(f'Posisi awal adalah {xt}m')
print(f'Delta t nya adalah {deltaT}s')
print(f'Percepatannya adalah {a}m/s^2')
print(f'Kecepatan awalnya adalah {vt}m/s\n')

print('#'*150)
print('#'*150+'\n')

#########################################################
## 			    Iterasi Gerak Jatuh Bebas		       ##
#########################################################

print('----------=Iterasi Gerak Jatuh Bebas=---------\n')
while xt >= 0: 
    # iterasi berhenti jika jarak objek ke tanah bernilai negatif
    print(f'Posisi benda sekarang adalah {xt}m ',end='') 
    print(f'dengan kecepatan {vt}m/s pada waktu {t}s')
    vt += (a*deltaT) # vt = v0 + (a*deltaT), v0 = kecepatan sebelumnya
    xt += (vt*deltaT) # xt = x0 + (vt*deltaT), x0 = jarak sebelumnya
    t += deltaT # t = t + deltaT, waktu bertambah tiap iterasi

#########################################################
## 			       Hasil akhir				           ##
#########################################################

print('\n'+'#'*150)
print('#'*150+'\n')

print('-----------------=Hasil Akhir=-----------------\n')
print(f'Waktu benda jatuh ke tanah {t} detik')
print(f'Waktu benda jatuh ke tanah {t/60} menit') # konversi ke menit
print(f'Waktu benda jatuh ke tanah {t/3600} jam') # konversi ke jam