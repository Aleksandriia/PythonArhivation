# Сжатие нескольких файлов / папки
# Пользователь вводит путь в терминале

import os
import zipfile

adres_file = str(input("Укажите путь файла: "))
adres_file_replace = adres_file.replace("\\", "\\\\")
print("Путь после преобразований: ", adres_file_replace)

fantasi_zip = zipfile.ZipFile(adres_file_replace + '.zip', 'w')

for folder, subfolders, files in os.walk(adres_file_replace):
	for file in files:
		fantasi_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), adres_file_replace), compress_type = zipfile.ZIP_DEFLATED)

fantasi_zip.close()
