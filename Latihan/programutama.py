# import geometri as geo
from geometri import LuasLingkaran, VolumeTabung

jarijari = float(input("Masukkan jari-jari lingkaran: "))
tinggi = float(input("Masukkan tinggi tabung: "))
# Volume = geo.VolumeTabung(geo.LuasLingkaran(jari-jari), tinggi)
Volume = VolumeTabung(LuasLingkaran(jari-jari), tinggi)
print("Volume tabung dengan jari-jari", jari-jari, "dan tinggi", tinggi, "adalah", Volume)