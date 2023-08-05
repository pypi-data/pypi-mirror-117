# PopcornGL
A Python module based on my custom graphics engine.

This project is in open Alpha, and will improve depending on the attention it gets.

# Requirements
Python versions tested: 3.9.6

Python modules needed:
 - operator
 - math
 - copy

# How to Install
To install PopcornGL you need to run the command `pip install popcorngl` in your command prompt. If the command does not work, create an issue relating the problem and I'll see if I can help you.

# Documentation
## Classes
### Camera(x_rotation, y_rotation, z_rotation, fov, center, distance)
This class is responsible for the camera in the scene.

**Class Functions:**  
*rotate_x(amount)*: rotates the camera a certain amount on the X axis around the center of the scene.  
*rotate_y(amount)*: rotates the camera a certain amount on the Y axis around the center of the scene.  
*rotate_z(amount)*: rotates the camera a certain amount on the Z axis around the center of the scene.  
*change_distance(amount)*: moves the camera further away from the object by a certain amount.  

**Class Variables:**  
*x_rotation*: the cameras rotation on the X axis.  
*y_rotation*: the cameras rotation on the Y axis.  
*z_rotation*: the cameras rotation on the Z axis.  
*fov*: the cameras fov. (not actually the FOV I just didnt know what else to call it)  
*center*: the center of the screen.  
*distance*: the distance from the object in the scene.  

### Light(position, intensity, radius)
This class is responsible for the lighting in the scene. It's not necessary if you're not going to use it.

**Class Variables:**  
*position*: The position of the light in the scene.  
*intensity*: The intensity of the light.  
*radius*: The range of the light.  

### Engine()
This class is responsible for functions that do math.

**Class Functions:**  
*do_3d_math(points, camera)*: This function returns the X and Y values of the points with 3D coords passed in it.  
*do_light_math(faces, points, light)*: This function returns the faces list with modification to the color based on the light.  
*sort_faces(faces)*: This function returns a sorted list of faces based on the depth of them in the scene (for painter's algorithm).
