import os
import pandas as pd 
from PIL import Image



file_name2 = r'C:\Users\Rana\Desktop\mrinal\Python Scripts\Update_data_files2.xlsx'

df = pd.read_excel(file_name2)


images_file = os.listdir('./Test_Images2') # images with extention.


columns = df.columns.to_list() # columns name list

def coordinateTuple(name, coordinateValue):
    coordinateValue =  tuple([int(i) for i in coordinateValue.split(',')])
    # print(len(coordinateValue))
  
    return coordinateValue, name

file_extention =  '.jpg'

imagesName = df['ImageFileName'].to_list() # list of image file name


for index, file_ in enumerate(images_file):
    # print(index, file_)
    image = os.path.join(
        r'C:\Users\Rana\Desktop\mrinal\Python Scripts\Test_Images2', file_

    )
    # print(image)


    img = Image.open(image)


    def coordinateTuple(name, coordinateValue):
        coordinateValueTuple =  tuple([int(i) for i in coordinateValue.split(',')])
        return coordinateValueTuple, name




    for item in columns:
        # print(df[item].name)
        for coordinateIndex,coordinate in enumerate(df[item].to_list()):
            if df[item].name  in columns[2:]: 
                coordinet = coordinateTuple(df[item].name, coordinateValue = coordinate)

                # print(coordinet)

                file_path = os.path.join(
                        r'C:\Users\Rana\Desktop\mrinal\Python Scripts\croped image', file_[:-4] + "_" + str(coordinateIndex) +"_" + df[item].name +"_"+ file_extention

                        )

                im = img.crop((coordinet[0]))
                im.save(file_path)




           



 

