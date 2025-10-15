# WriteProtected Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~WriteProtected.html

---

Check if object is currently write protected or sets Manual write protection

Syntax

**C#**
**C++/CLI**


public virtual bool WriteProtected {get; set;}

public:

virtual property bool WriteProtected {

   bool get();

   void set (    bool value);

}


#### Property Value

true : if object is currently write-protected

false : if no write protection was set or if write protection was disabled

Exceptions

| Exception | Description |
| --- | --- |
| [WriteProtectionChangeNotAllowed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionChangeNotAllowed.html) | Thrown if because of current write protection state, no further modifications are allowed. |
