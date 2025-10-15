# MountingLineMate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingLineMate.html

---

Represents mounting line mate.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)  
      [Eplan.EplApi.DataModel.E3D.LineMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate.html)  
         **Eplan.EplApi.DataModel.E3D.MountingLineMate**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class MountingLineMate : LineMate
```
```

```
```
public ref class MountingLineMate : public LineMate
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MountingLineMate Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingLineMate~_ctor().html) | Default constructor. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Description.html) | Description of this mate. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [EndPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate~EndPoint.html) | End of LineMate. Coordinate is relative if Placement is not defined, otherwise it is absolute. (Inherited from [Eplan.EplApi.DataModel.E3D.LineMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate.html)) |
| Public Property | [IsBaseMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsBaseMate.html) | Return true, if mate is base mate. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsReadOnly.html) | Determines if Mate can be modified. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [IsUserDefined](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsUserDefined.html) | Returns true, if mate is used defined. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [MatchingMateNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~MatchingMateNames.html) | Names of mates that can be snapped to this one separated by '#'. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Name.html) | Name of this mate. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Placement.html) | [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) to which this mate is assign. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Rotation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Rotation.html) | Angle by which the components are to be rotated when they are placed on the mounting point. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [RotationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~RotationType.html) | Rotation type which this mate force while snapping. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Source](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Source.html) | Returns object from which the mate was returned or changed by: Placement3D.GetTargetMates, Placement3D.GetSourceMates, Placement3D.AddMatePersistent or BaseMate property. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [StartPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate~StartPoint.html) | Beginning of LineMate. Coordinate is relative if Placement is not defined, otherwise it is absolute. (Inherited from [Eplan.EplApi.DataModel.E3D.LineMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate.html)) |
| Public Property | [Transformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transformation.html) | Position and rotation relative to the parent placement represented by transformation matrix. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingLineMate~Create.html) | Creates a mounting line mate. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Dispose().html) | Destructor for deterministic finalization of Mate object. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Equals.html) | Operator of comparison implementation. Checks if two mates have same name and belongs to the same object. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Remove.html) | Removes the Mate object. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [StoreToObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~StoreToObject.html) | Stores changes into a project database. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [Transform](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transform.html) | Transform mate position. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |

[Top](#top)
