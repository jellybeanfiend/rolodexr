$(document).ready(function(){
	
	// Search contacts
	$('#filter').on('keyup', function(){
		filter = this.value.toLowerCase()
		$("[class*=contact-card]").each(function(){
			if($(this).text().toLowerCase().indexOf(filter) == -1)
				$(this).hide();
			else
				$(this).show();
		})
	})

	// Submit Login & register forms if validation passes
	$('.auth-submit').click(function(e){
		e.preventDefault()
		if(validate_form(this))
			$("form")[0].submit()
	})

	function validate_form(btn){
		var pass = true;
		// Verify each input contains text
		$(btn).closest('form').find('input[type="email"], input[type="password"]').each(function(){
			if($(this).val() == ""){
				$(this).closest('.form-group').find('p').removeClass('hidden')
				pass = false
			}
			else
				$(this).closest('.form-group').find('p').addClass('hidden')
		})
		// Verify passwords match for register form
		var passwords = $(btn).closest('form').find('input[type="password"]')
		if(passwords.length == 2){
			if($(passwords[0]).val() != $(passwords[1]).val()){
				$('.passwords').removeClass('hidden')
				pass = false
			}
			else{
				$('.passwords').addClass('hidden')
			}
		}

		return pass
	}

	// Handles image preview before upload
	var filelistener = function(){
		var label = $(this).parent();
		var file = this.files[0];
		if(file.type.match('image.*')){
			var reader = new FileReader()
			reader.onload = (function(theFile){
		            return function(e){
		            	$(label).css({'background-image': "url("+this.result+")", 'background-size': "cover"})
		            };
		        })(this);
		        reader.readAsDataURL(file);
		}
	}

	// Display image preview when an image is selected
	$(".uploadimg").on('change', filelistener)
	
	// Expand contact card when a user clicks on it
	$('.inactive').on('click', function(e){
		$(this).removeClass('inactive').addClass('active');
	})

	// Replace contact card h3 with an input box so the user can edit the contact's name
	$('#add-contact').one('click', function(){
		var h3 = $(this).find('h3');
		$(h3).html('<input type="text" class="name-input" name="name" placeholder="Name">');
	})

	// Edit contact card
	$('.edit-contact').one('click', function(event){
		event.preventDefault()
		event.stopPropagation()
		var form = $(this).closest('form');
		var h3 = $(form).find('h3');
		$(h3).html('<span class="glyphicon glyphicon-pencil pencil" aria-hidden="true"></span> <input type="text" value="'+$(h3).text().trim()+'" class="name-input" name="name" placeholder="Name">');
		var contactinfo = $(form).find('.contact-info')
		$(this).html('<span class="glyphicon glyphicon-ok" aria-hidden="true">save</span>')
		$(form).addClass('edit')
		$(contactinfo).find('input').each(function(){
			$(this).removeAttr('disabled')
		})
		$(this).click(saveContact)
	})

	// Save changes after an edit/add
	function saveContact(){
		event.stopPropagation()
		event.preventDefault();
		var form = $(this).closest('form')
		var name = $(form).find('.name-input')
		if(validateName(form)){
			$(form).submit();
		}
	}

	$('.save-contact').delegate('form', 'click', saveContact)

	// ensure a contact card at least has a name - it would look weird without one!
	function validateName(form){
		var name = $(form).find('.name-input')
		if($(name).val() == ""){
			if(!$(name).hasClass('danger-border'))
				$(name).addClass('danger-border').attr('placeholder', "Name is required")
			return false;
		}
		else
			return true;
	}

	$('.delete-contact').on('click', function(){
		event.stopPropagation()
		event.preventDefault()
		var contactcard = $(this).closest('.contact-card')
		var contactid = $(contactcard).data('id')
		console.log(contactid)
		$.post("/deletecontact", {id: contactid}, function(data){
			console.log(data)
			$(contactcard).fadeOut(function(){
				$(this).remove();
			});
		});
	})

	// Sorting
	$('.dropdown-menu li a').on('click', function(){
		var type = $(this).data('sort');
		console.log(type)
		switch(type){
			case 'first':
				$('.contact-card').sort(sort_first).appendTo('.contacts');
				break;
			case 'last':
				console.log('hi')
				$('.contact-card').sort(sort_last).appendTo('.contacts');
				break;
		}
	})

	// collapse contact card
	$('.collapse-contact').on('click', function(event){
		event.stopPropagation()
		event.preventDefault()
		$(this).closest('li').removeClass('active').addClass('inactive');
	})

	/** Sorting functions */
	function sort_first(elem1,elem2){
		return ($(elem2).find('h3').text().toLowerCase()) < ($(elem1).find('h3').text().toLowerCase()) ? 1 : -1;
	}

	function sort_last(elem1,elem2){
		console.log(get_last_name(elem2))
		return get_last_name(elem2) < get_last_name(elem1) ? 1 : -1;
	}

	function get_last_name(elem){
		return $(elem).find('h3').text().trim().toLowerCase().split(" ").pop();
	}


})