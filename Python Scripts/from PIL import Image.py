from PIL import Image
def Generated_Art():
    print('generated art')
    image = Image.new('RGB',(128,128),(0,0,0))
    image.save(test.png)
if __name__=='__main__':
    Generated_Art()