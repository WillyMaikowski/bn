<header>
	<div class="container">
  	<h4 class="text-uppercase">/recurso/<?php print $tipo; ?></h4>
  	<h2><?php print $nombre?$nombre:$id; ?></h2>
	<p>
		<a href="<?php print $url; ?>?format=application%2Fsparql-results%2Bjson" class="label label-default">json</a>
		<a href="<?php print $url; ?>?format=text%2Fturtle" class="label label-default">ttl</a>
		<a href="<?php print $url; ?>?format=application%2Fsparql-results%2Bxml" class="label label-default">xml</a>
		<a href="<?php print $url; ?>?format=text%2Fcsv" class="label label-default">csv</a>
	</p>	
	</div>
</header>

<section class="success">
<div class="container">
  <div class="row">
    <div class="col-lg-12 text-center">
  		<h3>Triplas</h3>
		</div>
	</div>
  <div class="row">
    <div class="col-lg-6">
<?php  /*<p class=""><strong>Nombre: </strong><?php print $nombre; ?></p>*/  ?>
<?php  foreach( $res['results']['bindings'] as $v ) {  ?>
<?php  $test = ! $v['c'] || $v['c']['value'] == $url;  ?>
<?php  $c = $test ? $v['a'] : $v['c'];  ?>
				<p><strong><?php print $test?'<span class="glyphicon glyphicon-transfer"></span> ':''; ?><?php print $v['b']['value']; ?>:</strong><br/> <?php print $c['type']=='uri'?'<a href="'.$c['value'].'">'.$c['value'].'</a>':$c['value']; ?></p>
      <br/>
<?php  }  ?>
    </div>
  </div>
</div>
</section>
