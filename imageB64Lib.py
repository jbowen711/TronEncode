import base64
import os
from imageB64Lib import *

dir = os.path.dirname(os.path.realpath(__file__))

def encode_image_to_b64(src,target):
	"""
	Open the file, read it, encode it with b64
	"""
	with open('tron.jpg', 'b') as read_data:
		read_data = f.read

	encode_image_to_b64(dir+'/tron.jpg', dir+'/tronout.txt')
	pass

def decode_image_from_b64(src,target):
	"""
	open the b64 file, read it, decode using b64 decode
	"""
	with open('tronout.txt', 'b') as read_data:
		read_data = f.read
	decode_image_from_b64(dir+'/tronout.txt', dir+'/tron2.jpg')

	pass


def compare_image_files(src1,src2):
	"""
	Open both files, read them, compare them
	"""
	with open('tron2.jpg', 'b') as read_data:
		read_data = f.read
	with open('tron.jpg', 'b') as read_data:
		read_data = f.read

	compare_image_files(dir+'/tron.jpg', dir+'/tron2.jpg')
	compare_image_files(dir+'/tron.jpg', dir+'/tron2a.jpg')
	pass
