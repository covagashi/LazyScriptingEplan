# ParserParameter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html

---

Parameter Class for the usage with UnitParser. Configure the unit and the look of the Parser result.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.ParserParameter**  
      [Eplan.EplApi.DataModel.Graphics.ProjectParserParameter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ProjectParserParameter.html)

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class ParserParameter
```
```

```
```
public ref class ParserParameter
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ParserParameter Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~_ctor.html) | Constructor |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [GridSize](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~GridSize.html) | The grid size in millimeters. p.e. "4#" means 4 times grid size |
| Public Property | [Group](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Group.html) | The UnitGroup Property. When first UnitID is set,the group is automatically defined by the unit. While setting a Group also the Unit can be changed to the first Unit in new Group if: - new Group is different than the Group of assigned Unit - there is no Unit and Group assigned When new assigned Group is the same like Unit Group, nothing will change. The unitparser can never convert units of different groups |
| Public Property | [HideUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~HideUnit.html) | Hide the unit of the parsed result. |
| Public Property | [HideValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~HideValue.html) | Hide the value of the parsed result, all other texts (units and additional texts) will remain. |
| Public Property | [OnlyFirstValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~OnlyFirstValue.html) | Display only the first Value. |
| Public Property | [OnlyUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~OnlyUnit.html) | Display only the Unit. |
| Public Property | [Precision](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Precision.html) | Set the precision of the result (Values used for calculation: 0 up to 8) |
| Public Property | [SpaceBetweenUnitAndValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~SpaceBetweenUnitAndValue.html) | Add a space between Unit and the value |
| Public Property | [SuppressFloatingZeroes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~SuppressFloatingZeroes.html) | Suppress the last zeroes of a floating result. |
| Public Property | [UnitFromParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~UnitFromParameter.html) | Get if the unit needs extra parameter to get resolved. Use the project dependend parameter class if this is true. |
| Public Property | [UnitID](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~UnitID.html) | The UnitId Property. Set or get the unit of the parameters. |
| Public Property | [WithoutLimiters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~WithoutLimiters.html) | The unit is NOT separated by one of this chars: blank (){}[].,:;!?/\\ |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CanParse](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~CanParse.html) | Parsing can start when the unitid is not empty |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Dispose().html) | Destructor for deterministic finalization of ParserParameter object. |

[Top](#top)
