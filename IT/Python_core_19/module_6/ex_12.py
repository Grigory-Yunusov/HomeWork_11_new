"""
Робота з архівами
"""

import shutil
print(shutil.get_archive_formats())
archive = shutil.make_archive('archive_file_name', 'zip', 'Hello')
print(archive)  # /Users/vova/PycharmProjects/GoIT19/lesson_6/archive_file_name.zip


shutil.unpack_archive(archive, 'Archive/Test/In')