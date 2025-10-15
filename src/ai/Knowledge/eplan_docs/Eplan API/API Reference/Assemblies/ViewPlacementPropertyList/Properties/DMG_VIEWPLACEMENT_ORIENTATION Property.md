# DMG_VIEWPLACEMENT_ORIENTATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_ORIENTATION().html

---

Model view: Rotation # 36514.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DMG_VIEWPLACEMENT_ORIENTATION {get; set;}
```
```

```
```
public:

property PropertyValue^ DMG_VIEWPLACEMENT_ORIENTATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Rotates the content of the model view by 90Â°, 180Â° or 270Â° counterclockwise. This can be useful in order to make optimum use of highly-formatted model views on pages in landscape orientation. The border of the model view is not rotated. Texts in a model view that is rotated by 90Â° are rotated by the same angle. The exception are property texts to be read from the right. For them to remain legible, they are rotated by -90Â°.
