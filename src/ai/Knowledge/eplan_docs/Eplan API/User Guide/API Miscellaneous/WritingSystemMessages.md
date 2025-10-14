Eplan expects system errors to be handled by exceptions. For this resason, the interface to the Eplan system messages is implemented in the  BaseException  class. This means that in order to write a system message, a  BaseException  object must first be created. However, the exception does not have to be thrown!

The  fixMessage()  function of the exception adds the message to the Eplan system messages.

* [C#](#i-tab-content-CS)


```

Eplan.EplApi.Base.BaseException exc = new Eplan.EplApi.Base.BaseException("CSharpAction really failed!!",
                                      Eplan.EplApi.Base.MessageLevel.Error);
exc.FixMessage();
```

