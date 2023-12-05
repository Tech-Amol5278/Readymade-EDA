import os
import pandas as pd

def getData(file):
    '''
        file >> accept filename.ext
        returns dataframe
        
        **Assumptions "data_file.csv" in current_directory/data
        example : 
            df = getData('data_file.csv')
    '''    
    
    dataDir = os.path.join(os.getcwd(),"data")
    datPath = os.path.join(dataDir,file)
    print(datPath)
       
    return pd.read_csv(datPath)
##########################################################################################################
##########################################################################################################
##########################################################################################################
def filePrint(filePath,text):
    # print(filePath)
    ############### write to filePath ###############################
    f = open(filePath, "a")
    f.write(text)
    f.close()

    return




