Sets a label in the system error message management for getting a section of the 'message tree'

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public int GetBookmarkID()
```
```

```
```
public:
int GetBookmarkID();
```
```

#### Return Value

a serial number. save this value for later use

Example

get all messages which have been declared since the given bookmark was set

* [C#](#i-tab-content-265c92fc-9b7b-48e1-b238-a4f0cea55105)

```
int nBookmark = new Eplan.EplApi.Base.BaseException().GetBookmarkID(); //Starting point which sets the new bookmark
...
BaseException oBaseException = new BaseException("Exception message", MessageLevel.Error);
oBaseException.FixMessage(); //This error will be saved under nBookmark

SysMessagesCollection colSysMsg = new SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);
SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();
```

See Also

#### Reference

[BaseException Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)
  
[BaseException Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException_members.html)