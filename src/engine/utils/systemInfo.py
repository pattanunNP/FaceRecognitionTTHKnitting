import psutil
from tabulate import tabulate



class  SystemInfo:

        @staticmethod
        def getSystemInfo():
                print(f"\nChecking your CPU ...\n")
        
        
                table = [[f"CPU: {psutil.cpu_count(logical=False)} Cores"],
                        [f"LogicCore: {psutil.cpu_count()} Cores"]]
                print(tabulate(table))

                return psutil.cpu_count(logical=False),psutil.cpu_count()