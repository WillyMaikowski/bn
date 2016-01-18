<header>
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <div class="intro-text">
          <span class="name">Biblioteca Nacional</span>
          <span class="skills">Proyecto Linked Open Data</span>
        </div>
      </div>
    </div>
  </div>
</header>

<section class="success" id="examples">
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        <h2>Ejemplos</h2>
      </div>
    </div>
    <br/><br/>
    <div class="row">
      <div class="col-lg-3 col-lg-offset-2 text-center">
        <a href="recurso/tema/poesias_chilenas">
          <span class="fa-stack fa-lg fa-2x">
            <i class="fa fa-circle fa-stack-2x"></i>
            <i class="fa fa-files-o fa-stack-1x fa-inverse"></i>
          </span><br/>
          Tema
        </a>
      </div>
      <div class="col-lg-2 text-center">
        <a href="recurso/obra/antes_del_desorden">
          <span class="fa-stack fa-lg fa-2x">
            <i class="fa fa-circle fa-stack-2x"></i>
            <i class="fa fa-book fa-stack-1x fa-inverse"></i>
          </span><br/>
          Obra
        </a>
      </div>
      <div class="col-lg-3 text-center">
        <a href="recurso/persona/jorge_teillier">
          <span class="fa-stack fa-lg fa-2x">
            <i class="fa fa-circle fa-stack-2x"></i>
            <i class="fa fa-user fa-stack-1x fa-inverse"></i>
          </span><br/>
          Autor
        </a>
      </div>
    </div>
    <br/>
    <div class="row">
      <div class="col-lg-8 col-lg-offset-2"><p>A traves de los anteriores links se puede acceder a la información de un recurso en particular. Se observa que estan interconectados existiendo triplas de referencia entre ellos.</p></div>
    </div>
  </div>
</section>

<section class="success" id="tutorial">
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        <h2>Tutorial</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4 col-lg-offset-2">
        <p>Este sitio posee una conexión con un servidor con la herramienta Virtuoso. Este combina utilidades para el manejo de base de datos relacionales, en forma de grafo o basada en documentos para permitir la conexion con una aplicación web.</p>
      </div>
      <div class="col-lg-4">
        <p>Para su uso puede hacer click en la opcion "Endpoint" y a traves del lenguaje de consulta SPARQL puede obtener triplas que detallan los datos y sus conexiones de las bases de Biblioteca Nacional y Memoria Chilena.</p>
      </div>
      <div class="col-lg-8 col-lg-offset-2">
        <pre>select distinct ?a ?b ?c where { <br/> ?a ?b ?c .<br/> filter regex( str( ?a ), "^http://datos.bn.cl" )<br/>}<br/>limit 100</pre>
      </div>
      <div class="col-lg-8 col-lg-offset-2">
        <p>La anterior consulta realiza una busqueda de todas las triplas en el sistema cuyo sujeto comience con una url asociada a este sitio (datos.bn.cl).</p>
      </div>
    </div>
  </div>
</section>


<section class="success" id="about">
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        <h2>Acerca</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4 col-lg-offset-2">
        <p><a href="datos.bn.cl">datos.bn.cl</a> consiste en un proyecto exploratorio que busca unificar los metadatos de las distintas fuentes de datos que posee y que es responsable Biblioteca Nacional.</p>
      </div>
      <div class="col-lg-4">
        <p>Linked Open Data obedece a un movimiento internacional que busca disponibilizar datos de manera interconectada siendo, de esta manera, de mayor utilidad permitiendo incluso formatos que puedan ser leidos automaticamente.</p>
      </div>
    </div>
  </div>
</section>
