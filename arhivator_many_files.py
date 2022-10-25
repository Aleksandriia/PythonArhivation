# Сжатие нескольких файлов / папки
# Путь файла вносится через код

import os
import zipfile

fantasi_zip = zipfile.ZipFile('C:\\...\\Desktop\\file.zip', 'w')

for folder, subfolders, files in os.walk('C:\\...\\Desktop\\file'):
	for file in files:
		fantasi_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), 'C:\\...\\Desktop\\file'), compress_type = zipfile.ZIP_DEFLATED)

fantasi_zip.close()
