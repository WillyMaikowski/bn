<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<?php  if( $require_base ) {  ?>
	<base href="http://datos.bn.cl/">
<?php  }  ?>
	<link rel="stylesheet" href="d/css/bootstrap.min.css">
	<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
	<link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
	<link href="http://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">
	<link rel="stylesheet" href="d/css/style.css">
</head>
<body id="page-top" class="index">
	<nav class="navbar navbar-default navbar-fixed-top">
		<div class="container">
			<div class="navbar-header page-scroll">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="<?php print $require_base ? '/' : '#page-top'; ?>">BNLOD</a>
			</div>
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<ul class="nav navbar-nav navbar-right">
					<li class="hidden"><a href="#page-top"></a></li>
					<li class="page-scroll"><a href="sparql">Endpoint</a></li>
<?php  if( ! $require_base ) {  ?>
					<li class="page-scroll"><a href="#examples">Ejemplos</a></li>
					<li class="page-scroll"><a href="#tutorial">Tutorial</a></li>
					<li class="page-scroll"><a href="#about">Acerca</a></li>
<?php  }  ?>
				</ul>
			</div>
		</div>
	</nav>
