#Извлечение единичных файлов
import zipfile

fantasi_zip = zipfile.ZipFile('C:\\Users\\1\\Desktop\\Веб-дизайн.zip')
fantasi_zip.extract('Веб-дизайн Screenshot_6.png', 'C:\\Users\\1\\Desktop\\Веб-дизайн')

fantasi_zip.close()