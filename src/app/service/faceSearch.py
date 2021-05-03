import numpy as np 
import faiss
from tabulate import tabulate
from app.utils.message import message
from datetime import datetime


class FaceSearch:

    def __init__(self, dimension):

        self.dimension = dimension
        

        self.index = faiss.IndexFlatL2(self.dimension)

        
        print(f"\nInitialize FaceSearch ...\n") 
        
        table = [
                 [f"n_Dimension: {self.dimension}"]]
        print(tabulate(table))

      

    def train(self, data, database_path=None):
  
        start = datetime.now()
        message.HilightPrint("Start Trainig Face")
        self.index.train(data)
        assert self.index.is_trained
        self.index.add(data) 
        message.SuccessPrint(f"Done: {self.index.ntotal}")
        message.WarnPrint(f"Use: {datetime.now()-start} sec")
      
        if not database_path == None:
            message.WarnPrint(f"Wrote database index to {database_path} ")
            faiss.write_index(self.index, database_path)


    def search(self, query_vector, k=4):
        Distance, Index = self.index.search(query_vector, k) 
        return Distance, Index
