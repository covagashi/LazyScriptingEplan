# Create(MultiLangString,Matrix3D) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.HandleMate~Create(MultiLangString,Matrix3D).html

---

Creates a handle point with all mounting points permitted.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Create( 
   MultiLangString pMLSDescription,
   Matrix3D oPosition
)
```
```

```
```
public:
void Create( 
   MultiLangString^ pMLSDescription,
   Matrix3D oPosition
)
```
```

#### Parameters

*pMLSDescription*
:   Description of a handle

*oPosition*
:   Position represented by transformation matrix.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when a handle has already been created. |

Remarks

Notice that if user define handle is created, its position can be different then the one pass in argument. This is because mate of this type is projected on placement area if it exists. If placement area does not exist then z coordinate is set to 0.

Example

- [C#](#i-tab-content-2a8daba7-8a36-493e-ae8d-72dc1837c4f7)
- [C#](#i-tab-content-3c1103cf-247f-4b87-a21d-0e6d75f3fb2a)

```

var handle = new HandleMate();
handle.Create(new MultiLangString(), new Matrix3D());
oFunction3D.AddMatePersistent(handle);

//create a handle relative to placement area
var transformationToPlacementArea = new Matrix3D();
transformationToPlacementArea.Translate(new Vector3D(50.0, 500.0, 0.0));
var transformation = transformationToPlacementArea * oFunction3D.PlacementArea.RelativeTransformation;

var handle2 = new HandleMate();
handle2.Create(new MultiLangString(), transformation);
oFunction3D.AddMatePersistent(handle2);


```

```

//create a handle with extended logic 
var handleWithExtendedLogic = new HandleMate();
handleWithExtendedLogic.Create(new[] { "V1", "V2" }, new MultiLangString(), new Matrix3D());
oFunction3D.AddMatePersistent(handleWithExtendedLogic);


```

See Also

#### Reference

[HandleMate Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.HandleMate.html)
  
[HandleMate Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.HandleMate_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.HandleMate~Create.html)