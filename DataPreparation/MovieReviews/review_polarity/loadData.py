from os import listdir


#function to load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r' )
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

#load all documents from the negative directory

def process_docs(directory):
#walk through all files in the folder 
    for filename in listdir(directory):
        #skip the files that do not have the right extension 
        if not filename.endswith(".txt"):
            next
            
        # create the full path of the file to open
        path = directory + '/' + filename
        # load document
        doc = load_doc(path)
        print( 'Loaded %s' % filename)
        
#specify directory to load
directory = 'txt_sentoken/neg'
process_docs(directory)