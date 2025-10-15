# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Properties.html

---

.NET Property enabling access to P8 properties of the TerminalStrip object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new TerminalStripPropertyListComplete Properties {get;}
```
```

```
```
public:

new property TerminalStripPropertyListComplete^ Properties {

   TerminalStripPropertyListComplete^ get();

}
```
```

#### Property Value

P8 properties of the TerminalStrip.

Example

- [C#](#i-tab-content-1ecc720a-0a17-419c-a9a7-78fe386be654)

```
TerminalStrip ts;//a valid TerminalStrip

ts.Properties[Properties.TerminalStrip.DESIGNATION_PLANT] = "AP";

int cnt = ts.Properties[Properties.TerminalStrip.TERMINALSTRIP_COUNTOFTERMINALS];
```
