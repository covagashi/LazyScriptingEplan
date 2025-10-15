# SetProxy Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~SetProxy.html

---

Sets custom proxy connection configuration.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
IdentityClientResponse SetProxy( 

   EProxySettings proxySettings

)
```
```

```
```
IdentityClientResponse^ SetProxy( 

   EProxySettings^ proxySettings

)
```
```

#### Parameters

*proxySettings*
:   Proxy settings object.

#### Return Value

IdentityClientResponse: operation result.

Remarks

If not used, the system proxy settings are used by default.
