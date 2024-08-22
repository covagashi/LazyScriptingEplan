# Guía de inicio a la programación en EPLAN 2022 con C#

## Introducción

Esta guía está diseñada para ayudarte a dar tus primeros pasos en la programación de scripts para EPLAN 2022 utilizando C#, incluso si no tienes experiencia previa en programación. Aprenderemos a través de ejemplos prácticos, comenzando desde lo más básico hasta conceptos un poco más avanzados.

## Requisitos previos

- EPLAN Electric P8 2022 instalado en tu computadora.
- Conocimientos básicos de cómo usar EPLAN.
- Un editor de texto simple como el Bloc de notas o, preferiblemente, un entorno de desarrollo integrado (IDE) como Visual Studio Code.

## 1. Tu primer script en EPLAN

Empecemos con un script simple que muestra un mensaje.

```csharp
using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class MiPrimerScript
{
    [Start]
    public void Function()
    {
        MessageBox.Show("¡Hola, mundo! Este es mi primer script en EPLAN.");
    }
}
```
### Explicación:

1. `using`: Estas líneas al principio nos permiten usar funciones de Windows Forms y EPLAN.
2. `public class MiPrimerScript`: Definimos una clase que contendrá nuestro código.
3. `[Start]`: Esta etiqueta le dice a EPLAN que este es el punto de inicio del script.
4. `public void Function()`: Esta es la función que se ejecutará cuando EPLAN inicie el script.
5. `MessageBox.Show()`: Esta función muestra un cuadro de mensaje con el texto que le pasemos.

### Cómo ejecutar:

- Guarda este código en un archivo con extensión .cs, por ejemplo, MiPrimerScript.cs.
- Fichero > Extras > grupo de comandos Ampliaciones > Interfaces > grupo de comandos Scripts > Ejecutar.
- Selecciona tu archivo MiPrimerScript.cs.
- Verás un cuadro de mensaje que dice "¡Hola, mundo! Este es mi primer script en EPLAN."

## 2. Estructura básica de un script de EPLAN
Los scripts de EPLAN siguen una estructura básica:

- **Importaciones (using):** Al principio del archivo, importamos las bibliotecas necesarias.
- **Definición de la clase:** Creamos una clase que contendrá nuestras funciones.
- **Métodos:** Dentro de la clase, definimos uno o más métodos que realizarán las acciones deseadas.
- **Atributos:** Usamos atributos como `[Start]` o `[DeclareAction]` para indicar cómo EPLAN debe manejar nuestros métodos.

## 3. Acceso a las API de EPLAN
EPLAN proporciona varias API que podemos usar en nuestros scripts. Algunas de las más comunes son:

- `Eplan.EplApi.Base:` Contiene clases básicas para trabajar con EPLAN.
- `Eplan.EplApi.Scripting:` Proporciona funcionalidades para la ejecución de scripts.
- `Eplan.EplApi.DataModel:` Permite acceder y manipular datos del proyecto.

## 4. Trabajando con acciones en EPLAN

Las acciones son una forma poderosa de extender la funcionalidad de EPLAN. Veamos cómo crear una acción personalizada.

### Ejemplo: Creando una acción personalizada

```csharp
using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class MiAccionPersonalizada
{
    [DeclareAction("MiPrimeraAccion")]
    public void EjecutarAccion()
    {
        MessageBox.Show("¡Has ejecutado tu primera acción personalizada en EPLAN!");
    }
}
```

### Explicación:

1. Usamos el atributo [DeclareAction] para registrar nuestra función como una acción en EPLAN.
2. El nombre "MiPrimeraAccion" es el identificador que usaremos para llamar a esta acción desde EPLAN.
3. La función EjecutarAccion() contiene el código que se ejecutará cuando se llame a la acción.

### Cómo usar:

- Guarda y carga este script en EPLAN.
- Ahora puedes llamar a "MiPrimeraAccion" desde cualquier lugar en EPLAN donde puedas ejecutar acciones, como la línea de comandos o asignándola a un botón personalizado.

## 5. Creación de una interfaz de usuario simple

Aunque los cuadros de mensaje son útiles, a veces necesitamos interfaces más complejas. Veamos cómo crear un formulario simple.
```csharp
using System;
using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class InterfazUsuarioSimple
{
    [Start]
    public void MostrarFormulario()
    {
        Form formulario = new Form();
        formulario.Text = "Mi Formulario EPLAN";
        formulario.Size = new System.Drawing.Size(300, 200);

        Button boton = new Button();
        boton.Text = "Haz clic aquí";
        boton.Location = new System.Drawing.Point(100, 50);
        boton.Click += (sender, e) => MessageBox.Show("¡Botón clicado!");

        formulario.Controls.Add(boton);
        formulario.ShowDialog();
    }
}
```
### Explicación:

1. Creamos un nuevo objeto Form para nuestro formulario.
2. Añadimos un botón al formulario.
3. Usamos un evento Click para el botón, que muestra un mensaje cuando se hace clic en él.
4. Mostramos el formulario con ShowDialog().