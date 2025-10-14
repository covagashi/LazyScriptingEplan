The  PCTLoop  class represents the PCT loops in a project. They are logical units to measure or control.

 ``` 
 SegmentDefinition oSegmentDefinition = m_oTestProject.GetSegmentDefinition("Eplan.PCT.Loop");
 PCTLoop oPCTLoop  = PCTLoop.Create(oSegmentDefinition) as PCTLoop;
 ``` 

