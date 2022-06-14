import os
from isort import file
import pandas as pd 
from PIL import Image


file_name2 = r'C:\Users\mnhtel\Documents\Python Scripts\Update_data_files.xlsx'

df = pd.read_excel(file_name2)
# print(df.head())

images_file = os.listdir('./Test_Images')
# print(images_file)

for index, row in df.iterrows():
    ImageFileName = row["ImageFileName"]


    # print(ImageFileName,LineNumber_orig, LineNumber_Prect, SelfGivenName_Prect)
    ImageFileName_only = ImageFileName
    file_extention = ".j2k"
    ImageFileName = ImageFileName + file_extention
    # print(ImageFileName_only)

    for index, file_ in enumerate(images_file):
        if file_ == ImageFileName:
            image = os.path.join(
                r"C:\Users\mnhtel\Documents\Python Scripts\Test_Images", ImageFileName
                )
            # print(image)

            img = Image.open(image)
            # width, height = img.size
            # # print(LineNumber_Prect)
            LineNumber_PrectForFileName = '-'.join([i for i in LineNumber_Prect.split(',')])
            # print(LineNumber_PrectForFileName)

            # # print(width, height)
            file_path = os.path.join(
                r'C:\Users\mnhtel\Documents\Python Scripts\croped image', ImageFileName_only + "_" + str(LineNumber_orig) + LineNumber_PrectForFileName +  file_extention
            )
            # print(file_path)

            LineNumber_Prect = tuple([int(i) for i in LineNumber_Prect.split(',')])
            # print(LineNumber_Prect)
            # # print(type(LineNumber_Prect))
            # print(LineNumber_Prect)
            # # im = img.crop((int(float(LineNumber_Prect[0])), int(float(LineNumber_Prect[3])), int(float(LineNumber_Prect[2])), int(float(LineNumber_Prect[1]))))
            im = img.crop(LineNumber_Prect)
            im.save(file_path)

   

print('finished.')




  
   

