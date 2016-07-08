import sys
from PIL import Image

# define flip function
def flip(x):
    x = x.transpose(Image.FLIP_LEFT_RIGHT)
    #img.show()
    return

if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()

# call flip function
#flip(img)
#img.show()