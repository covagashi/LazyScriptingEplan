When a script function is to respond to events in the system, the function has to be marked with this attribute.

Inheritance Hierarchy

[System.Object](#)  
   [System.Attribute](#)  
      **Eplan.EplApi.Scripting.DeclareEventHandler**

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
[AttributeUsage(AttributeTargets.Method)]
public class DeclareEventHandler : System.Attribute
```
```

```
```
[AttributeUsage(AttributeTargets.Method)]
public ref class DeclareEventHandler : public System.Attribute
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DeclareEventHandler Constructor](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareEventHandler~_ctor.html) | This function of the script is registered as an event handler in the system. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Name](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareEventHandler~Name.html) |  |
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

[DeclareEventHandler Members](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareEventHandler_members.html)
  
[Eplan.EplApi.Scripting Namespace](Eplan.EplApi.AFu~Eplan.EplApi.Scripting_namespace.html)
  
**Script\_EventHandling.html**