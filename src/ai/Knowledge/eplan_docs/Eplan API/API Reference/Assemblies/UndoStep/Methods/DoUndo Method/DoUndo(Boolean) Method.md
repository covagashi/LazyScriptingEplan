# DoUndo(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~DoUndo(Boolean).html

---

Make Undo action - reverse all operations up to last CloseOpenUndo call or initalization of UndoStep object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void DoUndo( 

   bool bNoRedo

)
```
```

```
```
public:

void DoUndo( 

   bool bNoRedo

)
```
```

#### Parameters

*bNoRedo*
:   If false Redo action is not possible after call this method.
