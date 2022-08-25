<h3 align="center">
    <img height="150" src="/lib/assets/logoAthena.png" width="150"/>

<FONT SIZE=3>APImg de Athena</FONT>
</h3>

# Intro
<i align = "right">
Código para control y monitoreo de temperaturas en sistema ECMO para corazón
</i>

---

<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#comenzando">Comenzando 🚀</a>
    </li>
    <li>
      <a href="#pre-requisitos">Pre-Requisitos 📋</a>
      <ul>
        <li><a href="#requisitos-desarrollador">Requisitos Desarrollador 💻</a></li>
        <li><a href="#requisitos-usuario">Requisitos Usuario 👨‍🦱</a></li>
      </ul>
    </li>
    <li><a href="#instalación">Instalación 🔧</a></li>
    <li>
      <a href="#pruebas">Pruebas 🔩</a>      
      <ul>
        <li><a href="#pruebas-software">Pruebas Software 👨‍💻</a></li>
        <li><a href="#pruebas-hardware">Pruebas Hardware 🔌</a></li>
      </ul>
    </li>
    <li><a href="#diagramas">Diagramas 📚</a></li>
    <li><a href="#despliegue">Despliegue 📦</a></li>
    <li><a href="#construcción">Construido con</a></li>
    <li><a href="#versionado">Versionado 📌</a></li>
    <li><a href="#wiki">Wiki 📖</a></li>
    <li><a href="#autores">Autores 🖋</a></li>
    <li><a href="#licencia">Licencia 📄</a></li>
    <li><a href="#expresiones-de-gratitud">Expresiones De Gratitud 🎁</a></li>
  </ol>
</details>

<p align="right">(<a href="#intro">Inicio</a>)</p>

## Comenzando 🚀          
<div align="left">
  <a href = "https://github.com/ThunderGer23/APImg">
    <img width="20" height="20" src="/lib/assets/icons/GitHub.webp"/>
  </a>
  <i>click para obtener el código de la API</i>
</div>

<p align="right">(<a href="#intro">Inicio</a>)</p>

### Pre-requisitos 📋

_Conocimientos intermadios en bases de datos, servidores, microservicios y python. Además del manejo de entornos virtuales con las siguientes instalaciones_


#### Requisitos Desarrollador 💻

_Debe contar con el siguiente conjunto de herramientas instaladas_

- [ ] Python
- [ ] Editor de texto/IDE
- [ ] MongoDB
- [ ] Postman

_Con lo anterior en mente es importante mencionar que se recomienda la integración de un entorno virtual para el desarrollo de nuevas funcionalidades dentro de la API, ya que pudiera existir el caso en el que alguna instalación ajena dentro del equipo produzca inconvenientes con la integración de nuestro software._

**Comandos a ejecutar en la terminal:**
      
      > pip install virtualenv
      > python -m venv APImg
      > cd APImg/Scripts/activate
      > cd ../..
      > pip install Fastapi uvicorn pymongo


#### Requisitos Usuario 👨‍🦱

_Se hace caso omiso de este apartado puesto que no debería haber intervención alguna por parte de usuarios finales o terceros ajenos al desarrollo del proyecto._

<p align="right">
  (<a href="#requisitos-desarrollador">Requisitos Desarrollador</a>)
  (<a href="#requisitos-usuario">Requisitos Usuario</a>)
  (<a href="#intro">Inicio</a>)
</p>

### Instalación 🔧

_Con nuestro entorno virtual creado y en ejecución mencionado en el punto anterior podemos proceder a ejecutar nuestro proyecto con los siguientes comandos_

_**Dentro de la carpeta principal de la API ejecutar:**_

      > uvicorn app:app

_El comando anterior levantará nuestro servidor para comenzar a trabajar, sin embargo lo realizará con una configuración predeterminada y bastante deficiente para un constante desarrollo de nuevas funcionalidades e integraciones al sistema, por lo cual se recomienda utilizar la siguiente adición de parametros._

      > uvicorn app:app --reload

_Haciendo que nuestro servidor se reinicie cada que detecte algún cambio dentro de nuestro código de ruteo._
_Adicional a esto es posible adicionar mayor cantidad de parametros como el host, port, entre otros._

      > uvicorn app:app --reload --host: <param> --port: <param>

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Pruebas 🔩

_De manera adicional se incluiran archivos de la arquitectura y funcionamiento del sistema, así como un conjunto de datos que puede utilizar para realizar las pruebas pertinentes del sistema._

#### Pruebas Unitarias 👨‍💻

_El uso de pruebas unitarias dentro del proyecto nos permite detectar errores dentro de cada funcionalidad del sistema, son de gran ayuda a la hora de intentar agregar una nueva funcionalidad así como ahorrar tiempo al momento de testear el sistema._

```
Agregar instrucciones para la ejecución	de las pruebas unitarias
```

#### Pruebas de Integración 🔌

_El uso de pruebas de integración dentro del proyecto nos da la ventaja de poder identificar de manera rápida las conexiones fallidas entre este y más microservicios que componen al software así como la integración al backend principal._

```
Agregar instrucciones para la ejecución	de las pruebas unitarias
```

<p align="right">
  (<a href="#pruebas-software">Pruebas Software</a>)
  (<a href="#pruebas-hardware">Pruebas Hardware</a>)
  (<a href="#ecmo">Inicio</a>)
</p>

## Diagramas 📚

_A continuación se muestran los diagramas de funcionamiento general de la API_

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Despliegue 📦

_El despliegue se realiza de manera automatico con railway._

<p align="right">(<a href="#intro">Inicio</a>)</p>

## Construcción🛠️

_El diseño de esta API se realizo en base al siguiente conjunto de tecnologias._

* [Python 3.10.6](https://www.python.org/) ➡ Lenguaje utilizado
* [FastAPI](https://maven.apache.org/) ➡ Desarrollo del Servidor
* [Uvicorn](https://rometools.github.io/rome/) ➡ Manejo de peticiones HTTP

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/ThunderGer23/APImg)

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/ThunderGer23/APImg).

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Autores 🖋

* **ThunderGer** - *Trabajo Inicial* - [ThunderGer23](https://github.com/ThunderGer23)
* **R2D2** - *Documentación* - [R2D2](https://github.com/ArturoEmmanuelToledoAguado)

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Licencia 📄

Este proyecto está bajo la Licencia "*MIT*" - mira el archivo [LICENSE](LICENSE) para detalles

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Expresiones de Gratitud 🎁

**ThunderGer**
<div align="left">
    <table border="0">  
      <tbody>
        <tr>
          <td>
            <img height="100" src="/lib/assets/avatars/ThunderGer.png" width="100"/>
          </td>
          <th>
            <li>
              Algun agradecimiento quer agregare despues
            </li>
          </th>
        </tr>
      </tbody>
    </table>
</div>

<p align="right">(<a href="#intro">Inicio</a>)</p>


**R2D2**

* Algun agradecimiento que agregare despues x2 :v

---