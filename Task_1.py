import urllib.request
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.cvk.gov.ua/pls/vnd2019/wp401pt001f01=919lit=192current_row=1.html"
frst_url = "https://www.cvk.gov.ua/pls/vnd2019/wp401pt001f01=919lit="
mdl_url = "current_row="
lst_url = ".html"
candidates = []

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_ = 'pure-table pure-table-bordered w100')
    
    for row in table.find_all('tr')[1:]:
    	cols = row.find_all('td')

    	candidates.append({
    		'LastName': cols[0].a.text.split()[0],
    		'FirstName': cols[0].a.text.split()[1],
    		'FatherName': cols[0].a.text.split()[2],
    		'political party': cols[1].b.text.split(',')[0],
    		'number': cols[1].b.text.split()[-1]
    		})  

def csv_writer(data, path):
	with open(path, "w", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=';')
		for line in data:
			writer.writerow(line.values())

def prewriter():
	k = 1
	for i in range(32):
		while True:
			try:
				sub = frst_url + str(192+i) + mdl_url + str(k) +lst_url
				parse(get_html(sub))
				k +=30
			except:
				break
		k = 1

def main():
	prewriter()
	path = "output.csv"
	csv_writer(candidates, path)
    
if __name__ == '__main__':
    main()