import os
import shutil
import stat
import zipfile
from http import HTTPStatus

import requests

URL = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json'
LOCAL_ZIP_FILE = os.path.join(os.path.dirname(__file__), 'chromedriver.zip')
EXTRACT_TO = os.path.join(os.path.dirname(__file__), 'temp_extract')
BIN_DIR = os.path.join(os.path.dirname(__file__), '..', 'bin')

response = requests.get(URL)

if response.status_code == HTTPStatus.OK:
    data = response.json()
    url_download = data['channels']['Stable']['downloads']['chromedriver'][0][
        'url'
    ]

    with requests.get(url_download, stream=True) as response:
        response.raise_for_status()
        with open(LOCAL_ZIP_FILE, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    if not os.path.exists(EXTRACT_TO):
        os.makedirs(EXTRACT_TO, exist_ok=True)

    with zipfile.ZipFile(LOCAL_ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_TO)

    for root, dirs, files in os.walk(EXTRACT_TO):
        for file in files:
            extracted_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(BIN_DIR, file)

            shutil.move(extracted_file_path, destination_file_path)
            os.chmod(
                destination_file_path,
                os.stat(destination_file_path).st_mode | stat.S_IEXEC,
            )

    os.remove(LOCAL_ZIP_FILE)
    os.remove(os.path.join(BIN_DIR, 'LICENSE.chromedriver'))
    shutil.rmtree(EXTRACT_TO)
    print('Chromedriver atualizado!')
else:
    print('Falha no GET para a API.')
