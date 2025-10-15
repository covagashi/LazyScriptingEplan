# FUNC_ALLCONNECTIONDESCRIPTIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ALLCONNECTIONDESCRIPTIONS().html

---

Connection point descriptions (all) # 20039.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ALLCONNECTIONDESCRIPTIONS {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ALLCONNECTIONDESCRIPTIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Contains all connection point descriptions of a function. During entering (in the property dialog or for tabular editing) the individual values are separated by paragraph marks. For the display the values are separated by semicolons.

When setting the property an exception is thrown, if no value of the semicolon separated string is saved. This means the object has connection points (Pins) or the string is empty.
