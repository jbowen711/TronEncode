from imageB64Lib0 import *

dir = os.path.dirname(os.path.realpath(__file__))

encode_image_to_b64(dir+'/tron.jpg', dir+'/tronout.txt')
decode_image_from_b64(dir+'/tronout.txt', dir+'/tron2.jpg')
compare_image_files(dir+'/tron.jpg', dir+'/tron2.jpg')
compare_image_files(dir+'/tron.jpg', dir+'/tron2a.jpg')
