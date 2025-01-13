using System.Diagnostics;
using System.Windows.Forms;
using System.Xml;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        string filename =
            PathMap.SubstitutePath(@"$(PROJECTPATH)\Testfile.xml");

        XmlWriterSettings xs = new XmlWriterSettings();
        xs.Indent = true;
        xs.IndentChars = "\t";

        XmlWriter xw = XmlWriter.Create(filename, xs);

        xw.WriteStartDocument();

        xw.WriteStartElement("People");

            xw.WriteStartElement("Person");
                xw.WriteElementString("First name", "Max");
                xw.WriteElementString("Last name", "Mustermann");
                xw.WriteStartElement("Address");
                xw.WriteAttributeString("Location", "München");
                xw.WriteAttributeString("Street", "Musterstraße 1");
                xw.WriteEndElement();
            xw.WriteEndElement();

        xw.WriteStartElement("Person");
            xw.WriteElementString("First name", "Maria");
            xw.WriteElementString("Last name", "Musterfrau");
            xw.WriteStartElement("Address");
            xw.WriteAttributeString("Location", "München");
            xw.WriteAttributeString("Street", "Musterstraße 2");
            xw.WriteEndElement();
        xw.WriteEndElement();

        // Personen: Ende
        xw.WriteEndElement();

        xw.WriteEndDocument();
        xw.Close();

        MessageBox.Show(
            "XML file successfully exported.",
            "Information",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information
            );

        Process.Start(filename);

        return;
    }

}



