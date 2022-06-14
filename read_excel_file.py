import os
import pandas as pd 
from PIL import Image



file_name2 = r'C:\Users\Rana\Desktop\mrinal\Python Scripts\Update_data_files2.xlsx'

df = pd.read_excel(file_name2)


images_file = os.listdir('./Test_Images') # images with extention.


columns = df.columns.to_list() # columns name list

def coordinateTuple(name, coordinateValue):
    coordinateValue =  tuple([int(i) for i in coordinateValue.split(',')])
    # print(len(coordinateValue))
  
    return coordinateValue, name

file_extention =  '.jpg'

imagesName = df['ImageFileName'].to_list() # list of image file name


for index, file_ in enumerate(images_file):
    image = os.path.join(
        r'C:\Users\Rana\Desktop\mrinal\Python Scripts\Test_Images', file_

    )

    img = Image.open(image)

    file_path = os.path.join(
    r'C:\Users\Rana\Desktop\mrinal\Python Scripts\croped image', file_[:-4] + "_" + str(index)  
    
    )


        print(index, 'xxxxxxxxxx')
        print(file_path)
        im = img.crop(LineNumber_Prect)
        im.save(file_path)


        for item in columns:
            # print(df[item].name)
            for coordinateIndex,coordinate in enumerate(df[item].to_list()):
                
                if df[item].name  in columns[2:]:
                    # print(df[item].name)
                    coordinateValue = coordinateTuple(df[item].name, coordinateValue = coordinate)
                    print(coordinateValue)
                    # print(coordinateIndex, coordinateValue)
               
                    print()
            



 

