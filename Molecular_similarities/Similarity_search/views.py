from django.shortcuts import render
from Similarity_search import forms
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import AllChem
from pathlib import Path
import json
import os
from Molecular_similarities.settings import BASE_DIR
from rdkit.Chem import Draw
from PIL import Image
# Create your views here.
working_dir  = os.path.join(BASE_DIR, 'static/Json/cleaned_ecmdb.json')
with open(working_dir,'r', encoding='utf-8') as file:
    ecoli_data = json.load(file)


form = forms.input_for_mol()


def home(request):
    fpgen = AllChem.GetRDKitFPGenerator(fpSize=4096)
    
    if request.method == 'POST':
        input = forms.input_for_mol(request.POST)
        
        if input.is_valid():
            input_image_dir = os.path.join(BASE_DIR, 'static/input_image/')

            fp_list = []
            input_molecule_smile  = input.cleaned_data['Smiles_input']
            
            
            MOL_input = Chem.MolFromSmiles(input_molecule_smile)
            if MOL_input == None:
                return render(request, 'Similarity_search/result.html')
            else:

                fp_input = fpgen.GetFingerprint(MOL_input)
                img = Draw.MolToImage(MOL_input)
                img.save(input_image_dir+'user_input.png', 'PNG')
                
                
                fp_list.append(fp_input)
                count = 1
                res = []
                for item in ecoli_data:
                            
                    
                    
                    MOL_candidate = Chem.MolFromSmiles(item['smiles'])
                    
                    fp_candidate = fpgen.GetFingerprint(MOL_candidate)    
                    fp_list.append(fp_candidate)

                    comparison = DataStructs.TanimotoSimilarity(fp_list[0],fp_list[count])
                    count=count+1
                    if comparison > 0.8:
                        res_dict = {}
                        res_dict.update({'name': item['name']})
                        res_dict.update({'description': item['description']})
                        res_dict.update({'smiles': item['smiles']})
                        res_dict.update({'id': item['id']})
                        res.append(res_dict)
                        res_dict={}

                    else:
                        pass
                    
                return render(request, 'Similarity_search/home.html', context={'matches':res})
                
            
    return render(request, 'Similarity_search/home.html', context = {'form':form})

