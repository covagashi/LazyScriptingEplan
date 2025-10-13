Interface to switch the status on / off of an Action. If this interface is not used, the Action is off by default. If you implement this interface in an action class, you can set the state of the respective Action to on. If 0, unchecks; if 1, checks; and if 2, sets indeterminate.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public interface IEplActionChecked
```
```

```
```
public interface class IEplActionChecked
```
```

Example

* [c#](#i-tab-content-ed49404c-e294-4baf-ba8d-b541a7dca7a0)

```
public class TestAction : Eplan.EplApi.ApplicationFramework.IEplAction, Eplan.EplApi.ApplicationFramework.IEplActionChecked
    {
        //IEplAction Members

        \#region IEplActionChecked Members

        public int Checked(string strActionName, Eplan.EplApi.ApplicationFramework.ActionCallingContext actionContext)
        {
            if (strActionName == "TESTACTIONMIXED")
            {
                return 2;
            } 
			else if (strActionName == "TESTACTION")
            {
                return 1;
            }
            else 
            {
                return 0;
            }

        }

        \#endregion
    }
```





Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Checked](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionChecked~Checked.html) | One action can have the state on off or mixed. Return 0 for off, 1 for on, and 2 for mixed. |

[Top](#top)




See Also

#### Reference

[IEplActionChecked Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionChecked_members.html)
  
[Eplan.EplApi.ApplicationFramework Namespace](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html)