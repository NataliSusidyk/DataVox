from xlrd import open_workbook
from fuzzywuzzy import fuzz

def read_file(sstr, n):
	d_list = []
	book = open_workbook(sstr)
	sheet = book.sheet_by_index(n)
	keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]

	for row_index in range(1, sheet.nrows):
		d = {keys[col_index]: sheet.cell(row_index, col_index).value
		for col_index in range(sheet.ncols)}
		d_list.append(d)
	return d_list
	
def search_name(dict_l, x, mass):
	tmp = ""
	k = 0

	for item in mass:
		for line in dict_l:
			tmp+= line[item] + " "
		tmp = tmp.split()

		for i in tmp:
			prblt = fuzz.token_set_ratio(x, i)
			if prblt>80:
				k+=1
		print_data(item, k, tmp)
		k = 0
		tmp = ""

def print_data(itm, n, tmps):
	chst = round((n / len(tmps))*100,2)
	print("In coloumn '" + str(itm) + "': " + str(n) + " times mentioned person. Frequency relative to text: " + 
		str(chst) + ". Lenght of text in coloumn: " + str(len(tmps)) + " words.")


def main():
	dict_list = read_file('mentions.xlsx', 0)
	name_pltc = str(input("Enter name : "))
	name_coloumns = ['Заголовок', 'Аннотация', 'Полнотекст']
	search_name(dict_list, name_pltc, name_coloumns)
	
if __name__ == '__main__':
    main()