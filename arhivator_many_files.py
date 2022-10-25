#Сжатие нескольких файлов / папки
import os
import zipfile

fantasi_zip = zipfile.ZipFile('C:\\Users\\1\\Desktop\\Веб-дизайн.zip', 'w')

for folder, subfolders, files in os.walk('C:\\Users\\1\\Desktop\\Веб-дизайн'):
	for file in files:
		fantasi_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), 'C:\\Users\\1\\Desktop\\Веб-дизайн'), compress_type = zipfile.ZIP_DEFLATED)

fantasi_zip.close()