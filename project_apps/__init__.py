
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/files/')

class CSVFiles:
    def __init__(self, request) -> None:
        self.request = request
        pass

    def store_csv_file(self):
        file = self.request.FILES.get('file').read()
        content = ContentFile(file)
        temp_file = fs.save(name='data.csv', content=content) 
        return temp_file

    def get_csv_file(self):
        file = fs.path(self.store_csv_file())
        return file