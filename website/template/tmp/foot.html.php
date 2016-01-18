	<footer class="text-center">
		<div class="footer-above">
			<div class="container">
				<div class="row">
					<div class="footer-col col-md-4">
						<h3>Location</h3>
						<p>3481 Melrose Place<br>Beverly Hills, CA 90210</p>
					</div>
					<div class="footer-col col-md-4">
						<h3>Around the Web</h3>
						<ul class="list-inline">
							<li><a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-facebook"></i></a></li>
							<li><a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-google-plus"></i></a></li>
							<li><a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-twitter"></i></a></li>
							<li><a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-linkedin"></i></a></li>
							<li><a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-dribbble"></i></a></li>
						</ul>
					</div>
					<div class="footer-col col-md-4">
						<h3>About Freelancer</h3>
						<p>Freelance is a free to use, open source Bootstrap theme created by <a href="http://startbootstrap.com">Start Bootstrap</a>.</p>
					</div>
				</div>
			</div>
		</div>
		<div class="footer-below">
			<div class="container">
				<div class="row">
					<div class="col-lg-12">
						me @ 2016
					</div>
				</div>
			</div>
		</div>
	</footer>


	<script src="d/js/jquery-1.11.3.min.js "></script>
	<script src="d/js/bootstrap.min.js"></script>
	<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
	<script src="d/js/cbpAnimatedHeader.min.js"></script>
	<script>
$(	function() {
	$( 'body' ).on( 'click', '.page-scroll a', function( event ) {
		var $anchor = $( this );
		$( 'html, body' ).stop().animate( {
			scrollTop: $( $anchor.attr( 'href' ) ).offset().top
		}, 1500, 'easeInOutExpo' );
		event.preventDefault();
	} );
} );

$( 'body' ).scrollspy( {
	target: '.navbar-fixed-top'
} );

$( '.navbar-collapse ul li a' ).click( function() {
	$( '.navbar-toggle:visible' ).click();
} );
	</script>
</body>
</html>
