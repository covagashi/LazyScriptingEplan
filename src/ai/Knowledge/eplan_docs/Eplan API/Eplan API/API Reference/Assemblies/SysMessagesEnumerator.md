# SysMessagesEnumerator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator.html

---

supports a simple iteration over [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html)

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.SysMessagesEnumerator**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class SysMessagesEnumerator
```
```

```
```
public ref class SysMessagesEnumerator
```
```

Example

iterate over the complete system message tree get all errors and fatal errors of the system message tree since nBookmark was set; how to get a bookmark see [BaseException.GetBookmarkID](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetBookmarkID.html)

- [C#](#i-tab-content-6c519ef1-d296-46b6-a7f5-b1bdf160b10a)

```
SysMessagesCollection colSysMsg = new SysMessagesCollection();
SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();
int nNr=0;

itSysMsg.MoveNext(); // move to first item in collection

do 
{
BaseException osysMsg = itSysMsg.Current as BaseException;
if (osysMsg != null)
{
	nNr++;
}					

} while(itSysMsg.MoveNext());
```

- [C#](#i-tab-content-1ade2920-9be9-409c-a147-9c7470ef0127)

```
SysMessagesCollection colSysMsg = new SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);
SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();
int nNr=0;

itSysMsg.MoveNext(); // move to first item in collection

do 
{
BaseException osysMsg = itSysMsg.Current as BaseException;
if (osysMsg != null)
{
	nNr++;
}					

} while(itSysMsg.MoveNext());
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SysMessagesEnumerator Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Current](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~Current.html) | gets the current element in [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~Dispose().html) |  |
| Public Method | [GetCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~GetCount.html) |  |
| Public Method | [MoveNext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~MoveNext.html) | Advances the enumerator to the next element of [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |
| Public Method | [Reset](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~Reset.html) | Sets the enumerator to its initial position, which is before the first element in [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |

[Top](#top)




See Also

#### Reference

[SysMessagesEnumerator Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator_members.html)
  
[Eplan.EplApi.Base Namespace](Eplan.EplApi.Baseu~Eplan.EplApi.Base_namespace.html)