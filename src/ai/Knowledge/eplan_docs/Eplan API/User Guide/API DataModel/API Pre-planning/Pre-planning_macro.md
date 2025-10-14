For a Pre-planning module, the new  PrePlanningMacro  class has been created to represent macros.

These macros are created as follows:

 ``` 
 string strMacroPath = m_oDir.FullName + "\\TestMacro.emv";
 PrePlanningMacro oPrePlanningMacro = new PrePlanningMacro();
 oPrePlanningMacro.Create(new[] {oPlanningSegment1, oPlanningSegment2}, strMacroPath, oMultiLangString);
 ``` 

                   

Inserting macros requires parameters such as the parent planning segment, the path to macro and the project object:

``` 
 string strMacroPath = m_oDir.FullName + "\\TestMacro.emv";
 StorableObject[] arrInsertedPlaObjects = new Insert().PrePlanningMacro(strMacroPath, m_oTestProject, oPlanningSegment1);
 ``` 