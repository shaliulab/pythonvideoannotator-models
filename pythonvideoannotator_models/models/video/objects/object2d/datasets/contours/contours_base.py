import cv2, math, os, numpy as np
from pythonvideoannotator_models.models.video.objects.object2d.utils.interpolation import interpolate_positions
from pythonvideoannotator_models.models.video.objects.object2d.datasets.dataset import Dataset

def points_angle(p1, p2): 
	x1, y1 = p1
	x2, y2 = p2
	rads = math.atan2(y2-y1,x2-x1)
	#rads %= 2*np.pi
	return rads
"""
def points_angle(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return (ang1 - ang2) % (2 * np.pi)"""

def min_dist_angles(ang1, ang2):
    tmp = max(ang1, ang2)
    ang2 = min(ang1, ang2)
    ang1 = tmp
    angle1 = abs(ang1-ang2)
    angle2 = abs(ang1-(np.pi*2)-ang2)
    angle3 = abs(ang1+(np.pi*2)-ang2)
    return min(angle1, angle2, angle3)
  

class ContoursBase(Dataset):

	def __init__(self, object2d):
		super(ContoursBase, self).__init__(object2d)
		
		self.object2d   = object2d
		self.name 		= 'contours({0})'.format(len(object2d)) if len(object2d)>0 else 'contours'
		self._contours 	= []
		self._angles 	= []


		
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
		if M["m00"]==0:
			return None
		else:
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
			dists = list(map( lambda p: self.__lin_dist( p[0], centroid ), contour ))
			ndx = dists.index(max(dists))			
			head = tuple(contour[ndx][0])
			
			dists = list(map( lambda p: self.__lin_dist( p[0], contour[ndx][0] ), contour ))
			ndx = dists.index(max(dists))
			tail = tuple(contour[ndx][0])

			angle = self.get_angle(index)
			if angle is not None:
				angle1 = points_angle(centroid, head)
				angle2 = points_angle(centroid, tail)

				diff1 = min_dist_angles(angle, angle1)
				diff2 = min_dist_angles(angle, angle2)
				if diff1>diff2:
					return tail, head			
			
			return head, tail
		else:
			return None, None

	def get_angle(self, index):
		if index<0 or index>=len(self._angles): return None
		return self._angles[index] if self._angles[index] is not None else None

	def get_angular_velocity(self, index):
		a1 = self.get_angle(index)
		a2 = self.get_angle(index+1)
		return min_dist_angles(a1, a2) if (a1 is not None and a2 is not None) else None

	def get_contour(self, index):
		if index<0 or index>=len(self._contours): return None
		return self._contours[index] if self._contours[index] is not None else None

	def set_contour(self, index, contour, angle=None):
		# add contours in case they do not exists
		if index >= len(self._contours):
			for i in range(len(self._contours), index + 1): 
				self._contours.append(None)
				self._angles.append(None)

		self._contours[index] = contour

		# No angle was provided to save, we will try to calculate one
		if angle is None:
			p1, p2 = self.get_extreme_points(index)
			centroid = self.get_position(index)
			if centroid is not None:
				angle1  = points_angle(centroid,p1)
				angle2  = points_angle(centroid,p2)

				# Search for the last angle
				last_angle = None
				for i in range(index-1, -1, -1):
					tmp_angle = self._angles[i]
					if tmp_angle is not None: 
						last_angle = tmp_angle
						break

				# try to match the current angle with the last angle.
				# angles cannot switch values drastically
				if last_angle is not None:
					diff1 = min_dist_angles(last_angle, angle1)
					diff2 = min_dist_angles(last_angle, angle2)
				
					self._angles[index] = angle2 if diff1>diff2 else angle1
				else:
					#print math.degrees(angle)
					self._angles[index] = angle1
			else:
				self._angles[index] = angle
		else:
			self._angles[index] = angle
         
	def set_data_from_blob(self,index, blob):
		if blob is None:
			self.set_contour(index, None)
		else:
			self.set_contour(index, blob._contour)


	
	
	

	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	