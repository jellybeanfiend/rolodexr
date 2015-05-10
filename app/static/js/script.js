$(document).ready(function(){
	$('#filter').on('keyup', function(){
		filter = this.value
		$('.contact-card').each(function(){
			if(!$(this).text().match(filter))
				$(this).hide();
			else
				$(this).show();
		})
	})

	$('.dropdown-menu li a').on('click', function(){
		var type = $(this).data('sort');
		switch(type){
			case 'first':
				$('.contact-card').sort(sort_first).appendTo('.contacts');
				break;
			case 'last':
				$('.contact-card').sort(sort_last).appendTo('.contacts');
				break;
		}
	})

	function sort_first(elem1,elem2){
		return ($(elem2).find('h3').text().toLowerCase()) < ($(elem1).find('h3').text().toLowerCase()) ? 1 : -1;
	}

	function sort_last(elem1,elem2){
		return get_last_name(elem2) < get_last_name(elem1) ? 1 : -1;
	}

	function get_last_name(elem){
		return $(elem).find('h3').text().toLowerCase().split(" ").pop();
	}


})