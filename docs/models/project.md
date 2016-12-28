# Class models.Project

## **Variables**
***************************

### self.\_videos

Private variable where the videos from the project are stored.

### self.\_path

Private variable that stores the path of the project.

## **Properties**
***************************

### videos

Used to get and set the list of videos of the project.

### path

Returns the path of the project.

## **Functions**
***************************

### \_\_add\_\_(obj)

Used to add a new child Model to the project.

```python
project = Project()
project += Video()
```

**note:** The example above is just to show what the function \_\_add\_\_ does. A child video should be added as the example shown in the create_video() function.

### \_\_sub\_\_(obj)

```python
project = Project()
video = Video()
project += video
project -= video
```

### create_video

Factory to create an object that represents the Video Model.

```python
project = Project()
project.create_video()
```

### load(data, project_path=None)

Function called to load the project.
**data** - dictionary with the project description.
**project_path** - path to the project.

### save(data, project_path=None)

Function called to save the project.
**data** - dictionary where the project description will be stored.
**project_path** - path where to save the project.