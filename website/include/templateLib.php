<?php

function template( $file ) {
  if( ! is_file( $file ) ) halting_error( 'template no encontrado ( '.$file.' )' );

  global $template_dir;
  $template_dir = $file[0] == '/' ? dirname( $file ) : realpath( dirname( getcwd().'/'.$file ) );
  $compile_dir  = $template_dir.'/tmp';

  if( ! is_writeable( $compile_dir ) ) halting_error( '/tmp sin permisos de escritura' );

  $ftime = max( filemtime( $file ), filemtime( $_SERVER['SCRIPT_FILENAME'] ) );
  $comp = $compile_dir.'/'.basename( $file ).'.php';

  $file = file_get_contents( $file );
  $file = preg_replace( '/[ \t]*<!--/', "<!--", $file );
  $file = preg_replace( '/{{(.+)}}/U', '{UTIL::escapeHTML( $1 )}', $file );
  $file = preg_replace( '/{([^}\s][^}\r\n]*)\s*\|\|\s*(["\'].+["\'])}/', "<?php print $1 ? $1 : $2; ?>", $file );
  $file = preg_replace( '/{([^$}\s][^\$\)}\r\n]*)}/', "<?php print $$1; ?>", $file ); 
  $file = preg_replace( '/{([^}\s][^}\r\n]*)}/', "<?php print $1; ?>", $file );
  $file = str_replace( array( '<!--', '-->' ), array( '<?php ', ' ?>' ), $file );

  file_put_contents( $comp, $file );
  @chmod( $comp, 0664 );
  @touch( $comp, $ftime );

  return $comp;
}

function halting_error( $msg ) {
  /* Pagina que muestra mensahe de error */
  return $msg;
}

function print_a() {
  echo '<div style="width:100%;border:1px solid red;"><pre>';
  print_r( func_get_args() );
  echo '</pre></div>';
}

function wget( $url, $post = array() ) {
  $sess = isset( $_SESSION );
  if( $sess ) session_write_close();

  $cookies = array( session_name().'='.session_id() );
  foreach( $_COOKIE as $k => $v ) $cookies[] = $k.'='.$v;

  $ch = curl_init();
  curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1 );
  curl_setopt( $ch, CURLOPT_TIMEOUT,        100 );
  curl_setopt( $ch, CURLOPT_SSL_VERIFYPEER, 0 );
  curl_setopt( $ch, CURLOPT_SSL_VERIFYHOST, 0 );
  curl_setopt( $ch, CURLOPT_HEADER,         0 );
  curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 0 );
  curl_setopt( $ch, CURLOPT_COOKIE, implode( '; ', $cookies ) );
  curl_setopt( $ch, CURLOPT_URL, $url );
  if( ! empty( $post ) ) curl_setopt( $ch, CURLOPT_POSTFIELDS, $post );
  $res = curl_exec( $ch );
  curl_close( $ch );
  if( $sess ) session_start();

  return $res;
}
