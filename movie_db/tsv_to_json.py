import json 
  
def tsv2json(input_file,output_file): 
    arr = [] 
    with open(input_file, 'r', encoding='utf-8') as file:  # Specify the encoding here
        titles = [t.strip() for t in file.readline().split('\t')]
        
        for line in file: 
            d = {t: f.strip() for t, f in zip(titles, line.split('\t'))}
            arr.append(d)
         
        # we will append all the individual dictionaires into list  
        # and dump into file. 
    with open(output_file, 'w', encoding='utf-8') as output_file: 
        output_file.write(json.dumps(arr, indent=4)) 
  
# Driver Code 
input_filename = 'roles.tsv'
output_filename = 'roles.json'
tsv2json(input_filename,output_filename)