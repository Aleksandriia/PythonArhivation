# Сжатие одного файла
# Редактирование в коде

import zipfile

jungle_zip = zipfile.ZipFile('C:\\Users\\1\\Desktop\\file.zip', 'w')
jungle_zip.write('C:\\Users\\1\\Desktop\\file', compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()
