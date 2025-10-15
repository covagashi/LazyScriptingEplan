# Signin Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~Signin.html

---

Signs in to Eplan Cloud.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
Task<AuthenticationData> Signin()
```
```

```
```
Task<AuthenticationData^>^ Signin();
```
```

#### Return Value

AuthenticationData: operation result.

Remarks

If not already signed in, a login window will pop out.
