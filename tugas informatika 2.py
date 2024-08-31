nama_lengkap = input("Masukkan nama lengkap Anda: ")
usia_tahun = int(input("Masukkan usia Anda dalam tahun: "))
tinggi_cm = float(input("Masukkan tinggi badan Anda dalam sentimeter: "))
status_menikah = input("Apakah Anda sudah menikah? (y/n): ").lower() == 'y'

usia_bulan = usia_tahun * 12
tinggi_meter = tinggi_cm / 100

print("\n--- Ringkasan Informasi ---")
print(f"Nama lengkap: {nama_lengkap}")
print(f"Usia: {usia_tahun} tahun atau {usia_bulan} bulan")
print(f"Tinggi badan: {tinggi_cm} cm atau {tinggi_meter:.2f} m")
print(f"Status pernikahan: {'Sudah menikah' if status_menikah else 'Belum menikah'}")