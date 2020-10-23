#######################################
# Author: Liam McGunnigle
# Date: 10/21/2020
# License: MIT
#######################################

#necessary imports to convert formats
import easygui

#from coremltools.converters import keras
import coremltools as ct
from tensorflow.keras import models

#select model to convert
h5_path = easygui.fileopenbox(filetypes='.h5')

#convert model
print('converting model')
h5 = models.load_model(h5_path)
model = ct.convert(h5)
#model = keras.convert(h5_path, input_names=['image'], output_names=['output'], image_input_names='image')

#update metadata
model.class_labels = easygui.codebox(msg="enter the output class labels as ['output class 1', 'output class 2', ...] ")
model.author = 'Liam McGunnigle'
model.short_desription = easygui.enterbox(msg='enter a short description of your model')
model.long_description = easygui.enterbox(msg='enter a longer description of your model')
#model.output_description = easygui.enterbox(msg='enter a description of the output of your model')
model.license = 'MIT'
model.version = '1'

#view model
#model.visualize_spec()

#save model
mlmodel_path = easygui.filesavebox(filetypes='.mlmodel')
model.save(mlmodel_path)

