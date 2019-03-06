#Importing packages  

import shutil
import os
import csv

#Preprocessing first dataset  

file = "./Pokemon/data/pokemon_types_names.csv"
with open(file,'r') as f: 
        reader = csv.reader(f)
        next(reader,None) #Skip the header
        pkm_dict1 = {rows[1]:rows[2] for rows in reader}

for pkm_name, pkm_type in pkm_dict1.items():
            source = './Pokemon/pokemon-generation-one/{pkm_name}/'.format(pkm_name=pkm_name) 
            dest = './Pokemon/dataset/{pkm_type}'.format(pkm_type=pkm_type)
            for f in os.listdir(source):
                if not os.path.exists(dest):
                    os.makedirs(dest)
                shutil.copy(source+f, dest)
         
#Preprocessing second dataset  
            
file = "./Pokemon/data/pokemon_types.csv"
with open(file,'r') as f: 
        reader = csv.reader(f)
        next(reader,None) #Skip the header
        pkm_dict2 = {rows[0]:rows[1] for rows in reader}

for pkm_no, pkm_type in pkm_dict2.items():
            source = './Pokemon/pokemon-images-dataset/{pkm_no}.png'.format(pkm_no=pkm_no) 
            dest = './Pokemon/dataset/{pkm_type}'.format(pkm_type=pkm_type)
            if not os.path.exists(dest):
                os.makedirs(dest)
            shutil.copy(source, dest)
                
