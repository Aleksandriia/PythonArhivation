# Извлечение единичных файлов

import zipfile

fantasi_zip = zipfile.ZipFile('C:\\...\\Desktop\\file.zip')
fantasi_zip.extract('file Screenshot.png', 'C:\\...\\Desktop\\file')

fantasi_zip.close()
