The  StructureSegment  class represents structure segment objects. They are used to represent a part of the project structure.

 ``` 
 SegmentDefinition oSegmentDefinition = m_oTestProject.GetSegmentDefinition("Eplan.Base.StructureNode");
 StructureSegment oStructureSegment = StructureSegment.Create(m_oTestProject.SegmentDefinitions[0]) as StructureSegment;
 oStructureSegment.Name = "test1b";
 ``` 

