# [PyHund::Reporter ~]

class PyHundReporter:
    
    def build_report(self, raw_scan:dict, output_format:str = 'txt'):
        match output_format:
            case 'txt':
                pass

            case 'csv':
                pass

            case 'json':
                pass

            case 'yaml':
                pass

            case _:
                print(raw_scan)
