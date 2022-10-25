#Извлечение файлов из архива

import zipfile

adres_file = str(input("Укажите путь файла: "))
adres_file_replace = adres_file.replace("\\", "\\\\")
print("Путь после преобразований: ", adres_file_replace)
new_file_name = str(input("Введите имя новой папки: "))

fantasi_zip = zipfile.ZipFile(adres_file_replace)
fantasi_zip.extractall('C:\\Users\\1\\Desktop\\' + new_file_name)

fantasi_zip.close()
