from utils.export import export_csv, export_excel


class ExportService:
    def to_csv(self, df, path):
        export_csv(df, path)

    def to_excel(self, df, path):
        export_excel(df, path)
