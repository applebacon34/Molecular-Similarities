import json
import os
from Molecular_similarities.settings import BASE_DIR
from rdkit.Chem import Draw
from rdkit import Chem
from PIL import Image
working_dir  = os.path.join(BASE_DIR, 'static/Json/cleaned_ecmdb.json')
with open(working_dir,'r', encoding='utf-8') as file:
    data = json.load(file)

def save_img():
    for item in data:
        to_MOL = Chem.MolFromSmiles(item['smiles'])
        img = Draw.MolToImage(to_MOL)
        img.save("C:\\Users\\Maxym\\Desktop\\MyDjangoStuff\\Molecular_similarities\\static\\Images\\"+str(item['id'])+'.png')
        print("saving", item['id'])
if __name__ == '__main__':
    save_img()
