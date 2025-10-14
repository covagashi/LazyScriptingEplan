# LockingExceptionFailedLockAttempt

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt.html

---

Throw when StorableObject cannot be locked. It differs from LockingException as it has information about all objects which could not be locked (retrieved from Locking Manager) and is thrown only after failed lock attempt.

Inheritance Hierarchy

[System.Object](#)  
   [System.Exception](#)  
      [System.ApplicationException](#)  
         [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)  
            [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html)  
               **Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class LockingExceptionFailedLockAttempt : Eplan.EplApi.Base.LockingException
```
```

```
```
public ref class LockingExceptionFailedLockAttempt : public Eplan.EplApi.Base.LockingException
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [LockingExceptionFailedLockAttempt Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt~_ctor.html) | Internal constructor with description. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Data](#) | (Inherited from [System.Exception](#)) |
| Public Property | [HelpLink](#) | (Inherited from [System.Exception](#)) |
| Public Property | [HResult](#) | (Inherited from [System.Exception](#)) |
| Public Property | [InnerException](#) | (Inherited from [System.Exception](#)) |
| Public Property | [Message](#) | (Inherited from [System.Exception](#)) |
| Public Property | [MessageLevel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~MessageLevel.html) | Returns the level of message as [Eplan.EplApi.Base.MessageLevel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MessageLevel.html). (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Property | [NumberOfOccurrences](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~NumberOfOccurrences.html) | Returns number of repetitions of consecutive messages with the same text (i.e. error description) which are joined into one item in the system's message tree. (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Property | [Source](#) | (Inherited from [System.Exception](#)) |
| Public Property | [StackTrace](#) | (Inherited from [System.Exception](#)) |
| Public Property | [TargetSite](#) | (Inherited from [System.Exception](#)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~Dispose().html) | Destructor for deterministic finalization of BaseException object. (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [FixMessage](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~FixMessage.html) | Method enters a message in the system-wide message tree. (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetAllFailed2LockAsString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt~GetAllFailed2LockAsString.html) | Overridden. returns all object ids of the objects which were not locked. In case this exception was produced while accessing unlocked object in write mode, only one object will be returned (the one which was accessed first). |
| Public Method | [GetBaseException](#) | (Inherited from [System.Exception](#)) |
| Public Method | [GetBookmarkID](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetBookmarkID.html) | Sets a label in the system error message management for getting a section of the 'message tree' (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetFirstFailed2LockAsString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException~GetFirstFailed2LockAsString.html) | returns the object id of the first object which was not locked. . (Inherited from [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html)) |
| Public Method | [GetMessageIndex](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetMessageIndex.html) | returns the identifying S- number of a system message (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetMessageText](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetMessageText.html) | Returns the text of the system message without the index (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetObjectData](#) | (Inherited from [System.Exception](#)) |
| Public Method | [GetType](#) | (Inherited from [System.Exception](#)) |
| Public Method | [ToString](#) | (Inherited from [System.Exception](#)) |

[Top](#top)




See Also

#### Reference

[LockingExceptionFailedLockAttempt Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)