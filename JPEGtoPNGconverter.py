import sys
import os 
from PIL import Image

# grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(new_folder,output_folder)

# check if new folder exist, if not create it.
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
# print(new_folder, output_folder)

# loop through pokedex 
# convert images to png 
# save images
for filename in os.listdir(image_folder):
	img = Image.open(f'{new_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]

	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done brother!')