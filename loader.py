import requests
import zipfile
from io import BytesIO
import csv
from adapter import KenAllAdapter, JigyosyoAdapter
from repository import ZipCodeRepository
from files import FILES

def load_zip_csv(url: str, encoding: str = "utf-8"):
    response = requests.get(url)
    response.raise_for_status()
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        for file_name in z.namelist():
            with z.open(file_name) as f:
                text = f.read().decode(encoding)
                reader = csv.reader(text.splitlines())
                for row in reader:
                    yield row

def load_all_zipcode_data():
    repo = ZipCodeRepository()

    # ken all
    ken_all_file = FILES['ken_all']
    ken_adapter = KenAllAdapter()
    for row in load_zip_csv(ken_all_file['url'], encoding=ken_all_file.get('encoding', 'utf-8')):
        record = ken_adapter.adapt(row)
        repo.add(record)

    # JIGYOSYO
    jigyosyo_file = FILES['jigyosyo']
    jigyosyo_adapter = JigyosyoAdapter()
    for row in load_zip_csv(jigyosyo_file['url'], encoding=jigyosyo_file.get('encoding', 'utf-8')):
        record = jigyosyo_adapter.adapt(row)
        repo.add(record)

    return repo
