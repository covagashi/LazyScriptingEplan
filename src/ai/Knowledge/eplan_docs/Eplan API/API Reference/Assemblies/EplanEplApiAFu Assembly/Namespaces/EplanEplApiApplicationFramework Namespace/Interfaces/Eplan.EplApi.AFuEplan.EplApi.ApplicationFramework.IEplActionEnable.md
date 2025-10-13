Interface to enable or disable an Action. If this interface is not used, the Action is enabled by default. If you implement this interface in an action class, you can set the respective Action to disabled. If a ribbon item points to this Action, they will be also disabled (grayed out).

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public interface IEplActionEnable
```
```

```
```
public interface class IEplActionEnable
```
```

Example

* [c#](#i-tab-content-bd403255-ce68-4ae3-a18a-dc3010b1981e)

```
public class TestAction : Eplan.EplApi.ApplicationFramework.IEplAction, Eplan.EplApi.ApplicationFramework.IEplActionEnable
    {
        //IEplAction Members

        #region IEplActionEnable Members

        public bool Enabled(string strActionName, Eplan.EplApi.ApplicationFramework.ActionCallingContext actionContext)
        {
            if (strActionName == "TESTACTION")
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        #endregion
    }
```





Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Enabled](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionEnable~Enabled.html) | One action can be enabled or disabled. Return true when it is enabled. |

[Top](#top)




See Also

#### Reference

[IEplActionEnable Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionEnable_members.html)
  
[Eplan.EplApi.ApplicationFramework Namespace](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html)