#! /usr/bin/python2
# -*- coding: utf-8 -*-
#from pythonvideoannotator_models.video.objects import Objects

import cv2, os
from pythonvideoannotator_models.models.video.objects.object2d import Object2D
from pythonvideoannotator_models.models.video.image import Image

class VideoBase(object):

	def __init__(self, project):
		self._filename = None
		self._videocap = None
		self._path 	   = None
		self._project  = project
		self._project  += self

		self._objects  = []
		self._images   = []
			

	######################################################################################
	#### FUNCTIONS #######################################################################
	######################################################################################

	def __str__(self): return self.name

	def __add__(self, obj):
		if isinstance(obj, Object2D): self._objects.append(obj)
		if isinstance(obj, Image): self._images.append(obj)
		return self

	def __sub__(self, obj):
		if isinstance(obj, Object2D): self._objects.remove(obj)
		if isinstance(obj, Image): self._images.remove(obj)
		return self

	def create_object(self): return Object2D(self)
	def create_image(self): return Image(self)

	######################################################################################
	#### PROPERTIES ######################################################################
	######################################################################################

	
	@property
	def path(self): return self._path

	@property
	def objects(self): return self._objects

	@property
	def images(self): return self._images

	@property
	def filepath(self): return self._filename
	@filepath.setter
	def filepath(self, value): 
		self._filename = value
		self._videocap = cv2.VideoCapture(value)

	@property
	def filename(self): return os.path.basename(self.filepath)
	
	@property
	def name(self):
		try:
			name, extension = os.path.splitext(self.filename)
			return name
		except:
			return ''
	

	@property
	def video_capture(self): return self._videocap

	@property
	def total_frames(self): return self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT)

	@property
	def project(self): 	return self._project
