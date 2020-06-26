# importing os module 
import os 
import argparse
import re 
  
# Function to rename multiple files 
def renameFiles(directoryPath):
    print("**************")
    print("   RENAMING   ")
    print("**************")
    for count, filename in enumerate(os.listdir(directoryPath)): 
        source = directoryPath + "/" + filename
        print("Source " + source)
        
        dirname = os.path.basename(directoryPath)
        temp = re.findall(r'\d+', dirname) 
        saisonNumber = list(map(int, temp)) 

        temp = re.findall(r'\d+', filename) 
        episodeNumber = list(map(int, temp)) 
        
        name, extension = os.path.splitext(filename)
        destination = directoryPath + "/" + "s" + str(saisonNumber[0]) +"e" + str(episodeNumber[1]) + extension
        print("Destination : " + destination)
        print("-----")
        
        # rename() function will 
        # rename all the files 
        os.rename(source, destination)
    print("**************")
    print("     DONE     ")
    print("**************")
  
# Main method 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Rename multiple files.')
    parser.add_argument('-d', '--directoryPath', required=True,
                   help='Directory path where rename files for example : my/directory')

    args = parser.parse_args() 
    renameFiles(args.directoryPath) 
