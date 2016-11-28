#! /usr/bin/python2
# -*- coding: utf-8 -*-
import os
from pysettings import conf
from send2trash import send2trash
from pythonvideoannotator.utils import tools
from pythonvideoannotator_models.models.project_base import ProjectBase

class ProjectIO(ProjectBase):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################
	
	def save(self, data, project_path=None):
		data['videos'] = []

		videos_path = os.path.join(project_path, 'videos')
		if not os.path.exists(videos_path): os.makedirs(videos_path)

		paths = []
		for video in self.videos:
			video_data = video.save({}, videos_path)
			data['videos'].append(video_data)
			paths.append(video.path)

		for video_path in tools.list_folders_in_path(videos_path):
			if video_path not in paths: send2trash(video_path)

		return data

	def load(self, data, project_path=None):
		videos_path = os.path.join(project_path, 'videos')		
		videos_dirs = tools.list_folders_in_path(videos_path)

		for video_dir in videos_dirs:
			video = self.create_video()
			video.load(data, video_dir)