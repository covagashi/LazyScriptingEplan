# ToPathText Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text~ToPathText.html

---

Transforms this Text instance into a PathText instance.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual PathText ToPathText()
```
```

```
```
public:
virtual PathText^ ToPathText();
```
```

#### Return Value

A new PathText instance.

Remarks

After calling this method the current Text object becomes invalid (i.e. deleted) This method should not be called on an object that already is a PathText instance, otherwise an ObjectCreationException is thrown.



See Also

#### Reference

[Text Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text.html)
  
[Text Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text_members.html)
  
[PathText Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PathText.html)