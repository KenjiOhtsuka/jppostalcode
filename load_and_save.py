import requests
import zipfile
from io import BytesIO
import os
from files import FILES

os.makedirs('data', exist_ok=True)

for file_key, file_info in FILES.items():
    response = requests.get(file_info['url'])
    response.raise_for_status()

    with zipfile.ZipFile(BytesIO(response.content)) as z:
        for file_name in z.namelist():
            encoding = file_info.get('encoding', 'utf-8')

            with z.open(file_name) as f:
                raw = f.read()

            text = raw.decode(encoding)

            output_file = os.path.join('data', file_name)
            with open(output_file, 'w', encoding='utf-8') as out_f:
                out_f.write(text)
