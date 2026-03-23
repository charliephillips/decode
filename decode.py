#!/bin/python3 

import sys
from requests import Session
from time import sleep
import pandas as pd
import numpy as np

class Decode:
    def __init__(self, URL: str):
         self.file = "temp_file.txt"
         self.URL = URL
         self.CHUNK_SIZE = 32768

    def download(self):
        session = Session()
        response = session.get(self.URL, params={"id": self.URL}, stream=True)

        print(f"Downloading: {URL}")
        with open(self.file, "wb") as f:
            for chunk in response.iter_content(self.CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def read_doc(self):
        tables = pd.read_html(self.file, encoding='utf-8')
        for table in tables:
            #print(table)
            self.make_grid(table)

        #tables = pd.read_table(self.file, encoding='utf-8')
        #print(tables)

    def make_grid(self, table: str):
        #print(table[0])
        cols = self.get_max(table[0])
        rows = self.get_max(table[2])
        #print(f"X={rows} Y={cols}")
   
        matrix = np.full((rows + 1, cols + 1), ' ')

        #print(matrix)

        for row in range(len(table[0]) -1):
            y = int(table[0][row + 1])
            char = table[1][row + 1]
            x = int(table[2][row + 1])
            #print(f'{x} {char} {y}')

            matrix[rows - x][y] = char
        #self.add_char(matrix, row)

        print(matrix)


    def get_max(self, collumn):
        max = 0
        #print(f'Length: {len(collumn)}')
        for i in range(len(collumn) - 1):
            try:
                #print(int(collumn[i + 1]))
                if int(collumn[i + 1]) > max:
                    max = int(collumn[i + 1])
            except error as e:
                print('error: {e}')
            #print(f'max: {max}')
        return max

    def main(self):
        #self.download()
        #sleep(5)
        self.read_doc()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        URL = sys.argv[1]
        decode = Decode(URL)
        decode.main()
    else:
        print("Error please include a URL")