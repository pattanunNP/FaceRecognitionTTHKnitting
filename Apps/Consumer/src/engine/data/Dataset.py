
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from app.utils.file_preprocess import file_preprocess
import numpy as np
from facenet_pytorch import  training
import natsort
import os
import pendulum
import time
import re
import json
import uuid
import hashlib
from tqdm.auto import tqdm

block_size = 1024
hash = hashlib.md5()
img_re = re.compile(r'.+\.(jpg|png|jpeg|tif|tiff)$', re.IGNORECASE)
datapack = {}
datapack['runners'] = []

class Dataset:

    @staticmethod
    def create_json(root, size=160, TZ="Asia/Bangkok"):
           
        runners_data = {}
         
        for i, runner in enumerate(os.listdir(root),1):
         
            verify_path = []
            verify_hash = []
            content_counter = 0
            dirpath = os.path.join(root,runner)

            runners_data["image_path"] = []
            runners_data["image_counts"] = 0
      
            runners_data ={
                "id":runner.split('_')[0],
                "name":runner.split('_')[-1],
                "uid":str(uuid.uuid4()),
                "createTime":str(pendulum.now(TZ))
               
            }
            for filename in os.listdir(dirpath):
               
                img_path = os.path.join(dirpath, filename)
                print(img_path)
                file_hash = file_preprocess.generate_hash(img_path)
                verify_path.append(img_path)
                # if file_hash not in verify_hash:
                #     print("\t",img_path)
                #     verify_hash.append(file_hash)
                
                content_counter +=1
             
        
            runners_data["image_path"] = verify_path
            runners_data["image_counts"] = content_counter
        
            print(f"{i}: {runner}: matched {content_counter} images")
            
            datapack['runners'].append(runners_data)
            # time.sleep(0.5)
    
        with open("../Out/runner_data.json","w") as r:
            json.dump(datapack,r,indent=4)


   