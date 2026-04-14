#!/bin/python3 

from sys import argv
from requests import Session
from time import sleep
from pandas import read_html
from numpy import full

class Decode:
    def __init__(self, URL: str):
         self.file = "temp_file.txt"
         self.URL = URL
         self.CHUNK_SIZE = 32768

    def download(self):
        session = Session()
        response = session.get(self.URL, params={"id": self.URL}, stream=True)

        #print(f"Downloading: {URL}")
        with open(self.file, "wb") as f:
            for chunk in response.iter_content(self.CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def read_doc(self):
        tables = read_html(self.file, encoding='utf-8')
        for table in tables:
            #print(table)
            self.make_grid(table)

        #print(tables)

    def make_grid(self, table: str):
        #print(table[0])
        cols = self.get_max(table[0])
        rows = self.get_max(table[2])
        #print(f"X={rows} Y={cols}")
   
        # Adding one becase we start counting at 0
        matrix = full((rows + 1, cols + 1), ' ')

        #print(matrix)

        # Subtracting 1 to remove the headers
        for row in range(len(table[0]) -1):
            # Adding one to skip the headers
            y = int(table[0][row + 1])
            char = table[1][row + 1]
            x = int(table[2][row + 1])
            #print(f'{x} {char} {y}')

            # Subtracting x from rows to rotate the matrix
            matrix[rows - x][y] = char

#        print(matrix)
        for row in matrix:
            print()
            for element in row:
                print(element, end="")
        print()


    def get_max(self, collumn):
        max = 0
        #print(f'Length: {len(collumn)}')
        for i in range(len(collumn) - 1):
            try:
                temp = int(collumn[i + 1])
                #print(temp)
                if temp > max:
                    max = temp
            except error as e:
                print('error: {e}')
            #print(f'max: {max}')
        return max

    def main(self):
        self.download()
        sleep(1)
        self.read_doc()

if __name__ == "__main__":
    if len(argv) >= 2:
        URL = argv[1]
        decode = Decode(URL)
        decode.main()
    else:
        print("Error please include a URL")
