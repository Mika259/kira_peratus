#setelah sekian sekejap je buat :)
#DanielHakim : saya dah susun code² ini supaya kelihatan kemas :]

banner = """
_  ___           _  ____  __            _
| |/ (_)_ __ __ _(_)/ /  \/  | __ _ _ __| | __
| ' /| | '__/ _` | / /| |\/| |/ _` | '__| |/ /
| . \| | | | (_| |/ /_| |  | | (_| | |  |   <
|_|\_\_|_|  \__,_/_/(_)_|  |_|\__,_|_|  |_|\_]
Author :Mika259
Github :https://github.com/Mika259

"""
print("Kira Peratus Markah anda !")
import time
time.sleep(1)

print("Tulis 0 pada markah soalan yang tidak dijawab atau tidak perlu dijawab (maximum soalan 8 sahaja tersedia disini)")

s1 = int(input("Soalan 1 berapa : "))
s2 = int(input("Soalan 2 berapa : "))
s3 = int(input("Soalan 3 berapa : "))
s4 = int(input("Soalan 4 berapa : "))
s5 = int(input("Soalan 5 berapa : "))
s6 = int(input("Soalan 6 berapa : "))
s7 = int(input("Soalan 7 berapa : "))
s8 = int(input("Soalan 8 berapa : "))

mr = (s1+s2+s3+s4+s5+s6+s7+s8)

print("Tunggu sebentar..")
time.sleep(2)

print("Hasil Tambah Kesemua Soalan :")
print(mr)
time.sleep(0.5)

per = int(input("per berapa markah kesemuanya : "))
print("Ok")
time.sleep(0.3)

print("Tunggu Proses..")
time.sleep(2)

jw = mr/per
pr = jw*100

print("Markah Peratus :",str(round(pr))+"%")
time.sleep(0.3)
print("Terima Kasih menggunakan tool saya :)")
