class Printer:
    def print_info(self, info_list):
        for info in info_list:
            print("Título:", info["title"])
            print("Autores:", ", ".join(info["authors"]))
            print("Publicado en:", info["pub"])
            print("Enlace:", info["link"])
            print("Resumen:", info["abstract"])
            print("Número de Citas:", info["citations"])
            print("Tipo de Documento:", info["doc_type"])
            print("----------------------")