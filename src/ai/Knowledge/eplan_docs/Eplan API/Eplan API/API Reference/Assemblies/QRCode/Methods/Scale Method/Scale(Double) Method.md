# Scale(Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode~Scale(Double).html

---

Scales the QRCode by the specified factor in X and Y axis.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Scale( 
   double factor
)
```
```

```
```
public:
void Scale( 
   double factor
)
```
```

#### Parameters

*factor*
:   Scaling factor. E.g. value of 2 makes the width two times bigger.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when this method is called on an object that cannot be scaled. |

Remarks

When using this method, the scaling origin point is (0, 0).



See Also

#### Reference

[QRCode Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode.html)
  
[QRCode Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode~Scale.html)