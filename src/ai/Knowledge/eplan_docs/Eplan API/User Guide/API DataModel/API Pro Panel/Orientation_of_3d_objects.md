In Pro Panel API it is sometimes necessary to recognize sides of a 3D object, for example to place them in a row with the same orientation.

Please mind that the sides of a  Placement3D  are something different than the sides of its minimal bounding box. They are related to the same part of the object 3D, independently of a transformation and a viewpoint.

The representation of sides is in the  .Corners  property, for example:

**Placement3D.Corners.UpperRightBackAbsolute**  â Returns the upper right back coordinate in an absolute system.  
**Placement3D.Corners.LowerRightFrontRelative**  â Returns the lower right front coordinate in a relative system.

### Objects with placement area

In this case, orientation is according to placement area.

Example terminal:

![](images/ProPanelAPI/orientation_terminal1.jpg)

![](images/ProPanelAPI/orientation_terminal2.jpg)

Example rack:

![](images/ProPanelAPI/orientation_rack.jpg)

### Objects without placement area

In this case, orientation is according to the absolute axis origin (assumed identity transformation):

|  |  |
| --- | --- |
| Front | side with the lowest Y |
| Back | side with highest Y |
| Right | side with highest X |
| Left | side with lowest X |
| Top | side with highest Z |
| Bottom | side with lowest Z |

SE isometric viewpoint:

![](images/ProPanelAPI/orientation_without_pa1.jpg)

SW isometric viewpoint :

![](images/ProPanelAPI/orientation_without_pa2.jpg)

See Also

[API Pro Panel](API_Pro_Panel.html)