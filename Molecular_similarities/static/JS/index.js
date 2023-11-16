
var ketcherFrame = document.getElementById('ifKetcher');
var ketcher = null;


    

function exportSMILES(){
    ketcher = ketcherFrame.contentWindow.ketcher;
    if ('contentDocument' in ketcherFrame){
        promise = ketcher.getSmiles()
        promise.then(function(e){
            document.getElementById("id_Smiles_input").value = e;
        })
    }
        

        
    
}        


    



    