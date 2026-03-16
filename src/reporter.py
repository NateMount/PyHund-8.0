# [PyHund::Reporter ~]

# === Imports

from json import dump

# === PyHund Reporter Class

class PyHundReporter:
    
    def build_report(self, raw_scan:dict, output_format:str = 'txt', output_file:str = 'ScanResults'):
        match output_format:
            case 'txt'  :  self.to_text(raw_scan, output_file)
            case 'csv'  :  self.to_csv(raw_scan, output_file)
            case 'json' :  self.to_json(raw_scan, output_file)
            case 'yaml' :  self.to_yaml(raw_scan, output_file)
            case _      :  print(raw_scan)

    @staticmethod
    def to_txt(raw_scan:dict, output_file:str) -> None:
        
        with open(output_file, 'w') as f:
            pass

    @staticmethod
    def to_csv(raw_scan:dict, output_file:str) -> None:
        
        with open(output_file, 'w') as f:
            pass

    @staticmethod
    def to_json(raw_scan:dict, output_file:str) -> None:
        dump(raw_scan, output_file)

    @staticmethod
    def to_yaml(raw_scan:dict, output_file:str) -> None:
        pass
