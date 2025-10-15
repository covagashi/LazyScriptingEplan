# PlanningSegment Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PlanningSegment.html

---

Determines the planning segment to which all function inserted from window macro on page will be assign.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PlanningSegment PlanningSegment {get; set;}
```
```

```
```
public:

property PlanningSegment^ PlanningSegment {

   PlanningSegment^ get();

   void set (    PlanningSegment^ value);

}
```
```

Example

- [C#](#i-tab-content-ba02cef9-b00d-4f8c-a528-3f3c2fb153d3)

```
//create insert service

Insert oInsert = new Insert();



//set planning segment to which functions from macro will be assigned

oInsert.PlanningSegment = oPlanningSegment;



//insert a window macro

StorableObject [] arrInsertedSorableObjects = oInsert.WindowMacro(

    strPath,

    iVariant,

    oSchematicPage,

    oLocation,

    Insert.MoveKind.Absolute);



//get first inserted function 

Function oInsertedFunction = arrInsertedSorableObjects.OfType<Function>().FirstOrDefault();





```
