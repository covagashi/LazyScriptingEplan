# ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic57.html

---

Mass moment of inertia of the load # 26443.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Describes the resistance of a load to changes in its rotation around an axis. This is a measure of how difficult it is to change the rotational speed of the load and depends on the mass distribution of the load relative to the axis of rotation. Example: In the case of a rotating flywheel in a machine, the mass moment of inertia indicates the torque required to change the rotational speed of the flywheel.



See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](topic1766.html)