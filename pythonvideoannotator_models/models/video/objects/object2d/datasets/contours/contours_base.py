import cv2, math, os, numpy as np
from pythonvideoannotator_models.models.video.objects.object2d.utils.interpolation import interpolate_positions
from pythonvideoannotator_models.models.video.objects.object2d.datasets.dataset import Dataset



class ContoursBase(Dataset):

	def __init__(self, object2d):
		self.object2d   = object2d
		self.object2d   += self
		self.name 		= 'contours({0})'.format(len(object2d)) if len(object2d)>0 else 'contours'
		self._contours 	= []
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): 				return len(self._contours)
	def __getitem__(self, index): 	return self._contours[index] if index<len(self) else None
	def __str__(self):				return self.name

	
	######################################################################
	### DATA ACCESS FUNCTIONS ############################################
	######################################################################

	def get_position(self, index):
		cnt = self.get_contour(index)
		if cnt is None: return None
		M = cv2.moments(cnt)
		return int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])

	def get_velocity(self, index):
		p1 = self.get_position(index)
		p2 = self.get_position(index-1)
		if p1 is None or p2 is None: return None
		return p2[0]-p1[0], p2[1]-p1[1]
		
	def get_acceleration(self, index):
		v1 = self.get_velocity(index)
		v2 = self.get_velocity(index-1)
		if v1 is None or v2 is None: return None
		return v2[0]-v1[0], v2[1]-v1[1]

	def get_bounding_box(self, index):
		cnt = self.get_contour(index)
		if cnt is None: return None
		return cv2.boundingRect(cnt)
		
	def get_fit_ellipse(self, index):
		cnt = self.get_contour(index)
		if cnt is None: return None
		return cv2.fitEllipse(cnt)
		
	def get_convex_hull(self, index):
		cnt = self.get_contour(index)
		if cnt is None: return None
		pass

	def __lin_dist(self, p1, p2): return np.linalg.norm( (p1[0]-p2[0], p1[1]-p2[1]) )

	def get_extreme_points(self, index):
		centroid = self.get_position(index)
		contour  = self.get_contour(index)

		if centroid is not None and contour is not None:
			dists = map( lambda p: self.__lin_dist( p[0], centroid ), contour )
			ndx = dists.index(max(dists))			
			head = tuple(contour[ndx][0])
			
			dists = map( lambda p: self.__lin_dist( p[0], contour[ndx][0] ), contour )
			ndx = dists.index(max(dists))
			tail = tuple(contour[ndx][0])
			
			return head, tail
		else:
			return None, None


	def get_contour(self, index):
		if index<0 or index>=len(self._contours): return None
		return self._contours[index] if self._contours[index] is not None else None

	def set_contour(self, index, contour):
		# add contours in case they do not exists
		if index >= len(self._contours):
			for i in range(len(self._contours), index + 1): self._contours.append(None)
		self._contours[index] = contour
	
	def set_data_from_blob(self,index, blob):
		if blob is None:
			self.set_contour(index, None)
		else:
			self.set_contour(index, blob._contour)


	
	
	

	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	