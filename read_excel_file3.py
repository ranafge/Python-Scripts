import os
import pandas as pd 
from PIL import Image


file_name2 = r'C:\Users\Rana\Desktop\mrinal\Python Scripts\Update_data_files2.xlsx'

df = pd.read_excel(file_name2)

images_file = os.listdir('./Test_Images2') # images with extention.


columns = df.columns.to_list() # columns name list



file_extention =  '.jpg'

imagesName = df['ImageFileName'].to_list() # list of image file name


for index, file_ in enumerate(images_file):
    image = os.path.join(
        r'C:\Users\Rana\Desktop\mrinal\Python Scripts\Test_Images2', file_

    ) # full path with extention


    img = Image.open(image)
    coordinateVluaeWithName = ''

    def coordinateTuple(name, coordinateValue):
        coordinateValue =  tuple([int(i) for i in coordinateValue.split(',')])
        # print(len(coordinateValue))
        print(coordinateValue, name)
        return coordinateValue, name


    file_path = os.path.join(
    r'C:\Users\Rana\Desktop\mrinal\Python Scripts\croped image', file_[:-4] + "_" + str(index)  

    )
    # print(file_path, 'xx')
    # im = img.crop(LineNumber_Prect)
    # im.save(file_path)


    for item in columns:
        for coordinateIndex,coordinate in enumerate(df[item].to_list()):
            
            if df[item].name  in columns[2:]:
                coordinateTuple(df[item].name, coordinateValue = coordinate)
                

            

        





