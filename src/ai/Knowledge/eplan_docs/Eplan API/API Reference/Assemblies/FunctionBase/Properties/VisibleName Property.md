# VisibleName Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~VisibleName.html

---

Returns the visible name of the FunctionBase.

Syntax

**C#**
**C++/CLI**


public virtual string VisibleName {get; set;}

public:

virtual property String^ VisibleName {

   String^ get();

   void set (    String^ value);

}


#### Property Value

name of the function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the visible name cannot be retrieved from the function |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | FunctionBase is transient. |
| [System.ArgumentNullException](#) | Thrown while setting when the new value is `null`. |
