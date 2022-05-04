import urllib.request
import os

visited = set()                                     # stores downloaded url, prevents duplicates
links = []


def populate_array(csv_file):                       # input: csv file name
    f = open(csv_file, "r")                         # populates list "links" with unique urls
    while True:
        line = f.readline()
        if not line:
            break
        url = line.split(",")[1]
        if url not in visited:
            links.append(url)
            visited.add(url)
    links.pop(0)

def download_file(download_url, filename):          # input : url, what name to save it as
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()


def change_directory():
    print("creating dir...")
    os.mkdir("pdf_files")

    print("going into pdf_files...")
    os.chdir("pdf_files")


populate_array("Sample Receipt - Sheet1.csv")
change_directory()

for i in range(len(links)):
    download_file(links[i], str(i+1))
    print(f"{i+1}.pdf added.")