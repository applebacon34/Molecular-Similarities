from django import forms

class input_for_mol(forms.Form):
    Smiles_input = forms.CharField(max_length=1000)