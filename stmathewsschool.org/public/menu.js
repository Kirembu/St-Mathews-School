$(document).ready(function() {
	$(".details").hide();
	$("#history").show();
});

function sideMenuClick(detailId) {
	$(".details").hide();
	$("#" + detailId).show();
	$(".side-menu").find('.selected').removeClass('selected');
	$("#btn-" + detailId).addClass('selected');
}