# TextColorId Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~TextColorId.html

---

Color for displayed text. Color index (0-255) Please use -16002 as "From layer" value.

Predefined values for line color index are:

0 = black

1 = red

2 = yellow

3 = green

4 = cyan

5 = blue

6 = magenta

7 = white

252 = darkgray

253 = gray

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public short TextColorId {get; set;}
```
```

```
```
public:
property short TextColorId {
   short get();
   void set (    short value);
}
```
```

#### Property Value

Color index used by object

Remarks

In case of PropertyPlacement, TextColorId property can be used to change color of both text and its boxes. In case of other texts, TextColorId changes color of text and.Pen.ColorId color of its boxes.



See Also

#### Reference

[TextBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase.html)
  
[TextBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase_members.html)