# FixMessage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~FixMessage.html

---

Method enters a message in the system-wide message tree.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void FixMessage()
```
```

```
```
public:

void FixMessage();
```
```

Example

Writing an error message to the system error message management.

- [C#](#i-tab-content-efdc958c-94f2-4a48-ad96-fc72ceefd17b)

```
Eplan.EplApi.Base.BaseException exc= new Eplan.EplApi.Base.BaseException("Error message from API module",

                                                                          Eplan.EplApi.Base.MessageLevel.Error);

exc.FixMessage();
```
