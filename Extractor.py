class Extractor:
    def extract_info(self, soup):
        info_list = []
        for item in soup.select('[data-lid]'):
            title = item.select_one('h3').get_text()
            link = item.select('a')[0]['href']
            abstract = item.select_one('.gs_rs').get_text().strip() if item.select_one('.gs_rs') else "No hay resumen disponible"
            authors = [author.get_text() for author in item.select('.gs_a a')]
            pub = item.select_one('.gs_a').get_text().split('-')[-1].strip()
            citations = item.select_one('.gs_fl a[href*=cites]').get_text().split()[-1] if item.select_one('.gs_fl a[href*=cites]') else "No disponible"
            doc_type = item.select_one('.gs_ctg2').get_text() if item.select_one('.gs_ctg2') else "No disponible"
            
            info_list.append({
                "title": title,
                "authors": authors,
                "pub": pub,
                "link": link,
                "abstract": abstract,
                "citations": citations,
                "doc_type": doc_type
            })
        return info_list