Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetStringSetting( 
   string strSettingPath,
   string strvalue,
   int nIdx
)
```
```

```
```
public:
void SetStringSetting( 
   String^ strSettingPath,
   String^ strvalue,
   int nIdx
)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to scheme, path starts after scheme name).

*strvalue*
:   Indicates the value of the setting.

*nIdx*
:   Indicates the index.


