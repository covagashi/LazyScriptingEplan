Constructor

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public BaseException( 
   string strErrorText,
   MessageLevel eErrorLevel,
   BaseException innerException
)
```
```

```
```
public:
BaseException( 
   String^ strErrorText,
   MessageLevel eErrorLevel,
   BaseException^ innerException
)
```
```

#### Parameters

*strErrorText*
:   Note on the exception that occurred.

*eErrorLevel*
:   Severity of the exception that occurred.

*innerException*
:   The exception that is the cause of the current exception, or a null reference (Nothing in Visual Basic) if no inner exception is specified.
