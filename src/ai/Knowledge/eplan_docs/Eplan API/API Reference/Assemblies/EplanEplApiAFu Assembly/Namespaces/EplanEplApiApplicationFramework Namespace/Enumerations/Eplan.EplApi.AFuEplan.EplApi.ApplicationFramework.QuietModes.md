Quiet modes

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public enum QuietModes : System.Enum
```
```

```
```
public enum class QuietModes : public System.Enum
```
```

Members

| Member | Value | Description |
| --- | --- | --- |
| **ShowAllDialogs** | 0 |  |
| **ShowNoDialogs** | 1 |  |
| **ShowSomeDialogs** | 2 |  |
| **Undefined** | -1 |  |

Remarks

ShowAllDialogs : all dialogs will be shown ShowNoDialogs : no dialogs will be shown ShowSomeDialogs : only some special dialogs will be shown, e.g.progress bars

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.ApplicationFramework.QuietModes**
