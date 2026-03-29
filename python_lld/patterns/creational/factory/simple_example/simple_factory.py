from enum import Enum
from abc import ABC, abstractmethod
class ExporterType(Enum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"

class Exporter(ABC):

    @abstractmethod
    def export(self, data: list[dict]) -> str:
        pass

class CSVExporter(Exporter):

    def export(self, data: list[dict]) -> str:
        return f"data exported from CSV : {data}"
    
class JSONExporter(Exporter):

    def export(self, data: list[dict]) -> str:
        return f"data exported from JSON : {data}"
    
class ParquetExporter(Exporter):

    def export(self, data: list[dict]) -> str:
        return f"data exported from parquet : {data}"
    
class ExporterFactory:
    @staticmethod
    def create(exporter_type: ExporterType) -> Exporter:
        
        if exporter_type == ExporterType.CSV:
            return CSVExporter()
        elif exporter_type == ExporterType.JSON:
            return JSONExporter()
        elif exporter_type == ExporterType.PARQUET:
            return ParquetExporter()
        else:
            raise ValueError(f"Unsupported exporter type: {exporter_type}")


csv_exporter = ExporterFactory.create(ExporterType.CSV)

print(csv_exporter.export([{1: "one"}, {2: "two"}]))