#!/bin/python3 

import sys
import requests

class Decode:
    def __init__(self, URL: str):
         self.file = "temp_file.txt"
         self.URL = URL

    def download(self):

        session = requests.Session()

        response = session.get(self.URL, params={"id": self.URL}, stream=True)
        token = self.get_token(response)

        if token:
            params = {"id": self.URL, "confirm": token}
            response = session.get(URL, params=params, stream=True)
#        else:
#            params = {"id": self.URL}
#            response = session.get(URL, params=params, stream=True)

        self.save_content(response)

    def get_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value

    def save_content(self, response):
        CHUNK_SIZE = 32768

        with open(self.file, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def read_doc(self):
        with open(self.file, 'r') as f:
            contents = f.read()
            print(contents)
 

    def main(self):
        self.download()
#        self.read_doc()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        URL = sys.argv[1]
        print(f"dowload {URL}")
        decode = Decode(URL)
        decode.main()
    else:
        print("Error please include a URL")