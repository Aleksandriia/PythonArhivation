#Сжатие одного файла
import zipfile

adres_file = str(input("Укажите путь файла: "))
adres_file_replace = adres_file.replace("\\", "\\\\")
print("Путь после преобразований: ", adres_file_replace)

jungle_zip = zipfile.ZipFile(adres_file_replace + '.zip', 'w')
jungle_zip.write(adres_file_replace, compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()

#C:\Users\1\Desktop\Сессия2.pdf