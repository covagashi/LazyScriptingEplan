# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug~Create.html

---

Creates a Plug object related to a [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) given as a parameter. The created plug will get its symbol and function definition from the [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) parameter.

Overload List

| Overload | Description |
| --- | --- |
| [Create(PlugStrip,SymbolVariant)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug~Create(PlugStrip,SymbolVariant).html) | Creates a Plug object related to a [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) given as a parameter. The created plug will get its symbol and function definition from the [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) parameter. |
| [Create(PlugStrip,Page)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug~Create(PlugStrip,Page).html) | Creates a Plug object related to a [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) given as a parameter. The plug's function definition will be chosen based on the plug strip's function definition: - for "Male and female" plug strips, the plug will get "Male and Female pin" function definition,  - for "Male" plug strips, the plug will get "Male pin, 2 connection points" function definition,  - for "Female" plug strips, the plug will get "Female pin, 2 connection points" function definition |
| [Create(PlugStrip)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug~Create(PlugStrip).html) | Creates a Plug object related to a [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) given as a parameter. The plug's function definition will be chosen based on the plug strip's function definition: - for "Male and female" plug strips, the plug will get "Male and Female pin" function definition,  - for "Male" plug strips, the plug will get "Male pin, 2 connection points" function definition,  - for "Female" plug strips, the plug will get "Female pin, 2 connection points" function definition |
| [Create(Page,SymbolVariant,PointD,PointD)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Page,SymbolVariant,PointD,PointD).html) | Creates a `Function` object placed on a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) given as a parameter and sets it [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) together with `LogicalArea`. (Inherited from [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)) |
| [Create(Page,FunctionDefinition)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Page,FunctionDefinition).html) | Creates a Function object placed on a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) given as the first parameter and having a [Eplan.EplApi.DataModel.Function.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) taken from [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) passed as the second parameter. (Inherited from [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)) |
| [Create(Project,FunctionDefinition)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Project,FunctionDefinition).html) | Creates a Function. It is not placed on any [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). and having a [Eplan.EplApi.DataModel.Function.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) taken from [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) passed as the second parameter. (Inherited from [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)) |
| [Create(Page,SymbolVariant)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Page,SymbolVariant).html) | Creates a SymbolReference. It is placed on the page passed as a parameter, using a given SymbolVariant. (Inherited from [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)) |
| [Create(Project,SymbolVariant)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(Project,SymbolVariant).html) | Creates a Function. It is not placed on any [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). Its category is taken from [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html). (Inherited from [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)) |



See Also

#### Reference

[Plug Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)
  
[Plug Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug_members.html)