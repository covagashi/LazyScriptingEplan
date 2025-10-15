# ObjectsFilter Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.FunctionVerification~ObjectsFilter.html

---

Collection of objects types which will be used to determine objects passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method.

Syntax

**C#**
**C++/CLI**


public override IEnumerable<Type> ObjectsFilter {get;}

public:

property IEnumerable<Type^>^ ObjectsFilter {

   IEnumerable<Type^>^ get() override;

}


Remarks

This property is used only when check is done for hole project.

This property is only a tip for framework. Set of objects passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method is a sum of types passed by all verifications executed in current check.

Objects of all types inherit from types passed by this property are also checked by verification.
