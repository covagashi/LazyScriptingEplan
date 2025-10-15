# AssignedObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~AssignedObjects.html

---

Gets/Sets a list of StorableObject references to a PlaceHolder object. The originally assigned references are replaced.

Syntax

**C#**
**C++/CLI**


public virtual StorableObject[] AssignedObjects {get; set;}

public:

virtual property array<StorableObject^>^ AssignedObjects {

   array<StorableObject^>^ get();

   void set (    array<StorableObject^>^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |
