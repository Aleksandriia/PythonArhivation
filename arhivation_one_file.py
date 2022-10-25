#Сжфтие одного файла
import zipfile

jungle_zip = zipfile.ZipFile('C:\\Users\\1\\Desktop\\Веб-дизайн.zip', 'w')
jungle_zip.write('C:\\Users\\1\\Desktop\\Веб-дизайн', compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()