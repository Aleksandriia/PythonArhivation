# Сжатие одного файла
# Редактирование в коде

import zipfile

jungle_zip = zipfile.ZipFile('C:\\...\\Desktop\\file.zip', 'w')
jungle_zip.write('C:\\...\\Desktop\\file', compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()
