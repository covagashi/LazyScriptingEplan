# InterpretAutomatically(Placement3D,Placement3D[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1396.html

---

Starts automatic interpretation.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void InterpretAutomatically( 

   Placement3D oTarget,

   Placement3D[] arrSourcesToSearchForBestMach,

   bool bShowBestMachDlg

)
```
```

```
```
public:

void InterpretAutomatically( 

   Placement3D^ oTarget,

   array<Placement3D^>^ arrSourcesToSearchForBestMach,

   bool bShowBestMachDlg

)
```
```

#### Parameters

*oTarget*
:   3D placement for which automatic interpretation willl be started. Cannot be `null`.

*arrSourcesToSearchForBestMach*
:   Array of Placement3D objects from which the best mathing one will be searched for.

*bShowBestMachDlg*
:   Show best match dialog if true. In other case method selects best match automatically.

Example

Following example shows how to use the method:

- [C#](#i-tab-content-c2e2f1b9-dbbf-4690-9fb0-f14b3355c4fe)

```
new Placement3DService().InterpretAutomatically(oInstallationSpaceTarget.Children[0], oInstallationSpaceSource.Children, false);



```
