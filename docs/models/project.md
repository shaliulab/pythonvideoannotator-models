# Class models.Project

## **Variables**
***************************

### self.\_videos

Private variable where the videos from the project are stored.

## **Properties**
***************************

### videos

Used to get and set the list of videos of the project.

## **Functions**
***************************

### create_video

Factory to create an object that represents the Video Model.

```python
project = Project()
project.create_video()
```

### \_\_add\_\_

Used to add a new child Model to the project.

```python
project = Project()
project += Video()
```

**note:** The example above is just to show what the function \_\_add\_\_ does. A child video should be added as the example shown in the create_video() function.

### \_\_sub\_\_

```python
project = Project()
video = Video()
project += video
project -= video
```

