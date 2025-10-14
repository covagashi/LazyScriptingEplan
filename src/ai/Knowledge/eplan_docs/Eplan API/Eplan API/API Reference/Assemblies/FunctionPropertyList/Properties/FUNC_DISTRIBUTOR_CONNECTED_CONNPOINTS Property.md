# FUNC_DISTRIBUTOR_CONNECTED_CONNPOINTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_DISTRIBUTOR_CONNECTED_CONNPOINTS().html

---

Continuous connection between the connection points # 20331.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_DISTRIBUTOR_CONNECTED_CONNPOINTS {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_DISTRIBUTOR_CONNECTED_CONNPOINTS {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies at a connection splicer the connection points between which a continuous connection can run. Possible values are:

0 = None

1 = 1;2

2 = 1;3

3 = 1;4

4 = 2;3

5 = 2;4

6 = 3;4

7 = 1;2 / 3;4

8 = 1;3 / 2;4

9 = 1;4 / 2;3



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_DISTRIBUTOR_CONNECTED_CONNPOINTS.html)