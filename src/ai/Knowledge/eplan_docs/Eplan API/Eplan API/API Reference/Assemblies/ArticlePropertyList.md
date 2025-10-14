# ArticlePropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html

---

This class represents collection of properties of [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html) class. Please check also base classes for other properties which are available for [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.ArticlePropertyList**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
[DefaultMember("Property")]
public class ArticlePropertyList : StorableObjectPropertyList
```
```

```
```
[DefaultMember("Property")]
public ref class ArticlePropertyList : public StorableObjectPropertyList
```
```

Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

- [C#](#i-tab-content-3480a280-fbb0-47d0-b749-54f9056c0058)

```
// creation of persistent property list
FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;
oPersistentPropertyList1.FUNC_COMMENT = "Comment";
// now oFunction.Properties.FUNC_COMMENT is equal "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);
oPersistentPropertyList2.FUNC_COMMENT = "Test";
// now oFunction.Properties.FUNC_COMMENT is equal "Test"

// creation of transient property list
FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();
oTransientPropertyList.FUNC_COMMENT = "Test comment";
oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;
oTransientPropertyList.FUNC_COMMENT = "Transient comment";
// now oTransientPropertyList.FUNC_COMMENT is equal "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ArticlePropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ARTICLE\_ABSORPTION\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ABSORPTION_VOLUME().html) | Reception volume # 26223. |
| Public Property | [ARTICLE\_ACCESSORYID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACCESSORYID().html) | Accessory code # 22025. |
| Public Property | [ARTICLE\_ACCURACY\_FOR\_DYNAMIC\_VISCOSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACCURACY_FOR_DYNAMIC_VISCOSITY().html) | Dynamic viscosity: Accuracy # 26362. |
| Public Property | [ARTICLE\_ACCURACY\_FOR\_OPERATING\_VOLUME\_FLOW\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACCURACY_FOR_OPERATING_VOLUME_FLOW_RATE().html) | Actual volume flow: Accuracy # 26360. |
| Public Property | [ARTICLE\_ACTIVE\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTIVE_POWER().html) | Active power # 26641. |
| Public Property | [ARTICLE\_ACTIVE\_POWER\_LOSS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTIVE_POWER_LOSS().html) | Active power loss # 26621. |
| Public Property | [ARTICLE\_ACTIVE\_POWER\_MAX\_ASV](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTIVE_POWER_MAX_ASV().html) | Active power (general power supply), max. # 26643. |
| Public Property | [ARTICLE\_ACTIVE\_POWER\_MAX\_NEA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTIVE_POWER_MAX_NEA().html) | Active power (emergency power system), max. # 26645. |
| Public Property | [ARTICLE\_ACTIVE\_POWER\_MAX\_UPS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTIVE_POWER_MAX_UPS().html) | Active power (uninterruptible power supply), max. # 26647. |
| Public Property | [ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_OUTPUT_HYDRAULIC().html) | Actual power (hydraulic) # 26381. |
| Public Property | [ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MAX().html) | Actual power (hydraulic), max. # 26383. |
| Public Property | [ARTICLE\_ACTUAL\_OUTPUT\_HYDRAULIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MIN().html) | Actual power (hydraulic), min. # 26385. |
| Public Property | [ARTICLE\_ACTUAL\_OUTPUT\_PNEUMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_OUTPUT_PNEUMATIC().html) | Actual power (pneumatic) # 26387. |
| Public Property | [ARTICLE\_ACTUAL\_OUTPUT\_PNEUMATIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX().html) | Actual power (pneumatic), max. # 26389. |
| Public Property | [ARTICLE\_ACTUAL\_POWER\_PNEUMATIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN().html) | Actual power (pneumatic), min. # 26391. |
| Public Property | [ARTICLE\_ACTUAL\_TOTAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_TOTAL_VOLUME_FLOW().html) | Actual total flow rate # 26111. |
| Public Property | [ARTICLE\_ACTUAL\_TOTAL\_VOLUME\_FLOW\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_TOTAL_VOLUME_FLOW_MAX().html) | Actual total flow rate, max. # 26112. |
| Public Property | [ARTICLE\_ACTUAL\_TOTAL\_VOLUME\_FLOW\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACTUAL_TOTAL_VOLUME_FLOW_MIN().html) | Actual total flow rate, min. # 26113. |
| Public Property | [ARTICLE\_ADDRESSRANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADDRESSRANGE().html) | Address range (SIEMENS STEP 7 Classic) # 22106. |
| Public Property | [ARTICLE\_ADDRESSRANGE\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADDRESSRANGE_2().html) | Address range 2 (SIEMENS STEP 7 Classic) # 22261. |
| Public Property | [ARTICLE\_ADJUSTRANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADJUSTRANGE().html) | Control range # 22125. |
| Public Property | [ARTICLE\_ADJUSTRANGE\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADJUSTRANGE_FULL().html) | Control range (full) # 22231. |
| Public Property | [ARTICLE\_ADVANCECONTACTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADVANCECONTACTS().html) | Plugs: Leading pins # 22102. |
| Public Property | [ARTICLE\_AIRGAP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_AIRGAP().html) | Plugs: Clearance # 22096. |
| Public Property | [ARTICLE\_APPARENT\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_APPARENT_POWER().html) | Apparent power # 26549. |
| Public Property | [ARTICLE\_APPLICATION\_AREA\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_APPLICATION_AREA_OF_THE_CABLE().html) | Operating area: Cable # 26287. |
| Public Property | [ARTICLE\_APPLICATION\_RANGE\_OF\_THE\_CONNECTION\_CABLE](topic9.html) | Connecting cable: Application area # 26208. |
| Public Property | [ARTICLE\_ASSEMBLY\_POS\_PLACE\_SPREADED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ASSEMBLY_POS_PLACE_SPREADED().html) | Distributed placement of assembly # 22040. |
| Public Property | [ARTICLE\_ATTRIBUTE\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ATTRIBUTE_VALUE(Int32).html) | Attributes # 22051. |
| Public Property | [ARTICLE\_AWGFROM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_AWGFROM().html) | Terminals: AWG from # 22086. |
| Public Property | [ARTICLE\_AWGTILL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_AWGTILL().html) | Terminals: AWG to # 22087. |
| Public Property | [ARTICLE\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BACNET().html) | BACnet # 26227. |
| Public Property | [ARTICLE\_BARCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BARCOUNT().html) | Busbars: Number of rails # 22201. |
| Public Property | [ARTICLE\_BARDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BARDISTANCE().html) | Busbars: Rail spacing # 22202. |
| Public Property | [ARTICLE\_BARGEOMETRY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BARGEOMETRY().html) | Busbars: Profile geometry D x H (only Eplan Cabinet) # 22200. |
| Public Property | [ARTICLE\_BARMOUNTINGPLATEDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BARMOUNTINGPLATEDISTANCE().html) | Busbars: Distance between rails and mounting panel # 22203. |
| Public Property | [ARTICLE\_BENDINGRADIUS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BENDINGRADIUS().html) | Min. bending radius # 22063. |
| Public Property | [ARTICLE\_BENDINGRADIUS\_COPPER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BENDINGRADIUS_COPPER().html) | Bending radius # 22257. |
| Public Property | [ARTICLE\_BLOWER\_PRESENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BLOWER_PRESENT().html) | Blower available # 26352. |
| Public Property | [ARTICLE\_BOTTOMPANELDEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BOTTOMPANELDEPTH().html) | Base: Depth # 22186. |
| Public Property | [ARTICLE\_BOTTOMPANELDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BOTTOMPANELDISTANCE().html) | Distance base # 22185. |
| Public Property | [ARTICLE\_BOTTOMPANELPROJECTIONBACK](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BOTTOMPANELPROJECTIONBACK().html) | Overhang: Base back # 22184. |
| Public Property | [ARTICLE\_BOTTOMPANELPROJECTIONFRONT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BOTTOMPANELPROJECTIONFRONT().html) | Overhang: Base front # 22183. |
| Public Property | [ARTICLE\_BOTTOMPANELPROJECTIONLEFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BOTTOMPANELPROJECTIONLEFT().html) | Overhang: Base left # 22181. |
| Public Property | [ARTICLE\_BOTTOMPANELPROJECTIONRIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BOTTOMPANELPROJECTIONRIGHT().html) | Overhang: Base right # 22182. |
| Public Property | [ARTICLE\_BUNDLE\_MAXDIAMETER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUNDLE_MAXDIAMETER().html) | Maximum bundle diameter # 22259. |
| Public Property | [ARTICLE\_BUNDLE\_MINDIAMETER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUNDLE_MINDIAMETER().html) | Minimum bundle diameter # 22260. |
| Public Property | [ARTICLE\_BUS\_SYSTEM\_KNX\_COMPATIBLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUS_SYSTEM_KNX_COMPATIBLE().html) | KNX: Compatible # 26031. |
| Public Property | [ARTICLE\_BUS\_SYSTEM\_KNX\_RADIO\_COMPATIBLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUS_SYSTEM_KNX_RADIO_COMPATIBLE().html) | KNX: KNX-RF compatible # 26032. |
| Public Property | [ARTICLE\_BUSBARHOLDERPARTNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUSBARHOLDERPARTNR().html) | Busbar support: Part number # 22204. |
| Public Property | [ARTICLE\_BUSBARHOLDERVARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUSBARHOLDERVARIANT().html) | Busbar support: Part variant # 22205. |
| Public Property | [ARTICLE\_BUSBARRAILPARTNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUSBARRAILPARTNR().html) | Busbars: Part number # 22252. |
| Public Property | [ARTICLE\_BUSBARRAILVARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_BUSBARRAILVARIANT().html) | Busbars: Part variant # 22253. |
| Public Property | [ARTICLE\_CABLE\_DATA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_DATA().html) | Cable data # 26046. |
| Public Property | [ARTICLE\_CABLE\_DIAMETER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_DIAMETER().html) | Cable diameter # 26116. |
| Public Property | [ARTICLE\_CABLE\_ENTRY\_AVAILABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_ENTRY_AVAILABLE().html) | Cable entry available # 26047. |
| Public Property | [ARTICLE\_CABLE\_ENTRY\_INTO\_THE\_DEVICE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE().html) | Cable entry into device # 26395. |
| Public Property | [ARTICLE\_CABLE\_INCLUDED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_INCLUDED().html) | Cables included # 26044. |
| Public Property | [ARTICLE\_CABLE\_LENGTH\_LAID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_LENGTH_LAID().html) | Cable length, routed # 26397. |
| Public Property | [ARTICLE\_CABLE\_LENGTH\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_LENGTH_MAX().html) | Cable length, max. # 26117. |
| Public Property | [ARTICLE\_CABLE\_LEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_LEVEL().html) | Cable: Voltage level # 26400. |
| Public Property | [ARTICLE\_CABLE\_OUTER\_DIAMETER\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_OUTER_DIAMETER_MIN().html) | Cable outer diameter, min. # 26115. |
| Public Property | [ARTICLE\_CABLE\_PIPE\_TRANSMITTER\_CONNECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_PIPE_TRANSMITTER_CONNECTION().html) | Measuring transducer: Line connection (cable / pipe) # 26202. |
| Public Property | [ARTICLE\_CABLE\_WINDER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_WINDER().html) | Cable reel # 26393. |
| Public Property | [ARTICLE\_CABLE\_WINDER\_AVAILABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLE_WINDER_AVAILABLE().html) | Cable reel available # 26045. |
| Public Property | [ARTICLE\_CABLEDESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEDESIGNATION().html) | Cable / Conduit: Designation in graphic # 22064. |
| Public Property | [ARTICLE\_CABLEDISPLAYFORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEDISPLAYFORM().html) | Cable assignment diagram form # 22034. |
| Public Property | [ARTICLE\_CABLELENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLELENGTH().html) | Length (prefabricated) # 22055. |
| Public Property | [ARTICLE\_CABLETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLETYPE().html) | Cable type / Type designation # 22030. |
| Public Property | [ARTICLE\_CABLEWEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEWEIGHT().html) | Weight / length # 22067. |
| Public Property | [ARTICLE\_CABLEWIRECOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEWIRECOUNT().html) | Number of connections # 22031. |
| Public Property | [ARTICLE\_CABLEWIRECROSSSECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEWIRECROSSSECTION().html) | Connection: Cross-section / diameter # 22032. |
| Public Property | [ARTICLE\_CALIBRATION\_AUTHORISATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CALIBRATION_AUTHORISATION().html) | Calibration approval # 26034. |
| Public Property | [ARTICLE\_CAN\_BE\_LINED\_UP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CAN_BE_LINED_UP().html) | Alignable # 22229. |
| Public Property | [ARTICLE\_CAPACITIVE\_LOAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CAPACITIVE_LOAD().html) | Capacitive load # 26402. |
| Public Property | [ARTICLE\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CAPACITY().html) | Volume capacity # 26322. |
| Public Property | [ARTICLE\_CERTIFICATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CERTIFICATE().html) | Certification: General # 22048. |
| Public Property | [ARTICLE\_CERTIFICATE\_ATEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CERTIFICATE_ATEX().html) | Certification: ATEX identifier # 22270. |
| Public Property | [ARTICLE\_CERTIFICATE\_CE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CERTIFICATE_CE().html) | Certification: CE # 22113. |
| Public Property | [ARTICLE\_CERTIFICATE\_UL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CERTIFICATE_UL().html) | Certification: UL File Number # 22049. |
| Public Property | [ARTICLE\_CERTIFICATE\_UL\_CNN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CERTIFICATE_UL_CNN().html) | Certification: UL Category Control Number # 22368. |
| Public Property | [ARTICLE\_CERTIFICATE\_VDE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CERTIFICATE_VDE().html) | Certification: VDE # 22050. |
| Public Property | [ARTICLE\_CHARACTER\_SET\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic10.html) | BACnet: Character set acc. to BACnet specification # 26651. |
| Public Property | [ARTICLE\_CHARACTERISTIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CHARACTERISTIC().html) | Characteristic curve # 26403. |
| Public Property | [ARTICLE\_CHARACTERISTICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CHARACTERISTICS().html) | Technical characteristics # 22017. |
| Public Property | [ARTICLE\_CIRCUIT\_BREAKER\_TEST\_AVAILABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE().html) | Power circuit breaker - test available # 26433. |
| Public Property | [ARTICLE\_CLAMP\_COLOUR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CLAMP_COLOUR().html) | Terminal: Color # 26039. |
| Public Property | [ARTICLE\_CLIMATE\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CLIMATE_CLASS().html) | Climate class # 26407. |
| Public Property | [ARTICLE\_CLOSING\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CLOSING_PRESSURE().html) | Closing pressure # 26551. |
| Public Property | [ARTICLE\_CO2\_EMISSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CO2_EMISSION().html) | CO2 emission # 26245. |
| Public Property | [ARTICLE\_CODING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CODING().html) | Plugs: Coding # 22103. |
| Public Property | [ARTICLE\_COILVOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COILVOLTAGE().html) | Coil: Voltage # 22218. |
| Public Property | [ARTICLE\_COLLECTION\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COLLECTION_VOLUME().html) | Retention volume # 26221. |
| Public Property | [ARTICLE\_COLOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COLOR().html) | Color # 22080. |
| Public Property | [ARTICLE\_COLOUR\_OF\_THE\_CABLE\_SHEATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COLOUR_OF_THE_CABLE_SHEATH().html) | Cable jacket: Color # 26040. |
| Public Property | [ARTICLE\_CONDUCTIVITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONDUCTIVITY().html) | Conductivity (at +20 Â°C) # 22273. |
| Public Property | [ARTICLE\_CONDUCTOR\_CROSS\_SECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONDUCTOR_CROSS_SECTION().html) | Conductor cross-section # 26120. |
| Public Property | [ARTICLE\_CONDUCTOR\_STRUCTURE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONDUCTOR_STRUCTURE_CABLE().html) | Conductor design (cable) # 26049. |
| Public Property | [ARTICLE\_CONNECTABLE\_CABLE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTABLE_CABLE_TYPE().html) | Connectable cable type # 26182. |
| Public Property | [ARTICLE\_CONNECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTION().html) | Connection point # 22130. |
| Public Property | [ARTICLE\_CONNECTION\_CABLE\_COLOUR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTION_CABLE_COLOUR().html) | Connecting cable: Color # 26007. |
| Public Property | [ARTICLE\_CONNECTION\_CABLE\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTION_CABLE_LENGTH().html) | Connecting cable: Length # 26206. |
| Public Property | [ARTICLE\_CONNECTION\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTION_TYPE().html) | Connection point type # 26204. |
| Public Property | [ARTICLE\_CONNECTION\_WIRECROSSSECTION\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTION_WIRECROSSSECTION_UNIT().html) | Connection: Unit for connection cross-section / diameter # 22255. |
| Public Property | [ARTICLE\_CONNECTIONCROSSSECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTIONCROSSSECTION().html) | Connection point cross-section # 22036. |
| Public Property | [ARTICLE\_CONNECTIONMETHOD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTIONMETHOD().html) | Plugs: Connecting technique # 22101. |
| Public Property | [ARTICLE\_CONNECTOR\_DESIGN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTOR_DESIGN().html) | Plug-in connector design # 26063. |
| Public Property | [ARTICLE\_CONNECTOR\_HOUSING\_OF\_CONNECTION\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTOR_HOUSING_OF_CONNECTION_1().html) | Plug-in connector housing (connection 1) # 26579. |
| Public Property | [ARTICLE\_CONNECTOR\_HOUSING\_OF\_THE\_CONNECTION\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTOR_HOUSING_OF_THE_CONNECTION_2().html) | Plug-in connector housing (connection 2) # 26581. |
| Public Property | [ARTICLE\_CONTACT\_POTENTIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTACT_POTENTIAL().html) | Contact potential # 26119. |
| Public Property | [ARTICLE\_CONTACTOR\_ARRANGEMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTACTOR_ARRANGEMENT().html) | Plugs: Pin arrangement # 22095. |
| Public Property | [ARTICLE\_CONTACTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTACTTYPE().html) | Plugs: Pin type # 22099. |
| Public Property | [ARTICLE\_CONTAINS\_ADDONPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTAINS_ADDONPARTS().html) | Contains supplemental parts # 22423. |
| Public Property | [ARTICLE\_CONTAINS\_ASSEMBLIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTAINS_ASSEMBLIES().html) | Contains assemblies # 22425. |
| Public Property | [ARTICLE\_CONTAINS\_MODULES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTAINS_MODULES().html) | Contains modules # 22424. |
| Public Property | [ARTICLE\_CONTINUOUS\_HEAT\_PERFORMANCE\_AT\_10\_C](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTINUOUS_HEAT_PERFORMANCE_AT_10_C().html) | Continuous heating power (at 10Â°C) # 26093. |
| Public Property | [ARTICLE\_CONTINUOUS\_HEAT\_PERFORMANCE\_AT\_20\_C](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTINUOUS_HEAT_PERFORMANCE_AT_20_C().html) | Continuous heating power (at 20Â°C) # 26094. |
| Public Property | [ARTICLE\_CONTROL\_FLOW\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTROL_FLOW_RATE().html) | Control flow rate # 26152. |
| Public Property | [ARTICLE\_CONTROL\_PRESSURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTROL_PRESSURE_MAX().html) | Pilot pressure, max. # 26150. |
| Public Property | [ARTICLE\_CONTROL\_PRESSURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTROL_PRESSURE_MIN().html) | Pilot pressure, min. # 26151. |
| Public Property | [ARTICLE\_CONTROL\_SIGNAL\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONTROL_SIGNAL_TYPE().html) | Control signal: Type # 26583. |
| Public Property | [ARTICLE\_COOLING\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COOLING_TYPE().html) | Type of cooling # 26016. |
| Public Property | [ARTICLE\_COPPERNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_COPPERNUMBER().html) | Copper weight # 22066. |
| Public Property | [ARTICLE\_CPMS\_GUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CPMS_GUID().html) | Unique external part ID # 22984. |
| Public Property | [ARTICLE\_CRAFT\_COOLING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_COOLING().html) | Trade 'Cooling' # 22137. |
| Public Property | [ARTICLE\_CRAFT\_COOLINGLUBRICANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_COOLINGLUBRICANT().html) | Trade 'Cooling lubricant' # 22262. |
| Public Property | [ARTICLE\_CRAFT\_ELECTRICAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_ELECTRICAL().html) | Trade 'Electrical engineering' # 22131. |
| Public Property | [ARTICLE\_CRAFT\_FLUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_FLUID().html) | Trade 'Fluid power' # 22132. |
| Public Property | [ARTICLE\_CRAFT\_FLUID\_UNDEFINED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_FLUID_UNDEFINED().html) | Trade 'Fluid power (undefined)' # 22264. |
| Public Property | [ARTICLE\_CRAFT\_GASTECHNOLOGY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_GASTECHNOLOGY().html) | Trade 'Gas engineering' # 22263. |
| Public Property | [ARTICLE\_CRAFT\_HYDRAULICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_HYDRAULICS().html) | Trade 'Hydraulics' # 22134. |
| Public Property | [ARTICLE\_CRAFT\_LUBRICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_LUBRICATION().html) | Trade 'Lubrication' # 22136. |
| Public Property | [ARTICLE\_CRAFT\_MECHANICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_MECHANICS().html) | Trade 'Mechanics' # 22133. |
| Public Property | [ARTICLE\_CRAFT\_PNEUMATICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_PNEUMATICS().html) | Trade 'Pneumatics' # 22135. |
| Public Property | [ARTICLE\_CRAFT\_PROCESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CRAFT_PROCESS().html) | Trade 'Process engineering' # 22000. |
| Public Property | [ARTICLE\_CREEPAGEDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CREEPAGEDISTANCE().html) | Plugs: Creepage distance # 22097. |
| Public Property | [ARTICLE\_CROSS\_SECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CROSS_SECTION().html) | Cross-section # 26134. |
| Public Property | [ARTICLE\_CROSS\_SECTION\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CROSS_SECTION_MAX().html) | Cross-section, max. # 26137. |
| Public Property | [ARTICLE\_CROSS\_SECTION\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CROSS_SECTION_OF_THE_CABLE().html) | Cable: Cross-section # 26136. |
| Public Property | [ARTICLE\_CROSS\_SECTION\_OF\_THE\_CONNECTION\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CROSS_SECTION_OF_THE_CONNECTION_CABLE().html) | Connection cable: Cross-section # 26135. |
| Public Property | [ARTICLE\_CROSSSECTIONFROM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CROSSSECTIONFROM().html) | Terminals: Cross-section from # 22084. |
| Public Property | [ARTICLE\_CROSSSECTIONTILL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CROSSSECTIONTILL().html) | Terminals: Cross-section to # 22085. |
| Public Property | [ARTICLE\_CURRENT\_CARRYING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENT_CARRYING_CAPACITY().html) | Current carrying capacity # 26153. |
| Public Property | [ARTICLE\_CURRENT\_CARRYING\_CAPACITY\_MAX\_PER\_CONNECTION\_SOCKET](topic11.html) | Current carrying capacity (per connection socket), max. # 26154. |
| Public Property | [ARTICLE\_CURRENT\_CARRYING\_CAPACITY\_MAX\_PER\_I\_O\_SIGNAL](topic12.html) | Current carrying capacity (per I/O signal), max. # 26155. |
| Public Property | [ARTICLE\_CURRENT\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENT_CONSUMPTION().html) | Current consumption # 26595. |
| Public Property | [ARTICLE\_CURRENT\_CONSUMPTION\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENT_CONSUMPTION_MAX().html) | Current consumption, max. # 26597. |
| Public Property | [ARTICLE\_CURRENT\_LOAD\_RESISTIVE\_LOAD\_DC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX().html) | Current carrying capacity (resistive load, DC), max. # 26156. |
| Public Property | [ARTICLE\_CURRENTCSA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENTCSA().html) | Terminals: Current CSA # 22092. |
| Public Property | [ARTICLE\_CURRENTIEC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENTIEC().html) | Terminals: Current IEC # 22088. |
| Public Property | [ARTICLE\_CURRENTUL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENTUL().html) | Terminals: Current UL # 22090. |
| Public Property | [ARTICLE\_CUSTOM\_DATA\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CUSTOM_DATA_INDEX(Int32).html) | API Parts Management Extension: Name of add-in # 22212. |
| Public Property | [ARTICLE\_CUSTOM\_DATA\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CUSTOM_DATA_VALUE(Int32).html) | API Parts Management Extension: Value from add-in # 22213. |
| Public Property | [ARTICLE\_DEGOFPROTECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DEGOFPROTECTION().html) | Terminals: Degree of protection # 22082. |
| Public Property | [ARTICLE\_DELIVERYLENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DELIVERYLENGTH().html) | Delivery length # 22058. |
| Public Property | [ARTICLE\_DENSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DENSITY().html) | Density # 26095. |
| Public Property | [ARTICLE\_DEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DEPTH().html) | Depth # 22014. |
| Public Property | [ARTICLE\_DESCR1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESCR1().html) | Part: Designation 1 # 22004. |
| Public Property | [ARTICLE\_DESCR2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESCR2().html) | Part: Designation 2 # 22005. |
| Public Property | [ARTICLE\_DESCR3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESCR3().html) | Part: Designation 3 # 22006. |
| Public Property | [ARTICLE\_DESIGN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN().html) | Plugs: Type of construction # 22100. |
| Public Property | [ARTICLE\_DESIGN\_AS\_OUTDOOR\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_AS_OUTDOOR_CABLE().html) | Designed as outdoor cable # 26023. |
| Public Property | [ARTICLE\_DESIGN\_OF\_THE\_FIXING\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_OF_THE_FIXING_POINT().html) | Design of attachment point # 26226. |
| Public Property | [ARTICLE\_DESIGN\_OF\_THE\_HOUSING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_OF_THE_HOUSING().html) | Type of construction: Housing # 26027. |
| Public Property | [ARTICLE\_DESIGN\_OF\_THE\_SENSOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_OF_THE_SENSOR().html) | Type of construction: Sensor # 26029. |
| Public Property | [ARTICLE\_DESIGN\_OF\_THE\_TRANSDUCER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_OF_THE_TRANSDUCER().html) | Type of construction: Measuring transducer # 26028. |
| Public Property | [ARTICLE\_DESIGN\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_TEMPERATURE().html) | Design temperature # 26083. |
| Public Property | [ARTICLE\_DESIGNATION\_OF\_THE\_MEASURING\_METHOD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGNATION_OF_THE_MEASURING_METHOD().html) | Designation of the measurement method # 26030. |
| Public Property | [ARTICLE\_DEVICE\_PROFILE\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic13.html) | BACnet: Device profile according to BACnet specification # 26368. |
| Public Property | [ARTICLE\_DIAMETER\_OF\_THE\_CABLE\_ENTRY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DIAMETER_OF_THE_CABLE_ENTRY().html) | Diameter: Cable entry # 26097. |
| Public Property | [ARTICLE\_DIMENSIONS\_OF\_THE\_PRESSURED\_AREA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DIMENSIONS_OF_THE_PRESSURED_AREA().html) | Pressure area: Dimension # 26001. |
| Public Property | [ARTICLE\_DISASSEMBLE\_ADDONPARTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_ADDONPARTS().html) | Include supplemental parts (summarized parts list) # 22415. |
| Public Property | [ARTICLE\_DISASSEMBLE\_ADDONPARTS2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_ADDONPARTS2().html) | Include supplemental parts (parts list) # 22416. |
| Public Property | [ARTICLE\_DISASSEMBLE\_ADDONPARTS3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_ADDONPARTS3().html) | Include supplemental parts (summarized parts list / manufacturing data) # 22419. |
| Public Property | [ARTICLE\_DISASSEMBLE\_ADDONPARTS4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_ADDONPARTS4().html) | Include supplemental parts (parts list / manufacturing data) # 22420. |
| Public Property | [ARTICLE\_DISASSEMBLE\_MODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_MODE().html) | Break up in summarized parts list # 22292. |
| Public Property | [ARTICLE\_DISASSEMBLE\_SELECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_SELECTION().html) | Break up assembly during part selection # 22421. |
| Public Property | [ARTICLE\_DISASSEMBLE\_SELECTIONLEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_SELECTIONLEVEL().html) | Up to level # 22422. |
| Public Property | [ARTICLE\_DISASSEMBLE2\_MODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE2_MODE().html) | Break up in parts list # 22380. |
| Public Property | [ARTICLE\_DISASSEMBLE3\_MODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE3_MODE().html) | Break up in summarized parts list (manufacturing data) # 22417. |
| Public Property | [ARTICLE\_DISASSEMBLE4\_MODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE4_MODE().html) | Break up in parts list (manufacturing data) # 22418. |
| Public Property | [ARTICLE\_DISCONTINUED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISCONTINUED().html) | Discontinued part # 22258. |
| Public Property | [ARTICLE\_DISCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISCOUNT().html) | Discount # 22221. |
| Public Property | [ARTICLE\_DISTANCE\_WIRE\_HOLD\_BACK\_NOSE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISTANCE_WIRE_HOLD_BACK_NOSE().html) | Distance of the pinch point # 22287. |
| Public Property | [ARTICLE\_DOES\_NOT\_NEED\_3D\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOES_NOT_NEED_3D_MACRO().html) | Part does not require a 3D macro # 22392. |
| Public Property | [ARTICLE\_DOES\_NOT\_NEED\_CPP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOES_NOT_NEED_CPP().html) | Part does not require a connection point pattern # 22393. |
| Public Property | [ARTICLE\_DOES\_NOT\_NEED\_DRILL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOES_NOT_NEED_DRILL().html) | Part does not require a drilling pattern # 22394. |
| Public Property | [ARTICLE\_DOOR\_OFFSET\_RIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOOR_OFFSET_RIGHT().html) | Door opening: Offset right # 22162. |
| Public Property | [ARTICLE\_DOOR\_OFFSET\_TOP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOOR_OFFSET_TOP().html) | Door opening: Offset top # 22161. |
| Public Property | [ARTICLE\_DOOR\_RABBET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOOR_RABBET().html) | Door fold # 22160. |
| Public Property | [ARTICLE\_DOORDEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOORDEPTH().html) | Door: Max. mounting depth # 22121. |
| Public Property | [ARTICLE\_DOORHEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOORHEIGHT().html) | Door: Usable height # 22119. |
| Public Property | [ARTICLE\_DOORMOUNTINGSPACE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOORMOUNTINGSPACE().html) | Door: Mounting space # 22079. |
| Public Property | [ARTICLE\_DOORTHICKNESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOORTHICKNESS().html) | Door: Wall thickness # 22194. |
| Public Property | [ARTICLE\_DOORTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOORTYPE().html) | Door: Type # 22192. |
| Public Property | [ARTICLE\_DOORWIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOORWIDTH().html) | Door: Usable width # 22120. |
| Public Property | [ARTICLE\_DRIVE\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DRIVE_TORQUE().html) | Drive torque # 26008. |
| Public Property | [ARTICLE\_DUTY\_CYCLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DUTY_CYCLE().html) | Duty cycle # 26293. |
| Public Property | [ARTICLE\_ECABINET\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ECABINET_MACRO().html) | Texture # 22219. |
| Public Property | [ARTICLE\_EDP\_IMPORT\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EDP_IMPORT_DATE().html) | Data Portal import date # 22391. |
| Public Property | [ARTICLE\_EFFECTIVE\_DELIVERY\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EFFECTIVE_DELIVERY_RATE().html) | Effective delivery amount # 26271. |
| Public Property | [ARTICLE\_EFFICIENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EFFICIENCY().html) | Efficiency # 26649. |
| Public Property | [ARTICLE\_ELECTRICAL\_INTERFACE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ELECTRICAL_INTERFACE().html) | Electrical interface # 26036. |
| Public Property | [ARTICLE\_ELECTRICALCURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ELECTRICALCURRENT().html) | Current # 22071. |
| Public Property | [ARTICLE\_ELECTRICALPOWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ELECTRICALPOWER().html) | Switching capacity # 22072. |
| Public Property | [ARTICLE\_ELECTRONIC\_CONTROL\_AVAILABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ELECTRONIC_CONTROL_AVAILABLE().html) | Electronic control available # 26037. |
| Public Property | [ARTICLE\_EMC\_DESIGN\_PRESENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EMC_DESIGN_PRESENT().html) | EMC version available # 26298. |
| Public Property | [ARTICLE\_EMERGENCY\_CONTROL\_FUNCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EMERGENCY_CONTROL_FUNCTION().html) | Emergency control function # 26053. |
| Public Property | [ARTICLE\_EMERGENCY\_CONTROL\_FUNCTION\_CLOSED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EMERGENCY_CONTROL_FUNCTION_CLOSED().html) | Emergency control function (closed) # 26054. |
| Public Property | [ARTICLE\_EMERGENCY\_CONTROL\_FUNCTION\_OPEN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EMERGENCY_CONTROL_FUNCTION_OPEN().html) | Emergency control function (open) # 26055. |
| Public Property | [ARTICLE\_ENCLOSURE\_DESIGN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ENCLOSURE_DESIGN().html) | Type of construction # 26024. |
| Public Property | [ARTICLE\_END\_VALUE\_OF\_THE\_DYNAMIC\_VISCOSITY\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE().html) | Dynamic viscosity range: End value # 26299. |
| Public Property | [ARTICLE\_ENERGY\_EFFICIENCY\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ENERGY_EFFICIENCY_CLASS().html) | Energy efficiency class # 26301. |
| Public Property | [ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_CN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ENERGY_EFFICIENCY_CLASS_CN().html) | Energy efficiency class CN # 26305. |
| Public Property | [ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_MOTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ENERGY_EFFICIENCY_CLASS_MOTOR().html) | Energy efficiency class (motor) # 26303. |
| Public Property | [ARTICLE\_ENERGY\_EFFICIENCY\_CLASS\_US](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ENERGY_EFFICIENCY_CLASS_US().html) | Energy efficiency class US # 26307. |
| Public Property | [ARTICLE\_ERPNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR().html) | ERP / PDM number 1 # 22056. |
| Public Property | [ARTICLE\_ERPNR\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_10().html) | ERP / PDM number 10 # 22379. |
| Public Property | [ARTICLE\_ERPNR\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_2().html) | ERP / PDM number 2 # 22371. |
| Public Property | [ARTICLE\_ERPNR\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_3().html) | ERP / PDM number 3 # 22372. |
| Public Property | [ARTICLE\_ERPNR\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_4().html) | ERP / PDM number 4 # 22373. |
| Public Property | [ARTICLE\_ERPNR\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_5().html) | ERP / PDM number 5 # 22374. |
| Public Property | [ARTICLE\_ERPNR\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_6().html) | ERP / PDM number 6 # 22375. |
| Public Property | [ARTICLE\_ERPNR\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_7().html) | ERP / PDM number 7 # 22376. |
| Public Property | [ARTICLE\_ERPNR\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_8().html) | ERP / PDM number 8 # 22377. |
| Public Property | [ARTICLE\_ERPNR\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_9().html) | ERP / PDM number 9 # 22378. |
| Public Property | [ARTICLE\_ERPNR\_ALL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_ALL().html) | ERP / PDM numbers # 22370. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION().html) | ERP / PDM number 1: Description # 22381. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_10().html) | ERP / PDM number 10: Description # 22390. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_2().html) | ERP / PDM number 2: Description # 22382. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_3().html) | ERP / PDM number 3: Description # 22383. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_4().html) | ERP / PDM number 4: Description # 22384. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_5().html) | ERP / PDM number 5: Description # 22385. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_6().html) | ERP / PDM number 6: Description # 22386. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_7().html) | ERP / PDM number 7: Description # 22387. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_8().html) | ERP / PDM number 8: Description # 22388. |
| Public Property | [ARTICLE\_ERPNR\_DESCRIPTION\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ERPNR_DESCRIPTION_9().html) | ERP / PDM number 9: Description # 22389. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT(Int32).html) | External document # 22210. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_1().html) | External document 1 # 22149. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_10().html) | External document 10 # 22241. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_11().html) | External document 11 # 22242. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_12().html) | External document 12 # 22243. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_13](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_13().html) | External document 13 # 22244. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_14](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_14().html) | External document 14 # 22245. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_15](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_15().html) | External document 15 # 22246. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_16](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_16().html) | External document 16 # 22247. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_17](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_17().html) | External document 17 # 22248. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_18](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_18().html) | External document 18 # 22249. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_19](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_19().html) | External document 19 # 22250. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_2().html) | External document 2 # 22150. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_20](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_20().html) | External document 20 # 22251. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_3().html) | External document 3 # 22151. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_4().html) | External document 4 # 22235. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_5().html) | External document 5 # 22236. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_6().html) | External document 6 # 22237. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_7().html) | External document 7 # 22238. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_8().html) | External document 8 # 22239. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_9().html) | External document 9 # 22240. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_ALL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_ALL().html) | External documents # 22369. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_DESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION(Int32).html) | External document: Designation # 22279. |
| Public Property | [ARTICLE\_EXTERNAL\_DOCUMENT\_URL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_URL(Int32).html) | External document: File / hyperlink # 22280. |
| Public Property | [ARTICLE\_EXTERNAL\_PLACEMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_PLACEMENT().html) | External placement # 22220. |
| Public Property | [ARTICLE\_FAMILY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FAMILY().html) | Family # 22885. |
| Public Property | [ARTICLE\_FAN\_AIR\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FAN_AIR_FLOW().html) | Blower air flow # 26353. |
| Public Property | [ARTICLE\_FEEDBACK\_CONTACT\_PRESENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FEEDBACK_CONTACT_PRESENT().html) | Feedback contact available # 26061. |
| Public Property | [ARTICLE\_FILLING\_LEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FILLING_LEVEL().html) | Fill capacity # 26344. |
| Public Property | [ARTICLE\_FILLING\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FILLING_VOLUME().html) | Fill volume # 26346. |
| Public Property | [ARTICLE\_FILTER\_FINENESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FILTER_FINENESS().html) | Grade of filtration # 26586. |
| Public Property | [ARTICLE\_FIRE\_PROTECTION\_PROPERTIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FIRE_PROTECTION_PROPERTIES().html) | Fire protection properties # 26243. |
| Public Property | [ARTICLE\_FIRMWAREVERSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FIRMWAREVERSION().html) | Version # 22104. |
| Public Property | [ARTICLE\_FITTING\_LENGTH\_OF\_THE\_PROTECTION\_TUBE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FITTING_LENGTH_OF_THE_PROTECTION_TUBE().html) | Mounting length: Protective tube # 26277. |
| Public Property | [ARTICLE\_FLAME\_RESISTANCE\_ACCORDING\_TO\_STANDARD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLAME_RESISTANCE_ACCORDING_TO_STANDARD().html) | Flame resistance (according to standard) # 26042. |
| Public Property | [ARTICLE\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLOW().html) | Flow # 22126. |
| Public Property | [ARTICLE\_FLOW\_DIRECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLOW_DIRECTION().html) | Flow direction: Operating flow direction # 26267. |
| Public Property | [ARTICLE\_FLOW\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLOW_FULL().html) | Flow (full) # 22232. |
| Public Property | [ARTICLE\_FLOW\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLOW_RATE().html) | Flow rate # 26265. |
| Public Property | [ARTICLE\_FLOW\_RATE\_OPERATING\_NORMAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW().html) | Flow rate (operating / standard volume flow) # 26263. |
| Public Property | [ARTICLE\_FLUID\_WALLTHICKNESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FLUID_WALLTHICKNESS().html) | Fluid / process engineering Wall thickness of the connection # 22275. |
| Public Property | [ARTICLE\_FREE\_DATA\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_DESCRIPTION(Int32).html) | Free properties: Displayed name # 22146. |
| Public Property | [ARTICLE\_FREE\_DATA\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_FULL(Int32).html) | Free properties: Value and unit (full) # 22234. |
| Public Property | [ARTICLE\_FREE\_DATA\_IDENTNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_IDENTNAME(Int32).html) | User-defined properties: Identifying name # 22336. |
| Public Property | [ARTICLE\_FREE\_DATA\_NEWVALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_NEWVALUE(Int32).html) | User-defined properties: Value # 22337. |
| Public Property | [ARTICLE\_FREE\_DATA\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_UNIT(Int32).html) | Free properties: Unit # 22148. |
| Public Property | [ARTICLE\_FREE\_DATA\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREE_DATA_VALUE(Int32).html) | Free properties: Value # 22147. |
| Public Property | [ARTICLE\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREQUENCY().html) | Frequency # 26334. |
| Public Property | [ARTICLE\_FREQUENCY\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREQUENCY_RANGE().html) | Frequency range # 26342. |
| Public Property | [ARTICLE\_FREQUENCY\_RANGE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREQUENCY_RANGE_MAX().html) | Frequency range, max. # 26330. |
| Public Property | [ARTICLE\_FREQUENCY\_RANGE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREQUENCY_RANGE_MIN().html) | Frequency range, min. # 26332. |
| Public Property | [ARTICLE\_FREQUENCY\_SIGNAL\_PROCESSING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREQUENCY_SIGNAL_PROCESSING().html) | Frequency (signal processing) # 26336. |
| Public Property | [ARTICLE\_FREQUENCY\_SIGNAL\_PROCESSING\_SET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FREQUENCY_SIGNAL_PROCESSING_SET().html) | Frequency (signal processing), set # 26338. |
| Public Property | [ARTICLE\_FUNCTIONGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FUNCTIONGROUP().html) | Function group # 22026. |
| Public Property | [ARTICLE\_FUNKTION\_IN\_RUHESTELLUNG](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FUNKTION_IN_RUHESTELLUNG().html) | Function in rest position # 26348. |
| Public Property | [ARTICLE\_FUSE\_PROTECTION\_ON\_SITE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FUSE_PROTECTION_ON_SITE().html) | Amperage (fuse, on-site) # 26002. |
| Public Property | [ARTICLE\_GROUPNUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPNUMBER().html) | Group number # 22044. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO().html) | Schematic macro # 22145. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_CUSTOM\_ALL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_CUSTOM_ALL().html) | Schematic macros for company standard # 22882. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_CUSTOM\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_CUSTOM_MACRO(Int32).html) | Schematic macro: Macro for company standard # 22881. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_CUSTOM\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_CUSTOM_NAME(Int32).html) | Schematic macro: Name for company standard # 22880. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_GB\_CCC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_GB_CCC().html) | Schematic macro: GB/CCC # 22873. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_GOST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_GOST().html) | Schematic macro: GOST # 22874. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_IEC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_IEC().html) | Schematic macro: IEC # 22870. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_NFPA\_INCH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_NFPA_INCH().html) | Schematic macro: NFPA inch # 22872. |
| Public Property | [ARTICLE\_GROUPSYMBOLMACRO\_NFPA\_MM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_GROUPSYMBOLMACRO_NFPA_MM().html) | Schematic macro: NFPA mm # 22871. |
| Public Property | [ARTICLE\_HEAT\_OUTPUT\_SPECIFIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HEAT_OUTPUT_SPECIFIC().html) | Specific heat output # 26569. |
| Public Property | [ARTICLE\_HEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HEIGHT().html) | Height # 22012. |
| Public Property | [ARTICLE\_HINGEPOSITION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HINGEPOSITION().html) | Door: Hinge # 22193. |
| Public Property | [ARTICLE\_HOLDINGPOWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HOLDINGPOWER().html) | Holding power # 22073. |
| Public Property | [ARTICLE\_HOLE\_PATTERN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HOLE_PATTERN().html) | Hole pattern # 26437. |
| Public Property | [ARTICLE\_HYDRAULIC\_EFFICIENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HYDRAULIC_EFFICIENCY().html) | Hydraulic efficiency # 26380. |
| Public Property | [ARTICLE\_HYDRAULIC\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HYDRAULIC_POWER().html) | Hydraulic power # 26110. |
| Public Property | [ARTICLE\_IDENTCODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_IDENTCODE().html) | Barcode number # 22208. |
| Public Property | [ARTICLE\_IDENTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_IDENTTYPE().html) | Barcode type # 22209. |
| Public Property | [ARTICLE\_INITIAL\_VALUE\_OF\_THE\_DYNAMIC\_VISCOSITY\_RANGE](topic14.html) | Dynamic viscosity range: Start value # 26188. |
| Public Property | [ARTICLE\_INNERDIAMETER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INNERDIAMETER().html) | Inner diameter # 22128. |
| Public Property | [ARTICLE\_INPUT\_VOLTAGE\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INPUT_VOLTAGE_FREQUENCY().html) | Frequency (input voltage) # 26340. |
| Public Property | [ARTICLE\_INPUT\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INPUT_VOLUME_FLOW().html) | Input flow rate # 26279. |
| Public Property | [ARTICLE\_INRUSH\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INRUSH_CURRENT().html) | Inrush current # 26295. |
| Public Property | [ARTICLE\_INRUSH\_CURRENT\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INRUSH_CURRENT_MAX().html) | Inrush current, max. # 26098. |
| Public Property | [ARTICLE\_INRUSH\_CURRENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INRUSH_CURRENT_MIN().html) | Inrush current, min. # 26099. |
| Public Property | [ARTICLE\_INSERTPOINTOFFSETX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INSERTPOINTOFFSETX().html) | Busbar support: Vertical offset # 22207. |
| Public Property | [ARTICLE\_INSTALLATION\_DEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INSTALLATION_DEPTH().html) | Mounting depth # 22268. |
| Public Property | [ARTICLE\_INSTALLATION\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INSTALLATION_LENGTH().html) | Mounting length # 26275. |
| Public Property | [ARTICLE\_INSTALLATION\_POSITION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INSTALLATION_POSITION().html) | Mounting position # 26035. |
| Public Property | [ARTICLE\_INTAKE\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_CAPACITY().html) | Intake capacity # 26194. |
| Public Property | [ARTICLE\_INTAKE\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_PRESSURE().html) | Intake pressure # 26003. |
| Public Property | [ARTICLE\_INTAKE\_PRESSURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_PRESSURE_MAX().html) | Intake pressure, max. # 26004. |
| Public Property | [ARTICLE\_INTAKE\_PRESSURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_PRESSURE_MIN().html) | Intake pressure, min. # 26005. |
| Public Property | [ARTICLE\_INTAKE\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_TEMPERATURE().html) | Intake temperature # 26006. |
| Public Property | [ARTICLE\_INTAKE\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_VOLUME().html) | Intake volume # 26196. |
| Public Property | [ARTICLE\_INTAKE\_VOLUME\_FLOW\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTAKE_VOLUME_FLOW_MIN().html) | Intake flow rate, min. # 26200. |
| Public Property | [ARTICLE\_INTRINSICSAFETY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTRINSICSAFETY().html) | Intrinsically safe # 22114. |
| Public Property | [ARTICLE\_IS\_ACCESSORY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_IS_ACCESSORY().html) | Part is accessory # 22054. |
| Public Property | [ARTICLE\_LABELLING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LABELLING().html) | Identification # 26405. |
| Public Property | [ARTICLE\_LENGTH\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LENGTH_MAX().html) | Length, max. # 26413. |
| Public Property | [ARTICLE\_LENGTH\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LENGTH_MIN().html) | Length, min. # 26415. |
| Public Property | [ARTICLE\_LEVEL\_MEASURING\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LEVEL_MEASURING_RANGE().html) | Measuring range: Level # 26452. |
| Public Property | [ARTICLE\_LIFETIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LIFETIME().html) | Service time # 22142. |
| Public Property | [ARTICLE\_LOAD\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LOAD_CAPACITY().html) | Load capacity of the cable # 26085. |
| Public Property | [ARTICLE\_LOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LOCATION().html) | Operating location # 26291. |
| Public Property | [ARTICLE\_LV\_IDENTIFIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LV_IDENTIFIER().html) | Bill of quantities: Identifier # 26438. |
| Public Property | [ARTICLE\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MACRO().html) | Graphical macro # 22010. |
| Public Property | [ARTICLE\_MACRONAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MACRONAME().html) | Graphical macro (without macro directory name) # 22018. |
| Public Property | [ARTICLE\_MAINTENANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAINTENANCE().html) | Lubrication / maintenance # 22141. |
| Public Property | [ARTICLE\_MAINTENANCE\_CYCLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAINTENANCE_CYCLE().html) | Maintenance cycle # 26637. |
| Public Property | [ARTICLE\_MAINTENANCE\_INTERVAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAINTENANCE_INTERVAL().html) | Maintenance interval # 26635. |
| Public Property | [ARTICLE\_MAKING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAKING_CAPACITY().html) | Rated ultimate short-circuit making capacity (Icm) # 26589. |
| Public Property | [ARTICLE\_MANUAL\_CONTROLS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MANUAL_CONTROLS().html) | Manual control devices # 26050. |
| Public Property | [ARTICLE\_MANUFACTURER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MANUFACTURER().html) | Manufacturer # 22007. |
| Public Property | [ARTICLE\_MANUFACTURER\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MANUFACTURER_NAME().html) | Manufacturer name # 22222. |
| Public Property | [ARTICLE\_MASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MASS().html) | Mass # 26440. |
| Public Property | [ARTICLE\_MASS\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MASS_FLOW().html) | Mass flow # 26442. |
| Public Property | [ARTICLE\_MASS\_MOMENT\_OF\_INERTIA\_OF\_THE\_LOAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD().html) | Mass moment of inertia of the load # 26443. |
| Public Property | [ARTICLE\_MATERIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MATERIAL().html) | Material # 22081. |
| Public Property | [ARTICLE\_MATERIAL\_LIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MATERIAL_LIST().html) | Material selection list # 26656. |
| Public Property | [ARTICLE\_MATERIAL\_OF\_THE\_CABLE\_INNER\_CONDUCTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MATERIAL_OF_THE_CABLE_INNER_CONDUCTOR().html) | Material of the inner conductor # 26639. |
| Public Property | [ARTICLE\_MATERIAL\_OF\_THE\_CABLE\_SHEATH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MATERIAL_OF_THE_CABLE_SHEATH().html) | Material of the cable jacket # 26640. |
| Public Property | [ARTICLE\_MAX\_AMBIENT\_TEMPERATURE\_DURING\_OPERATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAX_AMBIENT_TEMPERATURE_DURING_OPERATION().html) | Ambient temperature (during operation), max. # 26157. |
| Public Property | [ARTICLE\_MAX\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAX_POWER_CONSUMPTION().html) | Power consumption, max. # 26419. |
| Public Property | [ARTICLE\_MAX\_RATED\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAX_RATED_CURRENT().html) | Nominal current, max. # 26500. |
| Public Property | [ARTICLE\_MAX\_RATED\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MAX_RATED_POWER().html) | Nominal power (in kW), max. # 26478. |
| Public Property | [ARTICLE\_MEASURED\_VARIABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURED_VARIABLE().html) | Measurand # 26460. |
| Public Property | [ARTICLE\_MEASURING\_ACCURACY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_ACCURACY().html) | Measurement accuracy # 26458. |
| Public Property | [ARTICLE\_MEASURING\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE().html) | Measuring range # 26181. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_LOWER\_LIMIT\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_LOWER_LIMIT_VALUE().html) | Measuring range: Lower limit # 26456. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_MAX\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_MAX_().html) | Measuring range, max. # 26453. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_MIN().html) | Measuring range, min. # 26454. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_DENSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_DENSITY().html) | Measuring range: Density # 26445. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_DYNAMIC\_VISCOSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_DYNAMIC_VISCOSITY().html) | Measuring range: Dynamic viscosity # 26446. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_HUMIDITY\_PERCENTRH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_HUMIDITY_PERCENTRH().html) | Measuring range: Humidity (in %r.H.) # 26447. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_PRESSURE().html) | Measuring range: Pressure # 26124. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_RATIO\_MEASUREMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_RATIO_MEASUREMENT().html) | Measuring range: Ratio measurement # 26450. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_STANDARD\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_STANDARD_VOLUME_FLOW().html) | Measuring range: Normalized volume flow # 26126. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_TEMPERATURE().html) | Measuring range: Temperature # 26121. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_CONCENTRATION\_MEASUREMENT](topic15.html) | Measuring range: Concentration measurement # 26448. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_MASS\_FLOW\_RATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_THE_MASS_FLOW_RATE().html) | Measuring range: Mass flow # 26451. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_OPERATING\_VOLUME\_FLOW\_RATE](topic16.html) | Measuring range: Actual volume flow # 26123. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_QUANTITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_THE_QUANTITY().html) | Measuring range: Quantity # 26449. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_SWITCHING\_DISTANCE](topic17.html) | Measuring range: Switching distance # 26127. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_VOLUME\_MEASUREMENT](topic18.html) | Measuring range: Volume measurement # 26122. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_OF\_THE\_WEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_OF_THE_WEIGHT().html) | Measuring range: Weight # 26125. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_SCALE\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_SCALE_LENGTH().html) | Measuring range / scale length # 26457. |
| Public Property | [ARTICLE\_MEASURING\_RANGE\_UPPER\_LIMIT\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MEASURING_RANGE_UPPER_LIMIT_VALUE().html) | Measuring range: Upper limit # 26455. |
| Public Property | [ARTICLE\_METHOD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_METHOD().html) | Method # 26051. |
| Public Property | [ARTICLE\_METHOD\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_METHOD_NAME().html) | Method name # 26052. |
| Public Property | [ARTICLE\_MIDDLEOFFSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MIDDLEOFFSET().html) | Center mismatch # 22215. |
| Public Property | [ARTICLE\_MIN\_AMBIENT\_TEMPERATURE\_DURING\_OPERATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MIN_AMBIENT_TEMPERATURE_DURING_OPERATION().html) | Ambient temperature (during operation), min. # 26158. |
| Public Property | [ARTICLE\_MODULE\_POS\_PLACE\_SPREADED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MODULE_POS_PLACE_SPREADED().html) | Distributed placement of module # 22288. |
| Public Property | [ARTICLE\_MOUNTING\_FORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MOUNTING_FORM().html) | Mounting configuration # 26273. |
| Public Property | [ARTICLE\_MOUNTINGSITE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MOUNTINGSITE().html) | Mounting surface # 22022. |
| Public Property | [ARTICLE\_MOUNTINGSPACE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MOUNTINGSPACE().html) | Space requirement # 22047. |
| Public Property | [ARTICLE\_NOMINAL\_CAPACITY\_PNEUMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_CAPACITY_PNEUMATIC().html) | Nominal power (pneumatic) # 26477. |
| Public Property | [ARTICLE\_NOMINAL\_COOLING\_PERFORMANCE\_L35W10\_200L\_H](topic19.html) | Nominal cooling capacity (L35W10 200 l/h) # 26130. |
| Public Property | [ARTICLE\_NOMINAL\_COOLING\_PERFORMANCE\_L35W10\_400L\_H](topic20.html) | Nominal cooling capacity (L35W10 400 l/h) # 26131. |
| Public Property | [ARTICLE\_NOMINAL\_CURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_CURRENT().html) | Nominal current # 26311. |
| Public Property | [ARTICLE\_NOMINAL\_MOTOR\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_MOTOR_POWER().html) | Motor nominal power # 26462. |
| Public Property | [ARTICLE\_NOMINAL\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_POWER_CONSUMPTION().html) | Nominal power consumption # 26482. |
| Public Property | [ARTICLE\_NOMINAL\_POWER\_HYDRAULIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_POWER_HYDRAULIC().html) | Nominal power (hydraulic) # 26476. |
| Public Property | [ARTICLE\_NOMINAL\_POWER\_REQUIREMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_POWER_REQUIREMENT().html) | Nominal power requirement # 26484. |
| Public Property | [ARTICLE\_NOMINAL\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_PRESSURE().html) | Nominal pressure # 26470. |
| Public Property | [ARTICLE\_NOMINAL\_PRESSURE\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_PRESSURE_RANGE().html) | Pressure range # 26472. |
| Public Property | [ARTICLE\_NOMINAL\_PRESSURE\_SERIES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_PRESSURE_SERIES().html) | Nominal pressure series # 26309. |
| Public Property | [ARTICLE\_NOMINAL\_SUCTION\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_SUCTION_PRESSURE().html) | Nominal intake pressure # 26128. |
| Public Property | [ARTICLE\_NOMINAL\_TOTAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_TOTAL_VOLUME_FLOW().html) | Nominal total flow rate # 26129. |
| Public Property | [ARTICLE\_NOMINAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_VOLUME_FLOW().html) | Nominal flow rate # 26506. |
| Public Property | [ARTICLE\_NOMINAL\_VOLUME\_FLOW\_OF\_THE\_SUCTION\_SIDE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE().html) | Nominal flow rate (intake side) # 26508. |
| Public Property | [ARTICLE\_NOMINAL\_VOLUMETRIC\_FLOW\_OF\_COMPRESSED\_AIR](topic21.html) | Nominal flow rate (compressed air) # 26510. |
| Public Property | [ARTICLE\_NOMINAL\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_WIDTH().html) | Nominal size / diameter # 26512. |
| Public Property | [ARTICLE\_NOMINAL\_WIDTH\_CONNECTION\_SIZE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE().html) | Nominal size / connection size # 26514. |
| Public Property | [ARTICLE\_NORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NORM().html) | Standard # 22227. |
| Public Property | [ARTICLE\_NOTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOTE().html) | Description # 22009. |
| Public Property | [ARTICLE\_NUMBER\_OF\_AUXILIARY\_POWER\_SPEC\_PNEUMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_AUXILIARY_POWER_SPEC_PNEUMATIC().html) | Number of auxiliary powers (specifically pneumatic) # 26069. |
| Public Property | [ARTICLE\_NUMBER\_OF\_BACNET\_I\_O\_OBJECTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS().html) | BACnet: Number of I/O objects # 26212. |
| Public Property | [ARTICLE\_NUMBER\_OF\_CONNECTABLE\_VALVES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_CONNECTABLE_VALVES().html) | Number of connectable valves # 26009. |
| Public Property | [ARTICLE\_NUMBER\_OF\_FIXING\_POINTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_FIXING_POINTS().html) | Number of attachment points # 26076. |
| Public Property | [ARTICLE\_NUMBER\_OF\_HW\_INTERFACES\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_HW_INTERFACES_BACNET().html) | BACnet: Number of hardware interfaces # 26214. |
| Public Property | [ARTICLE\_NUMBER\_OF\_INPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_INPUTS().html) | Number of inputs # 26216. |
| Public Property | [ARTICLE\_NUMBER\_OF\_IPCF\_CAPABLE\_WIRELESS\_MODULES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_IPCF_CAPABLE_WIRELESS_MODULES().html) | Number of iPCF compatible wireless modules # 26077. |
| Public Property | [ARTICLE\_NUMBER\_OF\_OUTPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_OUTPUTS().html) | Number of outputs # 26011. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PCF\_METHODS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_PCF_METHODS().html) | PCF: Number of calculation methods # 26078. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PNEUMATIC\_CONNECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTION().html) | Number of pneumatic ports # 26070. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PNEUMATIC\_CONNECTIONS\_CONTROL\_CONNECTION](topic22.html) | Number of pneumatic ports (control ports) # 26074. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PNEUMATIC\_CONNECTIONS\_EXHAUST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_EXHAUST().html) | Number of pneumatic ports (exhaust) # 26073. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PNEUMATIC\_CONNECTIONS\_INPUT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_INPUT().html) | Number of pneumatic ports (inputs) # 26072. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PNEUMATIC\_CONNECTIONS\_OUTPUT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_OUTPUT().html) | Number of pneumatic ports (outputs) # 26071. |
| Public Property | [ARTICLE\_NUMBER\_OF\_PROCESS\_CONNECTIONS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_PROCESS_CONNECTIONS().html) | Number of process connections points # 26068. |
| Public Property | [ARTICLE\_NUMBER\_OF\_TCF\_METHODS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_TCF_METHODS().html) | TCF: Number of calculation methods # 26079. |
| Public Property | [ARTICLE\_NUMBER\_OF\_TYPES\_OF\_FIXING\_POINTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NUMBER_OF_TYPES_OF_FIXING_POINTS().html) | Number of attachment point types # 26075. |
| Public Property | [ARTICLE\_OHMIC\_RESISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OHMIC_RESISTANCE().html) | Ohmic resistance # 26132. |
| Public Property | [ARTICLE\_OPENING\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPENING_PRESSURE().html) | Opening pressure # 26522. |
| Public Property | [ARTICLE\_OPERATING\_TEMPERATURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_TEMPERATURE().html) | Operating temperature # 26237. |
| Public Property | [ARTICLE\_OPERATING\_TEMPERATURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_TEMPERATURE_MAX().html) | Operating temperature, max. # 26239. |
| Public Property | [ARTICLE\_OPERATING\_TEMPERATURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_TEMPERATURE_MIN().html) | Operating temperature, min. # 26241. |
| Public Property | [ARTICLE\_OPERATING\_VOLTAGE\_WITH\_AC\_50\_HZ\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MAX().html) | Operating voltage (AC 50 Hz), max. # 26087. |
| Public Property | [ARTICLE\_OPERATING\_VOLTAGE\_WITH\_AC\_50\_HZ\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MIN().html) | Operating voltage (AC 50 Hz), min. # 26088. |
| Public Property | [ARTICLE\_OPERATING\_VOLTAGE\_WITH\_AC\_60\_HZ\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MAX().html) | Operating voltage (AC 60 Hz), max. # 26089. |
| Public Property | [ARTICLE\_OPERATING\_VOLTAGE\_WITH\_AC\_60\_HZ\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MIN().html) | Operating voltage (AC 60 Hz), min. # 26090. |
| Public Property | [ARTICLE\_OPERATING\_VOLTAGE\_WITH\_DC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX().html) | Operating voltage (DC), max. # 26091. |
| Public Property | [ARTICLE\_OPERATING\_VOLTAGE\_WITH\_DC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OPERATING_VOLTAGE_WITH_DC_MIN().html) | Operating voltage (DC), min. # 26092. |
| Public Property | [ARTICLE\_ORDERNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ORDERNR().html) | Order number # 22003. |
| Public Property | [ARTICLE\_OUTER\_CABLE\_DIAMETER\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OUTER_CABLE_DIAMETER_MAX().html) | Cable outer diameter, max. # 26114. |
| Public Property | [ARTICLE\_OUTER\_DIAMETER\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OUTER_DIAMETER_OF_THE_CABLE().html) | Cable outer diameter # 26084. |
| Public Property | [ARTICLE\_OUTERDIAMETER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OUTERDIAMETER().html) | Outside diameter # 22065. |
| Public Property | [ARTICLE\_OUTPUT\_SPEED\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OUTPUT_SPEED_MAX().html) | Output speed, max. # 26183. |
| Public Property | [ARTICLE\_OUTPUT\_SPEED\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OUTPUT_SPEED_MIN().html) | Output speed, min. # 26185. |
| Public Property | [ARTICLE\_OVERLOAD\_CAPACITY\_OVERCURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT().html) | Overload capability: Overcurrent # 26619. |
| Public Property | [ARTICLE\_PACKAGINGPRICE\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PACKAGINGPRICE_1().html) | Purchase price/packaging Currency 1 # 22111. |
| Public Property | [ARTICLE\_PACKAGINGPRICE\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PACKAGINGPRICE_2().html) | Purchase price/packaging Currency 2 # 22112. |
| Public Property | [ARTICLE\_PACKAGINGQUANTITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PACKAGINGQUANTITY().html) | Quantity/packaging # 22122. |
| Public Property | [ARTICLE\_PANELDEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PANELDEPTH().html) | Mounting panel: Max. mounting depth # 22118. |
| Public Property | [ARTICLE\_PANELHEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PANELHEIGHT().html) | Mounting panel: Usable height # 22116. |
| Public Property | [ARTICLE\_PANELMOUNTINGSPACE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PANELMOUNTINGSPACE().html) | Mounting panel: Mounting space # 22078. |
| Public Property | [ARTICLE\_PANELWIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PANELWIDTH().html) | Mounting panel: Usable width # 22117. |
| Public Property | [ARTICLE\_PARTIAL\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PARTIAL_LENGTH().html) | Subset / length # 20496. |
| Public Property | [ARTICLE\_PARTNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PARTNR().html) | Part number # 22001. |
| Public Property | [ARTICLE\_PARTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PARTTYPE().html) | Record type # 22023. |
| Public Property | [ARTICLE\_PCF\_CALCULATION\_METHOD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_CALCULATION_METHOD().html) | PCF: Calculation method # 26524. |
| Public Property | [ARTICLE\_PCF\_CO2EQ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_CO2EQ().html) | PCF: CO2-eq # 26526. |
| Public Property | [ARTICLE\_PCF\_GOODS\_TRANSFER\_ADDRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_GOODS_TRANSFER_ADDRESS().html) | PCF: Address for delivery of goods # 26530. |
| Public Property | [ARTICLE\_PCF\_LIFE\_CYCLE\_PHASE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_LIFE_CYCLE_PHASE().html) | PCF: Life cycle phase # 26527. |
| Public Property | [ARTICLE\_PCF\_PRODUCT\_CARBON\_FOOTPRINT\_CALCULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_PRODUCT_CARBON_FOOTPRINT_CALCULATION().html) | PCF: Calculation # 26529. |
| Public Property | [ARTICLE\_PCF\_QUANTITY\_FOR\_CALCULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_QUANTITY_FOR_CALCULATION().html) | PCF: Quantity for the calculation # 26528. |
| Public Property | [ARTICLE\_PCF\_REFERENCE\_VALUE\_FOR\_THE\_CALCULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PCF_REFERENCE_VALUE_FOR_THE_CALCULATION().html) | PCF: Reference value for the calculation # 26525. |
| Public Property | [ARTICLE\_PE\_WIRE\_COUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PE_WIRE_COUNT().html) | Number of PE conductors # 22123. |
| Public Property | [ARTICLE\_PERFORMANCE\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PERFORMANCE_DESCRIPTION().html) | Performance description, standardized: Description (device, utility, service) # 26425. |
| Public Property | [ARTICLE\_PERMISSIBLE\_BENDING\_RADIUS\_FLEXIBLE\_USE\_FREE\_MOVEMENT\_MIN](topic23.html) | Permitted bending radius (moving application / free movement), min. # 26654. |
| Public Property | [ARTICLE\_PERMISSIBLE\_BENDING\_RADIUS\_FLEXIBLE\_USE\_WITH\_FORCED\_GUIDANCE\_MIN](topic24.html) | Permitted bending radius (moving application with forced guidance), min. # 26653. |
| Public Property | [ARTICLE\_PERMISSIBLE\_BENDING\_RADIUS\_STATIONARY\_USE\_FIXED\_INSTALLATION\_MIN](topic25.html) | Permitted bending radius (stationary application / permanent installation), min. # 26655. |
| Public Property | [ARTICLE\_PERMISSIBLE\_EXTERNAL\_CABLE\_TEMPERATURE\_FIXED\_INSTALLATION\_MAX](topic26.html) | Permissible cable outer temperature (fixed installation), max. # 26177. |
| Public Property | [ARTICLE\_PERMISSIBLE\_EXTERNAL\_CABLE\_TEMPERATURE\_IN\_MOTION\_MAX](topic27.html) | Permissible cable outer temperature (when moving), max. # 26178. |
| Public Property | [ARTICLE\_PERMISSIBLE\_SURFACE\_TEMPERATURE\_WITH\_FIXED\_CONDUCTOR\_MAX](topic28.html) | Permissible surface temperature (with stationary lines), max. # 26180. |
| Public Property | [ARTICLE\_PERMISSIBLE\_SURFACE\_TEMPERATURE\_WITH\_MOVING\_CONDUCTOR\_MAX](topic29.html) | Permissible surface temperature (with open - not stationary - lines), max. # 26179. |
| Public Property | [ARTICLE\_PICTUREFILE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PICTUREFILE().html) | Image file # 22045. |
| Public Property | [ARTICLE\_PIECETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PIECETYPE().html) | Part group # 22027. |
| Public Property | [ARTICLE\_PINCOUNT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PINCOUNT().html) | Plugs: Number of pins # 22035. |
| Public Property | [ARTICLE\_PIPECLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PIPECLASS().html) | Pipe class # 22224. |
| Public Property | [ARTICLE\_PLCAXIS\_DEVICETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCAXIS_DEVICETYPE().html) | Drive: Device type # 22340. |
| Public Property | [ARTICLE\_PLCDEVICE\_ID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICE_ID().html) | Device description: File name # 22037. |
| Public Property | [ARTICLE\_PLCDEVICE\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICE_INDEX().html) | Device description: Index in file # 22283. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_1().html) | PLC subdevice 1: Name # 22293. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_10().html) | PLC subdevice 10: Name # 22302. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_11().html) | PLC subdevice 11: Name # 22303. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_12().html) | PLC subdevice 12: Name # 22304. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_2().html) | PLC subdevice 2: Name # 22294. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_3().html) | PLC subdevice 3: Name # 22295. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_4().html) | PLC subdevice 4: Name # 22296. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_5().html) | PLC subdevice 5: Name # 22297. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_6().html) | PLC subdevice 6: Name # 22298. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_7().html) | PLC subdevice 7: Name # 22299. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_8().html) | PLC subdevice 8: Name # 22300. |
| Public Property | [ARTICLE\_PLCDEVICENAME\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENAME_9().html) | PLC subdevice 9: Name # 22301. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_1().html) | PLC subdevice 1: Position (slot / module) # 22305. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_10().html) | PLC subdevice 10: Position (slot / module) # 22314. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_11().html) | PLC subdevice 11: Position (slot / module) # 22315. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_12().html) | PLC subdevice 12: Position (slot / module) # 22316. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_2().html) | PLC subdevice 2: Position (slot / module) # 22306. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_3().html) | PLC subdevice 3: Position (slot / module) # 22307. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_4().html) | PLC subdevice 4: Position (slot / module) # 22308. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_5().html) | PLC subdevice 5: Position (slot / module) # 22309. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_6().html) | PLC subdevice 6: Position (slot / module) # 22310. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_7().html) | PLC subdevice 7: Position (slot / module) # 22311. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_8().html) | PLC subdevice 8: Position (slot / module) # 22312. |
| Public Property | [ARTICLE\_PLCDEVICENUMBER\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICENUMBER_9().html) | PLC subdevice 9: Position (slot / module) # 22313. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS().html) | PLC device: Data length (inputs) # 20571. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_1().html) | PLC subdevice 1: Data length (inputs) # 22363. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_10().html) | PLC subdevice 10: Data length (inputs) # 22323. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_11().html) | PLC subdevice 11: Data length (inputs) # 22324. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_12().html) | PLC subdevice 12: Data length (inputs) # 22325. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_2().html) | PLC subdevice 2: Data length (inputs) # 20572. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_3().html) | PLC subdevice 3: Data length (inputs) # 22291. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_4().html) | PLC subdevice 4: Data length (inputs) # 22317. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_5().html) | PLC subdevice 5: Data length (inputs) # 22318. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_6().html) | PLC subdevice 6: Data length (inputs) # 22319. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_7().html) | PLC subdevice 7: Data length (inputs) # 22320. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_8().html) | PLC subdevice 8: Data length (inputs) # 22321. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_INPUTS\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS_9().html) | PLC subdevice 9: Data length (inputs) # 22322. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS().html) | PLC device: Data length (outputs) # 20573. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_1().html) | PLC subdevice 1: Data length (outputs) # 22364. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_10().html) | PLC subdevice 10: Data length (outputs) # 22333. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_11().html) | PLC subdevice 11: Data length (outputs) # 22334. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_12().html) | PLC subdevice 12: Data length (outputs) # 22335. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_2().html) | PLC subdevice 2: Data length (outputs) # 20574. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_3().html) | PLC subdevice 3: Data length (outputs) # 22326. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_4().html) | PLC subdevice 4: Data length (outputs) # 22327. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_5().html) | PLC subdevice 5: Data length (outputs) # 22328. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_6().html) | PLC subdevice 6: Data length (outputs) # 22329. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_7().html) | PLC subdevice 7: Data length (outputs) # 22330. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_8().html) | PLC subdevice 8: Data length (outputs) # 22331. |
| Public Property | [ARTICLE\_PLCGROUP\_DATALENGTH\_OUTPUTS\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_9().html) | PLC subdevice 9: Data length (outputs) # 22332. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_1().html) | PLC subdevice 1: Device description: Index in file # 22366. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_10().html) | PLC subdevice 10: Device description: Index in file # 22360. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_11().html) | PLC subdevice 11: Device description: Index in file # 22361. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_12().html) | PLC subdevice 12: Device description: Index in file # 22362. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_2().html) | PLC subdevice 2: Device description: Index in file # 22352. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_3().html) | PLC subdevice 3: Device description: Index in file # 22353. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_4().html) | PLC subdevice 4: Device description: Index in file # 22354. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_5().html) | PLC subdevice 5: Device description: Index in file # 22355. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_6().html) | PLC subdevice 6: Device description: Index in file # 22356. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_7().html) | PLC subdevice 7: Device description: Index in file # 22357. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_8().html) | PLC subdevice 8: Device description: Index in file # 22358. |
| Public Property | [ARTICLE\_PLCGROUP\_INDEXINFILE\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_9().html) | PLC subdevice 9: Device description: Index in file # 22359. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_1().html) | PLC subdevice 1: PLC type designation # 22365. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_10](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_10().html) | PLC subdevice 10: PLC type designation # 22349. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_11](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_11().html) | PLC subdevice 11: PLC type designation # 22350. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_12](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_12().html) | PLC subdevice 12: PLC type designation # 22351. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_2().html) | PLC subdevice 2: PLC type designation # 22341. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_3().html) | PLC subdevice 3: PLC type designation # 22342. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_4](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_4().html) | PLC subdevice 4: PLC type designation # 22343. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_5](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_5().html) | PLC subdevice 5: PLC type designation # 22344. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_6](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_6().html) | PLC subdevice 6: PLC type designation # 22345. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_7](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_7().html) | PLC subdevice 7: PLC type designation # 22346. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_8](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_8().html) | PLC subdevice 8: PLC type designation # 22347. |
| Public Property | [ARTICLE\_PLCGROUP\_TYPIDENTIFIER\_9](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_TYPIDENTIFIER_9().html) | PLC subdevice 9: PLC type designation # 22348. |
| Public Property | [ARTICLE\_PLCISBUSCOUPLER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCISBUSCOUPLER().html) | Bus coupler / head station # 22019. |
| Public Property | [ARTICLE\_PLCISBUSDISTRIBUTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCISBUSDISTRIBUTOR().html) | Bus distribution device # 22053. |
| Public Property | [ARTICLE\_PLCISCPU](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCISCPU().html) | CPU # 22020. |
| Public Property | [ARTICLE\_PLCISMOUNTEDONHEADMODULE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCISMOUNTEDONHEADMODULE().html) | PLC card is placed on head station # 22290. |
| Public Property | [ARTICLE\_PLCISPOWERSUPPLY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCISPOWERSUPPLY().html) | Power supply # 22052. |
| Public Property | [ARTICLE\_PLCOBJECT\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCOBJECT_DESCRIPTION().html) | Object description # 22038. |
| Public Property | [ARTICLE\_PLCSTATIONTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCSTATIONTYPE().html) | PLC station: Type # 22269. |
| Public Property | [ARTICLE\_PLCTEMPLATEREFERENCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCTEMPLATEREFERENCE().html) | PLC device: TemplateIdentifier # 22338. |
| Public Property | [ARTICLE\_PLCTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCTYPE().html) | PLC type designation # 22105. |
| Public Property | [ARTICLE\_PLUG\_CONNECTOR\_CONNECTION\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLUG_CONNECTOR_CONNECTION_1().html) | Plug-in connector (connection 1) # 26575. |
| Public Property | [ARTICLE\_PLUG\_CONNECTOR\_CONNECTION\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLUG_CONNECTOR_CONNECTION_2().html) | Plug-in connector (connection 2) # 26577. |
| Public Property | [ARTICLE\_PLUG\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLUG_TYPE().html) | Plug type # 26574. |
| Public Property | [ARTICLE\_PNEUMATICALLY\_OPERATED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PNEUMATICALLY_OPERATED().html) | Pneumatically operated # 26057. |
| Public Property | [ARTICLE\_POLE\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POLE_NUMBER().html) | Number of poles # 26531. |
| Public Property | [ARTICLE\_POSITION\_FEEDBACK\_SIGNAL\_ACTUATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POSITION_FEEDBACK_SIGNAL_ACTUATOR().html) | Feedback signal available # 26062. |
| Public Property | [ARTICLE\_POSITION\_KEYWORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POSITION_KEYWORD().html) | Performance description, standardized: Item keyword (device, utility, service) # 26536. |
| Public Property | [ARTICLE\_POSITION\_NUMBER\_MANUFACTURER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POSITION_NUMBER_MANUFACTURER().html) | Item number (manufacturer) # 26534. |
| Public Property | [ARTICLE\_POSITION\_NUMBER\_STLB](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POSITION_NUMBER_STLB().html) | Performance description, standardized: Item number (device, utility, service) # 26532. |
| Public Property | [ARTICLE\_POSSIBLE\_APPLICATIONS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POSSIBLE_APPLICATIONS().html) | Possible uses # 26289. |
| Public Property | [ARTICLE\_POWER\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_CONSUMPTION().html) | Power consumption # 26417. |
| Public Property | [ARTICLE\_POWER\_CONTROL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_CONTROL().html) | Power control # 26048. |
| Public Property | [ARTICLE\_POWER\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_DESCRIPTION().html) | Performance description (item, device) # 26427. |
| Public Property | [ARTICLE\_POWER\_FACTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_FACTOR().html) | Power factor (cos phi) # 26657. |
| Public Property | [ARTICLE\_POWER\_GROUP\_ITEM\_NUMBER\_LGPOSNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR().html) | Performance description, standardized: Performance group item number # 26431. |
| Public Property | [ARTICLE\_POWER\_LOSS\_PER\_POLE\_CURRENT\_DEPENDENT\_PVIP](topic30.html) | Power dissipation (per pole), current-dependent # 26159. |
| Public Property | [ARTICLE\_POWER\_LOSS\_STATIC\_CURRENT\_INDEPENDENT\_PVS](topic31.html) | Power dissipation (static), current-independent # 26160. |
| Public Property | [ARTICLE\_POWER\_REQUIREMENT\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_REQUIREMENT_MAX().html) | Power requirement, max. # 26421. |
| Public Property | [ARTICLE\_POWER\_REQUIREMENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWER_REQUIREMENT_MIN().html) | Power requirement, min. # 26423. |
| Public Property | [ARTICLE\_POWERDISSIPATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_POWERDISSIPATION().html) | Max. power dissipation # 22074. |
| Public Property | [ARTICLE\_PRESSURE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRESSURE().html) | Max. working pressure # 22124. |
| Public Property | [ARTICLE\_PRESSURE\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRESSURE_FULL().html) | Max. working pressure (full) # 22230. |
| Public Property | [ARTICLE\_PRESSURE\_STAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRESSURE_STAGE().html) | Pressure level # 26259. |
| Public Property | [ARTICLE\_PRESSURELEVEL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRESSURELEVEL().html) | Nominal pressure level # 22226. |
| Public Property | [ARTICLE\_PRICEUNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRICEUNIT().html) | Price unit # 22043. |
| Public Property | [ARTICLE\_PRODUCT\_FUNCTION\_WITH\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCT_FUNCTION_WITH_BACNET().html) | BACnet: Product function # 26538. |
| Public Property | [ARTICLE\_PRODUCT\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCT_TYPE().html) | Product type # 26058. |
| Public Property | [ARTICLE\_PRODUCTGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCTGROUP().html) | Product group # 22041. |
| Public Property | [ARTICLE\_PRODUCTGROUPING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCTGROUPING().html) | Product grouping # 22367. |
| Public Property | [ARTICLE\_PRODUCTSUBGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCTSUBGROUP().html) | Product subgroup # 22028. |
| Public Property | [ARTICLE\_PRODUCTTOPGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRODUCTTOPGROUP().html) | Generic product group # 22138. |
| Public Property | [ARTICLE\_PROFILEDEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROFILEDEPTH().html) | Profile horizontal: Depth # 22188. |
| Public Property | [ARTICLE\_PROFILEDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROFILEDISTANCE().html) | Adjoining distance # 22191. |
| Public Property | [ARTICLE\_PROFILEHEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROFILEHEIGHT().html) | Profile horizontal: Height # 22187. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_IP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROTECTION_CLASS_IP().html) | Degree of protection (IP) # 26553. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_IP\_FRONT\_SIDE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROTECTION_CLASS_IP_FRONT_SIDE().html) | Degree of protection (IP): Front side # 26559. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_IP\_MOUNTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROTECTION_CLASS_IP_MOUNTED().html) | Degree of protection (IP): Mounted # 26561. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_IP\_OF\_THE\_EVALUATION\_ELECTRONICS](topic32.html) | Degree of protection (IP): Evaluation electronics # 26555. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_IP\_OF\_THE\_MEASURING\_HEAD](topic33.html) | Degree of protection (IP): Measuring head # 26557. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_IP\_REAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROTECTION_CLASS_IP_REAR().html) | Degree of protection (IP): Rear side # 26563. |
| Public Property | [ARTICLE\_PROTECTION\_CLASS\_OF\_THE\_ELECTRIC\_MOTOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR().html) | Protection type class (motor) # 26565. |
| Public Property | [ARTICLE\_PROTOCOL\_BACNET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROTOCOL_BACNET().html) | BACnet: Protocol # 26540. |
| Public Property | [ARTICLE\_PROVISION\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROVISION_OF_THE_CABLE().html) | Provision of cable # 26232. |
| Public Property | [ARTICLE\_PROVISION\_OF\_THE\_CABLE\_GLAND](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PROVISION_OF_THE_CABLE_GLAND().html) | Provision of cable gland # 26230. |
| Public Property | [ARTICLE\_PUMPING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PUMPING_CAPACITY().html) | Transport capacity # 26324. |
| Public Property | [ARTICLE\_PUMPING\_CAPACITY\_OF\_THE\_OPERATING\_LIQUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID().html) | Transport capacity of the operating fluid # 26326. |
| Public Property | [ARTICLE\_PUMPING\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PUMPING_VOLUME().html) | Transport volume # 26328. |
| Public Property | [ARTICLE\_PURCHASEPRICE\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PURCHASEPRICE_1().html) | Purchase price/price unit Currency 1 # 22109. |
| Public Property | [ARTICLE\_PURCHASEPRICE\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PURCHASEPRICE_2().html) | Purchase price/price unit Currency 2 # 22110. |
| Public Property | [ARTICLE\_PURITY\_CLASS\_OF\_THE\_CONTROL\_OIL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PURITY_CLASS_OF_THE_CONTROL_OIL().html) | Purity class of the control oil # 26060. |
| Public Property | [ARTICLE\_PURITY\_CLASS\_OF\_THE\_PRESSURISED\_FLUID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PURITY_CLASS_OF_THE_PRESSURISED_FLUID().html) | Purity class of the pressurized fluid # 26059. |
| Public Property | [ARTICLE\_QUANTITYUNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_QUANTITYUNIT().html) | Quantity unit # 22042. |
| Public Property | [ARTICLE\_RAILCROSSSECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RAILCROSSSECTION().html) | Rail cross-section # 22271. |
| Public Property | [ARTICLE\_RAILMATERIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RAILMATERIAL().html) | Rail material # 22272. |
| Public Property | [ARTICLE\_RANGE\_OF\_APPLICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RANGE_OF_APPLICATION().html) | Operating area # 26285. |
| Public Property | [ARTICLE\_RATED\_APPARENT\_POWER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_APPARENT_POWER().html) | Rated apparent power # 26234. |
| Public Property | [ARTICLE\_RATED\_CURRENT\_CONSUMPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_CURRENT_CONSUMPTION().html) | Nominal current consumption # 26504. |
| Public Property | [ARTICLE\_RATED\_CURRENT\_IN\_FOR\_THE\_POWER\_LOSS\_SPECIFICATION](topic34.html) | Rated current (ln) for power dissipation specification # 26086. |
| Public Property | [ARTICLE\_RATED\_CURRENT\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_CURRENT_MIN().html) | Nominal current, min. # 26502. |
| Public Property | [ARTICLE\_RATED\_DRIVING\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_DRIVING_TORQUE().html) | Nominal drive torque # 26466. |
| Public Property | [ARTICLE\_RATED\_OUTPUT\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_OUTPUT_TORQUE().html) | Nominal output torque # 26464. |
| Public Property | [ARTICLE\_RATED\_POWER\_KW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_POWER_KW().html) | Nominal power # 26474. |
| Public Property | [ARTICLE\_RATED\_POWER\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_POWER_MIN().html) | Nominal power (in kW), min. # 26480. |
| Public Property | [ARTICLE\_RATED\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_SPEED().html) | Nominal rotation speed # 26468. |
| Public Property | [ARTICLE\_RATED\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_VOLTAGE().html) | Nominal voltage # 26486. |
| Public Property | [ARTICLE\_RATED\_VOLTAGE\_FOR\_AC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_VOLTAGE_FOR_AC().html) | Nominal voltage (AC) # 26490. |
| Public Property | [ARTICLE\_RATED\_VOLTAGE\_FOR\_AC\_50\_HZ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_VOLTAGE_FOR_AC_50_HZ().html) | Nominal voltage (AC 50 Hz) # 26488. |
| Public Property | [ARTICLE\_RATED\_VOLTAGE\_FOR\_DC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_VOLTAGE_FOR_DC().html) | Nominal voltage (DC) # 26492. |
| Public Property | [ARTICLE\_RATED\_VOLTAGE\_OF\_THE\_CONTROL\_CIRCUIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_VOLTAGE_OF_THE_CONTROL_CIRCUIT().html) | Nominal voltage (control circuit) # 26496. |
| Public Property | [ARTICLE\_RATED\_VOLTAGE\_OF\_THE\_LOAD\_CIRCUIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RATED_VOLTAGE_OF_THE_LOAD_CIRCUIT().html) | Nominal voltage (load circuit) # 26494. |
| Public Property | [ARTICLE\_REARPANELDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REARPANELDISTANCE().html) | Distance rear panel # 22173. |
| Public Property | [ARTICLE\_REARPANELDPEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REARPANELDPEPTH().html) | Rear panel: Depth # 22174. |
| Public Property | [ARTICLE\_REARPANELPROJECTIONBOTTOM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REARPANELPROJECTIONBOTTOM().html) | Overhang: Rear panel bottom # 22172. |
| Public Property | [ARTICLE\_REARPANELPROJECTIONLEFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REARPANELPROJECTIONLEFT().html) | Overhang: Rear panel left # 22169. |
| Public Property | [ARTICLE\_REARPANELPROJECTIONRIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REARPANELPROJECTIONRIGHT().html) | Overhang: Rear panel right # 22170. |
| Public Property | [ARTICLE\_REARPANELPROJECTIONTOP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REARPANELPROJECTIONTOP().html) | Overhang: Rear panel top # 22171. |
| Public Property | [ARTICLE\_RECOMMENDED\_DIAMETER\_OF\_THE\_CABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RECOMMENDED_DIAMETER_OF_THE_CABLE().html) | Recommended cable diameter # 26297. |
| Public Property | [ARTICLE\_REF\_CONSTRUCTION\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REF_CONSTRUCTION_NAME().html) | Drilling pattern # 22217. |
| Public Property | [ARTICLE\_REF\_TERMINAL\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REF_TERMINAL_NAME().html) | Connection point pattern # 22941. |
| Public Property | [ARTICLE\_REF\_TERMINAL\_OFFSET\_X](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REF_TERMINAL_OFFSET_X().html) | Connection point pattern: Offset X-direction # 22277. |
| Public Property | [ARTICLE\_REF\_TERMINAL\_OFFSET\_Y](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REF_TERMINAL_OFFSET_Y().html) | Connection point pattern: Offset Y-direction # 22278. |
| Public Property | [ARTICLE\_REMOTE\_CONTROL\_FUNCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REMOTE_CONTROL_FUNCTION().html) | Remote control function # 26041. |
| Public Property | [ARTICLE\_REPLACEMENT\_FOR\_PRODUCT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REPLACEMENT_FOR_PRODUCT().html) | Replacement part: Original part # 26318. |
| Public Property | [ARTICLE\_REPLACEMENT\_PART\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REPLACEMENT_PART_DATE().html) | Replacement part: Date # 26320. |
| Public Property | [ARTICLE\_REPLACEMENT\_PART\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REPLACEMENT_PART_DESCRIPTION().html) | Replacement part: Description # 26038. |
| Public Property | [ARTICLE\_REPLACEMENT\_PART\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REPLACEMENT_PART_NUMBER().html) | Replacement part: Number # 26321. |
| Public Property | [ARTICLE\_REPORT\_IDENTIFIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REPORT_IDENTIFIER().html) | Identifier for reports # 22214. |
| Public Property | [ARTICLE\_REPORT\_SYMBOL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_REPORT_SYMBOL(Int32).html) | Symbol for reports # 22228. |
| Public Property | [ARTICLE\_RUN\_UP\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_RUN_UP_TIME().html) | Start-up time # 26313. |
| Public Property | [ARTICLE\_SALESPRICE\_1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SALESPRICE_1().html) | Sales price Currency 1 # 22107. |
| Public Property | [ARTICLE\_SALESPRICE\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SALESPRICE_2().html) | Sales price Currency 2 # 22108. |
| Public Property | [ARTICLE\_SEALING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SEALING().html) | Sealing # 26000. |
| Public Property | [ARTICLE\_SEALING\_MATERIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SEALING_MATERIAL().html) | Sealing material # 26067. |
| Public Property | [ARTICLE\_SECONDARY\_CASING\_PRESSURE\_STAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SECONDARY_CASING_PRESSURE_STAGE().html) | Pressure level of secondary housing # 26261. |
| Public Property | [ARTICLE\_SERVICE\_ACCORDING\_TO\_BACNET\_SPECIFICATION](topic35.html) | BACnet: Service in accord. with BACnet specification # 26033. |
| Public Property | [ARTICLE\_SERVICE\_BREAKING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SERVICE_BREAKING_CAPACITY().html) | Service short-circuit breaking capacity (Ics) # 26588. |
| Public Property | [ARTICLE\_SERVICE\_BREAKING\_CAPACITY\_PERCENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SERVICE_BREAKING_CAPACITY_PERCENT().html) | Service short-circuit breaking capacity (Ics as % of Icu) # 26592. |
| Public Property | [ARTICLE\_SERVICE\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SERVICE_UNIT().html) | Performance unit (bill of quantities) # 26429. |
| Public Property | [ARTICLE\_SET\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SET_POINT().html) | Setpoint # 26567. |
| Public Property | [ARTICLE\_SETPOINT\_OUTPUT\_HYDRAULIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SETPOINT_OUTPUT_HYDRAULIC_MAX().html) | Target power (hydraulic), max. # 26143. |
| Public Property | [ARTICLE\_SETPOINT\_OUTPUT\_HYDRAULIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SETPOINT_OUTPUT_HYDRAULIC_MIN().html) | Target power (hydraulic), min. # 26144. |
| Public Property | [ARTICLE\_SETPOINT\_OUTPUT\_PNEUMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SETPOINT_OUTPUT_PNEUMATIC().html) | Target power (pneumatic) # 26145. |
| Public Property | [ARTICLE\_SETPOINT\_POWER\_HYDRAULIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SETPOINT_POWER_HYDRAULIC().html) | Target power (hydraulic) # 26142. |
| Public Property | [ARTICLE\_SETPOINT\_POWER\_PNEUMATIC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SETPOINT_POWER_PNEUMATIC_MIN().html) | Target power (pneumatic), min. # 26147. |
| Public Property | [ARTICLE\_SHOCK\_LOAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SHOCK_LOAD().html) | Shock load # 26584. |
| Public Property | [ARTICLE\_SHORTCIRCUITRESISTANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SHORTCIRCUITRESISTANT().html) | Short-circuit proof # 22115. |
| Public Property | [ARTICLE\_SIDEPANELDEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SIDEPANELDEPTH().html) | Side panel: Depth # 22168. |
| Public Property | [ARTICLE\_SIDEPANELDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SIDEPANELDISTANCE().html) | Distance side panel # 22167. |
| Public Property | [ARTICLE\_SIDEPANELPROJECTIONBACK](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SIDEPANELPROJECTIONBACK().html) | Overhang: Side panel back # 22164. |
| Public Property | [ARTICLE\_SIDEPANELPROJECTIONBOTTOM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SIDEPANELPROJECTIONBOTTOM().html) | Overhang: Side panel bottom # 22166. |
| Public Property | [ARTICLE\_SIDEPANELPROJECTIONFRONT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SIDEPANELPROJECTIONFRONT().html) | Overhang: Side panel front # 22163. |
| Public Property | [ARTICLE\_SIDEPANELPROJECTIONTOP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SIDEPANELPROJECTIONTOP().html) | Overhang: Side panel top # 22165. |
| Public Property | [ARTICLE\_SLOT\_GAP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SLOT_GAP().html) | Slot width # 22286. |
| Public Property | [ARTICLE\_SNAPHEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SNAPHEIGHT().html) | Clip-on height # 22211. |
| Public Property | [ARTICLE\_SOUND\_INSULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SOUND_INSULATION().html) | Sound insulation # 26543. |
| Public Property | [ARTICLE\_SOUND\_PRESSURE\_LEVEL\_ACCORDING\_TO\_ISO\_20145](topic36.html) | Sound pressure level acc. to ISO 20145 # 26542. |
| Public Property | [ARTICLE\_SPACING\_ABOVE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPACING_ABOVE().html) | Mounting clearance Height: Above # 22154. |
| Public Property | [ARTICLE\_SPACING\_BELOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPACING_BELOW().html) | Mounting clearance Height: Below # 22155. |
| Public Property | [ARTICLE\_SPACING\_FRONT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPACING_FRONT().html) | Mounting clearance Depth: Front # 22156. |
| Public Property | [ARTICLE\_SPACING\_LEFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPACING_LEFT().html) | Mounting clearance Width: Left # 22152. |
| Public Property | [ARTICLE\_SPACING\_REAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPACING_REAR().html) | Mounting clearance Depth: Rear # 22157. |
| Public Property | [ARTICLE\_SPACING\_RIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPACING_RIGHT().html) | Mounting clearance Width: Right # 22153. |
| Public Property | [ARTICLE\_SPARE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPARE().html) | Spare part # 22140. |
| Public Property | [ARTICLE\_SPECIFIED\_MAXIMUM\_DRIVE\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPECIFIED_MAXIMUM_DRIVE_TORQUE().html) | Drive torque (specified), max. # 26570. |
| Public Property | [ARTICLE\_SPECIFIED\_MINIMUM\_DRIVE\_TORQUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE().html) | Drive torque (specified), min. # 26572. |
| Public Property | [ARTICLE\_SPEED\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPEED_MAX().html) | Rotation speed, max. # 26255. |
| Public Property | [ARTICLE\_SPEED\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SPEED_MIN().html) | Rotation speed, min. # 26257. |
| Public Property | [ARTICLE\_STANDARD\_BACNET\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STANDARD_BACNET_().html) | BACnet: Standard # 26516. |
| Public Property | [ARTICLE\_STANDARDINVERS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STANDARDINVERS().html) | Plugs: Standard / inverse # 22098. |
| Public Property | [ARTICLE\_START\_UP\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_START_UP_TIME().html) | Switch-on time # 26192. |
| Public Property | [ARTICLE\_STARTING\_CURRENT\_A](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STARTING_CURRENT_A().html) | Starting current, max. # 26190. |
| Public Property | [ARTICLE\_STORAGE\_TRANSPORT\_AND\_PACKAGING\_REQUIREMENT](topic37.html) | Storage, transport and packaging (requirement) # 26409. |
| Public Property | [ARTICLE\_STRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STRESS().html) | Stress # 22143. |
| Public Property | [ARTICLE\_STRIPPING\_LENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STRIPPING_LENGTH().html) | Jacket (cable) stripping length # 26010. |
| Public Property | [ARTICLE\_STROKELENGTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STROKELENGTH().html) | Length of stroke # 22129. |
| Public Property | [ARTICLE\_SUBCRAFT\_COOLING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_COOLING(Int32).html) | Subtrade 'Cooling' # 22196. |
| Public Property | [ARTICLE\_SUBCRAFT\_COOLINGLUBRICANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_COOLINGLUBRICANT(Int32).html) | Subtrade 'Cooling lubricant' # 22265. |
| Public Property | [ARTICLE\_SUBCRAFT\_ELECTRICAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_ELECTRICAL(Int32).html) | Subtrade 'Electrical engineering' # 22077. |
| Public Property | [ARTICLE\_SUBCRAFT\_FLUID\_UNDEFINED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_FLUID_UNDEFINED(Int32).html) | Subtrade 'Fluid power (undefined)' # 22267. |
| Public Property | [ARTICLE\_SUBCRAFT\_GASTECHNOLOGY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_GASTECHNOLOGY(Int32).html) | Subtrade 'Gas engineering' # 22266. |
| Public Property | [ARTICLE\_SUBCRAFT\_HYDRAULICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_HYDRAULICS(Int32).html) | Subtrade 'Hydraulics' # 22158. |
| Public Property | [ARTICLE\_SUBCRAFT\_LUBRICATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_LUBRICATION(Int32).html) | Subtrade 'Lubrication' # 22195. |
| Public Property | [ARTICLE\_SUBCRAFT\_MECHANICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_MECHANICS(Int32).html) | Subtrade 'Mechanics' # 22094. |
| Public Property | [ARTICLE\_SUBCRAFT\_PNEUMATICS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_PNEUMATICS(Int32).html) | Subtrade 'Pneumatics' # 22159. |
| Public Property | [ARTICLE\_SUBCRAFT\_PROCESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_PROCESS(Int32).html) | Subtrade 'Process engineering' # 22197. |
| Public Property | [ARTICLE\_SUCTION\_VOLUME\_FLOW\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUCTION_VOLUME_FLOW_MAX().html) | Intake flow rate, max. # 26198. |
| Public Property | [ARTICLE\_SUITABLE\_AS\_MONITOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUITABLE_AS_MONITOR().html) | Suitable as monitoring device # 26355. |
| Public Property | [ARTICLE\_SUITABLE\_FOR\_CABLE\_DIAMETERS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUITABLE_FOR_CABLE_DIAMETERS().html) | Suitable for cable diameter # 26350. |
| Public Property | [ARTICLE\_SUITABLE\_FOR\_KNX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUITABLE_FOR_KNX().html) | Suitable for KNX # 26043. |
| Public Property | [ARTICLE\_SUITABLE\_FOR\_PCF\_HCS\_FIBRE\_230\_uM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUITABLE_FOR_PCF_HCS_FIBRE_230_uM().html) | Suitable for PCF / HCS fiber 230 Âµm # 26357. |
| Public Property | [ARTICLE\_SUITABLE\_FOR\_PROTECTION\_CLASS\_IP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP().html) | Suitable for degree of protection (IP) # 26358. |
| Public Property | [ARTICLE\_SUPPLIER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLIER().html) | Supplier # 22008. |
| Public Property | [ARTICLE\_SUPPLIER\_BATCH\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLIER_BATCH_NUMBER().html) | Supplier batch number # 26435. |
| Public Property | [ARTICLE\_SUPPLIER\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLIER_NAME().html) | Supplier name # 22223. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE().html) | Supply voltage # 26161. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_ADJUSTABLE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_ADJUSTABLE().html) | Supply voltage adjustable # 26171. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_AT\_AC\_50\_HZ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ().html) | Supply voltage (AC 50 Hz) # 26162. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_AT\_AC\_50\_HZ\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MAX().html) | Supply voltage (AC 50 Hz), max. # 26163. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_AT\_AC\_50\_HZ\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MIN().html) | Supply voltage (AC 50 Hz), min. # 26164. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_AT\_AC\_60\_HZ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ().html) | Supply voltage (AC 60 Hz) # 26165. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_AT\_AC\_60\_HZ\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MAX().html) | Supply voltage (AC 60 Hz), max. # 26166. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_AT\_AC\_60\_HZ\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MIN().html) | Supply voltage (AC 60 Hz), min. # 26167. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_FOR\_DC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_FOR_DC().html) | Supply voltage (DC) # 26168. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_FOR\_DC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MAX().html) | Supply voltage (DC), max. # 26169. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_FOR\_DC\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN().html) | Supply voltage (DC), min. # 26170. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_MAX().html) | Supply voltage, max. # 26172. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_MIN().html) | Supply voltage, min. # 26173. |
| Public Property | [ARTICLE\_SUPPLY\_VOLTAGE\_RANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPLY_VOLTAGE_RANGE().html) | Supply voltage range # 26623. |
| Public Property | [ARTICLE\_SUPPORTS\_PROTOCOL\_EIB\_KNX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPORTS_PROTOCOL_EIB_KNX().html) | KNX: Supports EIB protocol # 26064. |
| Public Property | [ARTICLE\_SUPPORTS\_PROTOCOL\_INCOMING\_EIB\_KNX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPORTS_PROTOCOL_INCOMING_EIB_KNX().html) | KNX: Supports EIB protocol, incoming # 26066. |
| Public Property | [ARTICLE\_SUPPORTS\_PROTOCOL\_OUTGOING\_EIB\_KNX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPORTS_PROTOCOL_OUTGOING_EIB_KNX().html) | KNX: Supports EIB protocol, outgoing # 26065. |
| Public Property | [ARTICLE\_SUPPRESSINPARTSLIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPRESSINPARTSLIST().html) | Suppress in bill of materials # 22886. |
| Public Property | [ARTICLE\_SURFACE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SURFACE().html) | Type of surface # 26225. |
| Public Property | [ARTICLE\_SURFACE\_COATING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SURFACE_COATING().html) | Surface coating # 26056. |
| Public Property | [ARTICLE\_SWITCHING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SWITCHING_CAPACITY().html) | Switching capacity # 26545. |
| Public Property | [ARTICLE\_SWITCHING\_CURRENT\_RESISTIVE\_LOAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SWITCHING_CURRENT_RESISTIVE_LOAD().html) | Switching current (resistive load) # 26138. |
| Public Property | [ARTICLE\_SWITCHING\_FREQUENCY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SWITCHING_FREQUENCY().html) | Switching frequency # 26544. |
| Public Property | [ARTICLE\_TAB\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TAB_WIDTH().html) | Finger width # 22285. |
| Public Property | [ARTICLE\_TARGET\_OUTPUT\_PNEUMATIC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TARGET_OUTPUT_PNEUMATIC_MAX().html) | Target power (pneumatic), max. # 26146. |
| Public Property | [ARTICLE\_TARGET\_TOTAL\_VOLUMETRIC\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TARGET_TOTAL_VOLUMETRIC_FLOW().html) | Target total flow rate # 26139. |
| Public Property | [ARTICLE\_TARGET\_TOTAL\_VOLUMETRIC\_FLOW\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TARGET_TOTAL_VOLUMETRIC_FLOW_MAX().html) | Target total flow rate, max. # 26140. |
| Public Property | [ARTICLE\_TARGET\_TOTAL\_VOLUMETRIC\_FLOW\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TARGET_TOTAL_VOLUMETRIC_FLOW_MIN().html) | Target total flow rate, min. # 26141. |
| Public Property | [ARTICLE\_TCF\_CALCULATION\_METHOD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TCF_CALCULATION_METHOD().html) | TCF: Calculation method # 26599. |
| Public Property | [ARTICLE\_TCF\_CO2EQ](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TCF_CO2EQ().html) | TCF: CO2-eq # 26601. |
| Public Property | [ARTICLE\_TCF\_GOODS\_ACCEPTANCE\_ADDRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TCF_GOODS_ACCEPTANCE_ADDRESS().html) | TCF: Address for acceptance of goods # 26606. |
| Public Property | [ARTICLE\_TCF\_GOODS\_HANDOVER\_ADDRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TCF_GOODS_HANDOVER_ADDRESS().html) | TCF: Address for delivery of goods # 26605. |
| Public Property | [ARTICLE\_TCF\_PROCESSES\_FOR\_GREENHOUSE\_GAS\_EMISSIONS\_FOR\_A\_TRANSPORT\_SERVICE](topic38.html) | TCF: Processes for greenhouse gas emissions in a transport service # 26603. |
| Public Property | [ARTICLE\_TCF\_QUANTITY\_REFERENCE\_FOR\_CALCULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TCF_QUANTITY_REFERENCE_FOR_CALCULATION().html) | TCF: Quantity for the calculation # 26602. |
| Public Property | [ARTICLE\_TCF\_REFERENCE\_VALUE\_FOR\_CALCULATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TCF_REFERENCE_VALUE_FOR_CALCULATION().html) | TCF: Reference value for the calculation # 26600. |
| Public Property | [ARTICLE\_TCF\_TRANSPORT\_CARBON\_FOOTPRINT\_CALCULATION](topic39.html) | TCF: Calculation # 26604. |
| Public Property | [ARTICLE\_TEMPERATUR\_MEDIUM\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATUR_MEDIUM_MAX().html) | Temperature (medium), max. # 26609. |
| Public Property | [ARTICLE\_TEMPERATUR\_MEDIUM\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATUR_MEDIUM_MIN().html) | Temperature (medium), min. # 26611. |
| Public Property | [ARTICLE\_TEMPERATURE\_COEFFICIENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATURE_COEFFICIENT().html) | Temperature coefficient # 22274. |
| Public Property | [ARTICLE\_TEMPERATURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATURE_MAX().html) | Temperature, max. # 26607. |
| Public Property | [ARTICLE\_TEMPERATURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATURE_MIN().html) | Temperature, min. # 26613. |
| Public Property | [ARTICLE\_TEMPERATURE\_RANGE\_MEDIUM\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATURE_RANGE_MEDIUM_MAX().html) | Temperature range (medium), max. # 26615. |
| Public Property | [ARTICLE\_TEMPERATURE\_RANGE\_MEDIUM\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN().html) | Temperature range (medium), min. # 26617. |
| Public Property | [ARTICLE\_TERMINAL\_POTENTIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TERMINAL_POTENTIAL().html) | Terminal potential # 26118. |
| Public Property | [ARTICLE\_TERMINALSIZE\_DESTINATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TERMINALSIZE_DESTINATION().html) | Connection dimension target # 22282. |
| Public Property | [ARTICLE\_TERMINALSIZE\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TERMINALSIZE_SOURCE().html) | Connection dimension source # 22281. |
| Public Property | [ARTICLE\_TEST\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TEST_VOLTAGE().html) | Test voltage # 26133. |
| Public Property | [ARTICLE\_THICKNESS\_OF\_MATERIAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THICKNESS_OF_MATERIAL().html) | Material thickness # 26096. |
| Public Property | [ARTICLE\_THREAD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THREAD().html) | Thread # 22127. |
| Public Property | [ARTICLE\_THREAD\_SIZE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THREAD_SIZE().html) | Thread dimension # 26108. |
| Public Property | [ARTICLE\_THREAD\_SIZE\_FITTING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THREAD_SIZE_FITTING().html) | Thread dimension (fitting) # 26109. |
| Public Property | [ARTICLE\_THREAD\_SIZE\_METRIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THREAD_SIZE_METRIC().html) | Thread size (metric) # 26107. |
| Public Property | [ARTICLE\_THROUGHPUT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THROUGHPUT().html) | Throughput # 26269. |
| Public Property | [ARTICLE\_TIGHTENING\_TORQUE\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TIGHTENING_TORQUE_().html) | Tightening torque # 26080. |
| Public Property | [ARTICLE\_TIGHTENING\_TORQUE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TIGHTENING_TORQUE_MAX().html) | Tightening torque, max. # 26081. |
| Public Property | [ARTICLE\_TIGHTENING\_TORQUE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TIGHTENING_TORQUE_MIN().html) | Tightening torque, min. # 26082. |
| Public Property | [ARTICLE\_TOPPANELDISTANCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOPPANELDISTANCE().html) | Distance cover # 22179. |
| Public Property | [ARTICLE\_TOPPANELDPEPTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOPPANELDPEPTH().html) | Cover: Depth # 22180. |
| Public Property | [ARTICLE\_TOPPANELPROJECTIONBACK](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOPPANELPROJECTIONBACK().html) | Overhang: Cover back # 22178. |
| Public Property | [ARTICLE\_TOPPANELPROJECTIONFRONT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOPPANELPROJECTIONFRONT().html) | Overhang: Cover front # 22177. |
| Public Property | [ARTICLE\_TOPPANELPROJECTIONLEFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOPPANELPROJECTIONLEFT().html) | Overhang: Cover left # 22175. |
| Public Property | [ARTICLE\_TOPPANELPROJECTIONRIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOPPANELPROJECTIONRIGHT().html) | Overhang: Cover right # 22176. |
| Public Property | [ARTICLE\_TORQUE\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TORQUE_().html) | Torque # 26247. |
| Public Property | [ARTICLE\_TORQUE\_AT\_MAX\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TORQUE_AT_MAX_SPEED().html) | Torque (at max. rotation speed) # 26249. |
| Public Property | [ARTICLE\_TORQUE\_AT\_MIN\_SPEED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TORQUE_AT_MIN_SPEED().html) | Torque (at min. rotation speed) # 26251. |
| Public Property | [ARTICLE\_TORQUE\_MAX\_](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TORQUE_MAX_().html) | Torque, max. # 26253. |
| Public Property | [ARTICLE\_TOTAL\_COOLING\_CAPACITY\_AT\_35\_35\_C](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOTAL_COOLING_CAPACITY_AT_35_35_C().html) | Total cooling capacity (at 35/35Â°C) # 26105. |
| Public Property | [ARTICLE\_TOTAL\_NUMBER\_OF\_BACNET\_OBJECTS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOTAL_NUMBER_OF_BACNET_OBJECTS().html) | BACnet: Total number of objects # 26210. |
| Public Property | [ARTICLE\_TOTAL\_PRESSURE\_DIFFERENCE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOTAL_PRESSURE_DIFFERENCE_MAX().html) | Total pressure difference, max. # 26103. |
| Public Property | [ARTICLE\_TOTAL\_PRESSURE\_DIFFERENCE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOTAL_PRESSURE_DIFFERENCE_MIN().html) | Total pressure difference, min. # 26104. |
| Public Property | [ARTICLE\_TOTAL\_VOLUME\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TOTAL_VOLUME_FLOW().html) | Total flow rate # 26106. |
| Public Property | [ARTICLE\_TRIGGERCURRENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TRIGGERCURRENT().html) | Tripping current # 22075. |
| Public Property | [ARTICLE\_TYPE\_OF\_CERTIFICATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_CERTIFICATE().html) | Type of certificate # 26022. |
| Public Property | [ARTICLE\_TYPE\_OF\_CONSTRUCTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_CONSTRUCTION().html) | Design # 26229. |
| Public Property | [ARTICLE\_TYPE\_OF\_CONTROL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_CONTROL().html) | Type of control # 26017. |
| Public Property | [ARTICLE\_TYPE\_OF\_CONTROL\_COMMAND\_TRANSMISSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_CONTROL_COMMAND_TRANSMISSION().html) | Type of control (command transmission) # 26018. |
| Public Property | [ARTICLE\_TYPE\_OF\_CONTROL\_TECHNOLOGY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_CONTROL_TECHNOLOGY().html) | Type of control (technology) # 26019. |
| Public Property | [ARTICLE\_TYPE\_OF\_COOLING\_MEDIUM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_COOLING_MEDIUM().html) | Type of cooling medium # 26020. |
| Public Property | [ARTICLE\_TYPE\_OF\_DYNAMIC\_SEAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_DYNAMIC_SEAL().html) | Type of construction: Dynamic seal # 26025. |
| Public Property | [ARTICLE\_TYPE\_OF\_FIXING\_POINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_FIXING_POINT().html) | Type of attachment point # 26218. |
| Public Property | [ARTICLE\_TYPE\_OF\_FLOW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_FLOW().html) | Type of flow # 26219. |
| Public Property | [ARTICLE\_TYPE\_OF\_HEATING\_COOLING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_HEATING_COOLING().html) | Type of heating / cooling # 26015. |
| Public Property | [ARTICLE\_TYPE\_OF\_MOUNTING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_MOUNTING().html) | Mounting type # 26187. |
| Public Property | [ARTICLE\_TYPE\_OF\_OPERATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_OPERATION().html) | Type of operation # 26236. |
| Public Property | [ARTICLE\_TYPE\_OF\_SEAL\_EX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_SEAL_EX().html) | Type of seal (EX) # 26014. |
| Public Property | [ARTICLE\_TYPE\_OF\_SEALING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_SEALING().html) | Type of sealing # 26013. |
| Public Property | [ARTICLE\_TYPE\_OF\_SENSOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_SENSOR().html) | Type of sensor # 26021. |
| Public Property | [ARTICLE\_TYPE\_OF\_STATIC\_SEAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_STATIC_SEAL().html) | Type of construction: Static seal # 26026. |
| Public Property | [ARTICLE\_TYPE\_OF\_SWITCHING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_SWITCHING().html) | Circuit type # 26547. |
| Public Property | [ARTICLE\_TYPE\_OF\_USE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_USE().html) | Operating mode # 26283. |
| Public Property | [ARTICLE\_TYPENR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPENR().html) | Type number # 22002. |
| Public Property | [ARTICLE\_ULTIMATE\_BREAKING\_CAPACITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ULTIMATE_BREAKING_CAPACITY().html) | Rated ultimate short-circuit breaking capacity (Icu) # 26587. |
| Public Property | [ARTICLE\_ULTIMATE\_BREAKING\_CAPACITY\_AC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ULTIMATE_BREAKING_CAPACITY_AC().html) | Rated breaking capacity (AC) # 26590. |
| Public Property | [ARTICLE\_ULTIMATE\_BREAKING\_CAPACITY\_DC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ULTIMATE_BREAKING_CAPACITY_DC().html) | Rated breaking capacity (DC) # 26591. |
| Public Property | [ARTICLE\_ULTIMATE\_PRESSURE\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ULTIMATE_PRESSURE_MAX().html) | Final pressure, max. # 26101. |
| Public Property | [ARTICLE\_ULTIMATE\_PRESSURE\_MIN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ULTIMATE_PRESSURE_MIN().html) | Final pressure, min. # 26102. |
| Public Property | [ARTICLE\_ULTIMATE\_PRESSURE\_SET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ULTIMATE_PRESSURE_SET().html) | Final pressure, preset # 26100. |
| Public Property | [ARTICLE\_UNIQUEID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_UNIQUEID().html) | Unique part ID # 22060. |
| Public Property | [ARTICLE\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_UNIT().html) | Unit # 26281. |
| Public Property | [ARTICLE\_UNIT\_CLASS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_UNIT_CLASS().html) | Device class # 26366. |
| Public Property | [ARTICLE\_UNIT\_DESIGN](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_UNIT_DESIGN().html) | Type of construction: Device # 26364. |
| Public Property | [ARTICLE\_UPPER\_PROCESS\_PRESSURE\_LIMIT\_ABSOLUTE\_PRESSURE](topic40.html) | Process pressure (absolute pressure), max. # 26518. |
| Public Property | [ARTICLE\_UPPER\_PROCESS\_PRESSURE\_LIMIT\_GAUGE\_PRESSURE](topic41.html) | Process pressure (overpressure), max. # 26520. |
| Public Property | [ARTICLE\_USAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_USAGE().html) | Procurement # 22144. |
| Public Property | [ARTICLE\_USE\_FOR\_MARKING\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_USE_FOR_MARKING_TYPE().html) | Usage for labeling type # 26625. |
| Public Property | [ARTICLE\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VARIANT().html) | Variant # 22024. |
| Public Property | [ARTICLE\_VARIANT\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VARIANT_DESCRIPTION().html) | Part variant description # 22887. |
| Public Property | [ARTICLE\_VERSION\_AS\_MAINTENANCE\_REPAIR\_SWITCH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VERSION_AS_MAINTENANCE_REPAIR_SWITCH().html) | Designed as maintenance / repair switch # 26012. |
| Public Property | [ARTICLE\_VISCOSITY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VISCOSITY().html) | Viscosity # 26627. |
| Public Property | [ARTICLE\_VISCOSITY\_CLASS\_ACCORDING\_TO\_DIN\_51519](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VISCOSITY_CLASS_ACCORDING_TO_DIN_51519().html) | Viscosity class (acc. to DIN 51519) # 26631. |
| Public Property | [ARTICLE\_VISCOSITY\_INDEX\_ACCORDING\_TO\_DIN\_ISO\_2909](topic42.html) | Viscosity index (acc. to DIN ISO 2909) # 26629. |
| Public Property | [ARTICLE\_VOLTAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGE().html) | Voltage # 22033. |
| Public Property | [ARTICLE\_VOLTAGE\_LOAD\_RESISTIVE\_LOAD\_DC\_MAX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGE_LOAD_RESISTIVE_LOAD_DC_MAX().html) | Voltage load (resistive load, DC), max. # 26148. |
| Public Property | [ARTICLE\_VOLTAGECSA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGECSA().html) | Terminals: Voltage CSA # 22093. |
| Public Property | [ARTICLE\_VOLTAGEIEC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGEIEC().html) | Terminals: Voltage IEC # 22089. |
| Public Property | [ARTICLE\_VOLTAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGETYPE().html) | Voltage type # 22070. |
| Public Property | [ARTICLE\_VOLTAGEUL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLTAGEUL().html) | Terminals: Voltage UL # 22091. |
| Public Property | [ARTICLE\_VOLUME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLUME().html) | Volume # 26174. |
| Public Property | [ARTICLE\_VOLUME\_FLOW\_FREELY\_BLOWING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLUME_FLOW_FREELY_BLOWING().html) | Flow rate (free blowing) # 26175. |
| Public Property | [ARTICLE\_VOLUME\_FLOW\_HEATING\_M3\_H](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLUME_FLOW_HEATING_M3_H().html) | Flow rate # 26633. |
| Public Property | [ARTICLE\_VOLUME\_FLOW\_MAX\_M3\_H](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VOLUME_FLOW_MAX_M3_H().html) | Flow rate (mÂ³/h), max. # 26176. |
| Public Property | [ARTICLE\_VPROFILEDPETH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VPROFILEDPETH().html) | Profile vertical: Depth # 22190. |
| Public Property | [ARTICLE\_VPROFILEWIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VPROFILEWIDTH().html) | Profile vertical: Width # 22189. |
| Public Property | [ARTICLE\_WALLTHICKNESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WALLTHICKNESS().html) | Wall thickness # 22216. |
| Public Property | [ARTICLE\_WEAR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEAR().html) | Wearing part # 22139. |
| Public Property | [ARTICLE\_WEIGHT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT().html) | Weight # 22046. |
| Public Property | [ARTICLE\_WEIGHT\_DISPLAY\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT_DISPLAY_UNIT().html) | Weight in displayed unit # 22059. |
| Public Property | [ARTICLE\_WEIGHT\_FULL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT_FULL().html) | Weight (full) # 22233. |
| Public Property | [ARTICLE\_WEIGHT\_ITEM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT_ITEM().html) | Weight (part) # 26370. |
| Public Property | [ARTICLE\_WEIGHT\_KG\_1000\_M](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT_KG_1000_M().html) | Weight (in kg/1000 m) # 26374. |
| Public Property | [ARTICLE\_WEIGHT\_OF\_THE\_INDIVIDUAL\_ARTICLE\_PACKAGING](topic43.html) | Weight (individual packaging) # 26376. |
| Public Property | [ARTICLE\_WEIGHT\_OF\_THE\_PACKAGING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT_OF_THE_PACKAGING().html) | Weight (packaging) # 26378. |
| Public Property | [ARTICLE\_WEIGHT\_TOTAL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WEIGHT_TOTAL().html) | Total weight (part) # 26372. |
| Public Property | [ARTICLE\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIDTH().html) | Width # 22013. |
| Public Property | [ARTICLE\_WIDTHBOTTOM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIDTHBOTTOM().html) | Width bottom # 22199. |
| Public Property | [ARTICLE\_WIDTHRATING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIDTHRATING().html) | Nominal size # 22225. |
| Public Property | [ARTICLE\_WIDTHTOP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIDTHTOP().html) | Width top # 22198. |
| Public Property | [ARTICLE\_WIRECROSSSECTION\_AND\_DIAMETER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIRECROSSSECTION_AND_DIAMETER().html) | No. of connections and cross-section / diameter # 22069. |
| Public Property | [ARTICLE\_WIRECROSSSECTION\_UNIT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIRECROSSSECTION_UNIT().html) | Unit for connection cross-section / diameter # 22068. |
| Public Property | [ARTICLE\_WIRETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIRETYPE().html) | Connection type # 22254. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [MESSAGEMGMT\_MESSAGES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~MESSAGEMGMT_MESSAGES().html) | Check run messages available # 20930. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [PART\_CREATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~PART_CREATE().html) | Creator / Creation date # 22902. |
| Public Property | [PART\_LASTCHANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~PART_LASTCHANGE().html) | Last editor / Modification date # 22901. |
| Public Property | [PART\_USED\_AS\_ACCESSORY\_FILTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~PART_USED_AS_ACCESSORY_FILTER().html) | Part number in accessory # 22963. |
| Public Property | [PART\_USED\_IN\_ASSEMBLY\_FILTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~PART_USED_IN_ASSEMBLY_FILTER().html) | Part number in assembly # 22967. |
| Public Property | [PART\_USED\_IN\_MODULE\_FILTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~PART_USED_IN_MODULE_FILTER().html) | Part number in module # 22966. |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of ArticlePropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |

[Top](#top)




See Also

#### Reference

[ArticlePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)
  
[StorableObjectPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)