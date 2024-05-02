class ExcelPrinter:
    def __init__(self, filename,worbook):
        self.filename = filename
        self.workbook = worbook
        self.sheet = self.workbook.active
        self.sheet.append(["Título", "Autores", "Publicado en", "Enlace", "Resumen", "Número de Citas", "Tipo de Documento"])

    def add_record(self, info_list):
        for info in info_list:
            self.sheet.append([info["title"],
                               ", ".join(info["authors"]),
                               info["pub"],
                               info["link"],
                               info["abstract"],
                               info["citations"],
                               info["doc_type"]])

    def save(self):
        self.workbook.save(filename=self.filename)