#! /usr/bin/python2
# -*- coding: utf-8 -*-
from pythonvideoannotator_models.models.video import Video

class ProjectBase(object):

	def __init__(self):
		self._videos = []

	######################################################################################
	#### FUNCTIONS #######################################################################
	######################################################################################

	def __add__(self, obj):
		if isinstance(obj, Video): self._videos.append(obj)

		return self

	def __sub__(self, obj):
		if isinstance(obj, Video): self._videos.remove(obj)

		return self
		

	def create_video(self): return Video(self)

	######################################################################################
	#### PROPERTIES ######################################################################
	######################################################################################

	@property
	def videos(self): return self._videos
	@videos.setter
	def videos(self, value): self._videos = value