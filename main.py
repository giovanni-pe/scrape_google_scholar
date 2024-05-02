from bs4 import BeautifulSoup
import requests
from Extractor import Extractor
from Scraper import Scraper
from Printer import Printer
from ExcelPrinter import ExcelPrinter
from openpyxl import Workbook
def scrape_google_scholar(author_names, num_pages=1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    }
    scraper = Scraper(headers,requests, BeautifulSoup)
    extractor = Extractor()
    printer = Printer()
    excel_printer=ExcelPrinter('reporte.xlsx',Workbook())

    for page in range(num_pages):
        start = page * 10
        author_query = build_query(author_names)
        url = f"https://scholar.google.com/scholar?start={start}&q={author_query}&hl=es&as_sdt=0,5"
        soup = scraper.scrape(url)
        print(f"Resultados de la página {page + 1} para el autor {' '.join(author_names)}:")
        info_list = extractor.extract_info(soup)
        printer.print_info(info_list)
        excel_printer.add_record(info_list)
    excel_printer.save()

def build_query(author_names_string):
    author_names = [name.strip() for name in author_names_string.split(" ")]
    return " ".join(f"author:{name}" for name in author_names)

author_names_input = input("Ingrese los nombres y apellidos del autor: ")
num_pages = int(input("Ingrese el número de páginas a buscar: "))

scrape_google_scholar(author_names_input, num_pages)
