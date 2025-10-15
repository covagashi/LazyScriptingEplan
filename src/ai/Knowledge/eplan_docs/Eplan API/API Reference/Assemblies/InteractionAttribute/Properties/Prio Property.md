# Prio Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionAttribute~Prio.html

---

Priority of interaction.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int Prio {get; set;}
```
```

```
```
public:

property int Prio {

   int get();

   void set (    int value);

}
```
```

Remarks

If interaction is started while another interaction is running then the one with the lower priority will be deactivated until all interactions with higher priority will be finished.
