# Contents Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text~Contents.html

---

Contents of object represented by this type.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override MultiLangString Contents {get; set;}
```
```

```
```
public:
property MultiLangString^ Contents {
   MultiLangString^ get() override;
   void set (    MultiLangString^ value) override;
}
```
```

#### Property Value

[Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) stored in the TextBase.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when setting a value and this object is of type [PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html). |

Remarks

It is invalid to set content of [PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html) and because of it an exception is thrown when setting the value for object of that type.



See Also

#### Reference

[Text Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text.html)
  
[Text Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text_members.html)
  
[MultiLangString Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html)