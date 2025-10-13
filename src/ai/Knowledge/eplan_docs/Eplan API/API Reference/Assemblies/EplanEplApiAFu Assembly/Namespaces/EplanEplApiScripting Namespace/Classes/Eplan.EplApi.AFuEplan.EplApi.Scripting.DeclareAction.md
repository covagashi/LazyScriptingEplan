Attribute used to mark a method of a class in a [Scripts](Scripts.html) so that this method will be registered as an **Eplan.EplApi.Scripting.Action** in the system. If a method, which is marked by the DeclareAction attribute has string parameters, these \parameters will be recognized as parameters of the Action.

Inheritance Hierarchy

[System.Object](#)  
   [System.Attribute](#)  
      **Eplan.EplApi.Scripting.DeclareAction**

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
[AttributeUsage(AttributeTargets.Method)]
public class DeclareAction : System.Attribute
```
```

```
```
[AttributeUsage(AttributeTargets.Method)]
public ref class DeclareAction : public System.Attribute
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DeclareAction Constructor](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Name](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction~Name.html) | Name of the action. |
| Public Property | [Ordinal](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction~Ordinal.html) | Overload level of the action. |
| Public Property | [TypeId](#) | (Inherited from [System.Attribute](#)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Equals](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [GetHashCode](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [IsDefaultAttribute](#) | (Inherited from [System.Attribute](#)) |
| Public Method | [Match](#) | (Inherited from [System.Attribute](#)) |

[Top](#top)




See Also

#### Reference

[DeclareAction Members](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction_members.html)
  
[Eplan.EplApi.Scripting Namespace](Eplan.EplApi.AFu~Eplan.EplApi.Scripting_namespace.html)
  
**Eplan.EplApi.Scripting.Action**