$(document).ready(function(){
	$(".editgr, .editst").hide();

	function date(y, m, d, dval){
		//if month is February and year is leap, then hide day 30, day 31,  and show 29
		if(m == 2 & y % 4 === 0 && y % 100 !== 0 || y % 400 === 0){
				
			$(d[28]).show();
			$(d[29]).hide();
			$(d[30]).hide();
			//if day > 29, then set day to 29
			if($(dval).val() > 29){
				$(dval).val('29')
			}
		}
	//if month is February, then hide day 31, day 30, day 29
		else if(m == 2){
			$(d[28]).hide();
			$(d[29]).hide();
			$(d[30]).hide();
			//if day > 28, then set day to 28
			if($(dval).val() > 28){
				$(dval).val('28')
			}
		}
	// if month is April, June, September, or November, then hide day 31
		else if(m == 4 | m == 6 | m == 9 | m == 11){
			$(d[28]).show();
			$(d[29]).show();
			$(d[30]).hide();
			//if day > 30, then set day to 30
			if($(dval).val() > 30){
				$(dval).val('30')
			}
		}
		else {
			$(d[28]).show();
			$(d[29]).show();
			$(d[30]).show();
		}
	};


	$('#id_date_year, #id_date_month').change(function(){
		var y = $('#id_date_year').val()
		var m = $('#id_date_month').val()
		var d = $('#id_date_day').children()
		var dval = $('#id_date_day')
		console.log(y, m, d, dval)
		date(y, m, d, dval)		
	})

	// group editing
	function editgr(curr_id, json){

		$(".editst").hide();// hide student editting form
		var redgroup
		for (i = 0; i < $('.redgroup').length; i++){
			if ($('.redgroup:eq(' + i + ')').val() == curr_id){
				redgroup = $('.redgroup:eq(' + i + ')')
			}
		}

		redgroup.next().after($('.editgr'));// insert group editing form
		redgroup.siblings('.editgr').children('.mainstudent').html('');
		for (x in json){
			if (json[x].group == redgroup.val()){
				redgroup.siblings('.editgr').children('.mainstudent').append('<option>' + json[x].name + '</option>');
			}	
		}
		// set the initial values to the current values
		redgroup.siblings('.editgr').children('.mainstudent').val(redgroup.prev().val())
		redgroup.siblings('.editgr').children('.mainstudent').prev().val(redgroup.prev().prev().prev().html())
		redgroup.siblings('.editgr').show()
		$('.erroreditgr').html('')

		$('.redactgroup').click(function(){
			console.log($(this).siblings('input').val())
			var check = $(this).siblings('input').val()
			// validation
			if (check.match(/^([a-zA-Zа-яА-Я0-9]+)([ ]*|[-]?)([a-zA-Zа-яА-Я0-9]+)$/i) == null){
				$('.erroreditgr').html('Please, write only letters and digits, \
				only one hyphenation. Something like "Group-32", "33 MM", "92f5gf9d4f" etc')
			}
			else{	
				$('.erroreditgr').html('')
				var its = $(this).parent()
				$.ajax({
					url: 'http://127.0.0.1:8000/groupsAPI/' + its.prev().prev().val(),
					type: 'PUT',
					dataType: 'json',
					data: {
						'groupname': $(this).siblings('input').val(),
						'mainstudent': $(this).siblings('select').val(),
					},
					success: function(json){
						its.prev().prev().prev().prev().prev().html(json.groupname)
						its.hide()
					},
				})
			}
		})
	}
	// group deleting
	function delgr(curr_id, current){

		$.ajax({
			url: 'http://127.0.0.1:8000/groupsAPI/' + curr_id,
			type: 'DELETE',
			success: function(){
				var it = $('.delgroup:eq(' + current + ')')
				it.siblings('.editgr').remove()
				it.prev().remove()
				it.prev().remove()
				it.next().remove()
				it.next().remove()
				it.next().remove()
				it.siblings('.editst').remove()
				it.remove()
				
				for (i in $('.inp')){

					if ($('.inp:eq(' + i + ')').html() == it.val()){
						$('.inp:eq(' + i + ')').prev().prev().remove()
						$('.inp:eq(' + i + ')').prev().prev().remove()
						$('.inp:eq(' + i + ')').prev().prev().remove()
						$('.inp:eq(' + i + ')').prev().remove()

					}
				}
				
				function rem(it){
					for (i in $('.inp')){
						if ($('.inp:eq(' + i + ')').html() == it.val()){
							$('.inp:eq(' + i + ')').remove()
						}
					}
				}
				rem(it)
				rem(it)
				rem(it)
				rem(it)
			}
		})
	}
	// student editing
	function redst(value){
		$('.err_edit_st').html('')
		var it 
		for (i = 0; i < $('.redstud').length; i++){
			if($('.redstud:eq(' + i + ')').next().next().next().html() == value){

				it = $('.redstud:eq(' + i + ')')
			}
		}
		$(".editgr").hide()// hide group editing form
		$('.delstud').show()
		$('.redstud').show()
		it.prev().hide()
		it.hide()
		it.next().after($('.editst'));// insert student edtiting form
		it.siblings(".editst").show();
		var currgroup = it.next().next().next().html()
		var thisinf = it.prev().prev().html().split('; ')
		var day = thisinf[2].split('-')[2]
		if(day[0] == 0){
			day = day[1]
		}
		//set initial values to current values
		it.siblings(".editst").children('#id_name').val(thisinf[0])
		it.siblings(".editst").children('#id_num').val(thisinf[1])
		it.siblings(".editst").children('#id_group').val(currgroup)
		it.siblings(".editst").children('#id_date_month').val(thisinf[2].split('-')[1])
		it.siblings(".editst").children('#id_date_day').val(day)
		it.siblings(".editst").children('#id_date_year').val(thisinf[2].split('-')[0])

		var y = it.siblings(".editst").children('#id_date_year').val()
		var m = it.siblings(".editst").children('#id_date_month').val()
		var d = it.siblings(".editst").children('#id_date_day').children()
		var dval = it.siblings(".editst").children('#id_date_day')

		date(y, m, d, dval)

		$('#id_date_year, #id_date_month').change(function(){
			var y = $(this).siblings('#id_date_year').val();
			var m = $(this).siblings('#id_date_month').val();
			if (y == undefined){
				y = $(this).val()
			}
			if (m == undefined){
				m = $(this).val()
			}
			var d = $(this).siblings('#id_date_day').children();
			var dval = $(this).siblings('#id_date_day');
			date(y, m, d, dval)
		})
	
		$('.redactstudent').click(function(){
			$('.delstud').show()
			$('.redstud').show()
			var it = $(this).parent()
			var month = $(this).siblings('#id_date_month').val()
			var day = $(this).siblings('#id_date_day').val()
			var year = $(this).siblings('#id_date_year').val()
			var checkname = it.children('#id_name').val()
			// validation
			if (checkname.match(/^(([a-zA-Zа-яА-Я]+)([ ]*|[-]?)([a-zA-Zа-яА-Я]+))*$/i) == null){
				$('.err_edit_st').html('Please, write only letters and single hyphenations. Something like \
			"Name Surname", "Name Surname-Surname", "Name MiddleName Surname" etc')
			}
			else{
				$('.err_edit_st').html('')
				$.ajax({
					url: 'http://127.0.0.1:8000/studentsAPI/' + it.next().next().html(),
					type: 'PUT',
					dataType: 'json',
					data:{
						'name': $(this).siblings('#id_name').val(),
						'num': $(this).siblings('#id_num').val(),
						'group': $(this).siblings('#id_group').val(),
						'date': year + '-' + month + '-' + day,
					},
					
					success: function(json){
						if (it.next().html() != json.group){
							for (i = 0; i < $('.delgroup').length; i++){
								// if the student is edited and his group has been changed, then insert the student to the his new group
								if ($('.delgroup:eq(' + i + ')').val() == json.group){
									$('.redgroup:eq(' + i + ')').next().after(it.parent())
								}
							}
							}
						
						it.prev().prev().prev().prev().html(json.name + '; ' + json.num + '; ' + json.date)
						it.next().html(json.group)
						it.hide()
					}
				})
			}
		})
	}

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	//  group adding
	$('.addinggroup').click(function(){
		var check = $(this).siblings('#id_groupname').val()
		//validation
		if (check.match(/^([a-zA-Zа-яА-Я0-9]+)([ ]*|[-]?)([a-zA-Zа-яА-Я0-9]+)$/i) == null){
			$('.erroraddgr').html('Please, write only letters and digits, \
			only one hyphenation. Something like "Group-32", "33 MM", "92f5gf9d4f" etc')
		}		
		else {	
			$('.erroraddgr').html('')
			$.ajax({
				url: 'http://127.0.0.1:8000/groupsAPI/',
				type: 'POST',
				dataType: 'json',
				data: {
					'groupname': $(this).siblings('#id_groupname').val(),
				},
				success: function(data){
					
					$('.add_st select:eq(0)').append('<option class="added" value="' + data.id + '" >' + data.groupname + '</option>')
					$('.editst select:eq(0)').append('<option class="added" value="' + data.id + '" >' + data.groupname + '</option>')
					$('.ul_gr').append('<br><li class="line"></li>')
					$('.ul_gr').append('<button class="delgroup" \
						 alt="Delete"></button><button class="main" style="display: none">\
						 </button><button class="redgroup" alt="Redact"></button>\
						<br class="br">')
					
					var eq = $('.line').length -1
					$('.line:eq(' + eq + ')').html(data.groupname)
					$('.delgroup:eq(' + eq + ')').val(data.id)
					$('.redgroup:eq(' + eq + ')').val(data.id)
					$('.main:eq(' + eq + ')').val(data.mainstudent)
					$('.added:eq(' + eq + ')').val(data.id)
					var listgroups = ''
					listgroups += data.id  + ','
					var array = listgroups.split(',')
					delete array[5]	
					// group deleting
					$('.delgroup').click(function(){
						var current
						for (i = 0; i < $('.delgroup').length; i++){
							if($('.delgroup:eq(' + i + ')').val() == $(this).val()){
								current = i
							}
						}
						var curr_id = $(this).val()
						delgr(curr_id, current)
					})
					$.ajax({
						url: 'http://127.0.0.1:8000/studentsAPI/',
						type: 'GET',
						dataType: 'json',
						success: function(json){
							$(".redgroup").click(function(){
								var curr_id = $(this).val()
								editgr(curr_id, json)
							})
						}
					});
						
				}
			})
		}
	})
	
	$.ajax({
		url: 'http://127.0.0.1:8000/groupsAPI/',
		type: 'GET',
		dataType: 'json',
		success: function (data){
			var listgroups = '';
			
			for (i = 0; i < data.length; i++){
				var eq = i + 1
				$('.ul_gr').append('<br><li class="line"></li>')// loading list of groups
				$('li:eq(' + eq + ')').html(data[i].groupname)
				$('.ul_gr').append('<button class="delgroup" \
					 alt="Delete"></button><button class="main" style="display: none">\
					 </button><button class="redgroup" alt="Redact"></button>\
					<br class="br">')
				$('.delgroup:eq(' + i + ')').val(data[i].id)
				$('.redgroup:eq(' + i + ')').val(data[i].id)
				$('.main:eq(' + eq + ')').val(data[i].mainstudent)
				
				listgroups += data[i].id  + ','
				array = listgroups.split(',')
				delete array[array.length - 1]	
			};
	// student adding
	$('.addingstudent').click(function (){
		var month = $(this).siblings('#id_date_month').val()
		var day = $(this).siblings('#id_date_day').val()
		var year = $(this).siblings('#id_date_year').val()
		var checkname = $(this).siblings('#id_name').val()
		var gr = $(this).siblings('#id_group').val()
		console.log(gr)
		// validation
		if (checkname.match(/^(([a-zA-Zа-яА-Я]+)([ ]*|[-]?)([a-zA-Zа-яА-Я]+))*$/i) == null){
			$('.erroraddst').html('Please, write only letters and single hyphenations. Something like \
		"Name Surname", "Name Surname-Surname", "Name MiddleName Surname" etc')
		}
		else{
			$('.erroraddst').html('')
			$.ajax({
				url: 'http://127.0.0.1:8000/studentsAPI/',
				type: 'POST',
				dataType: 'json',
				data: {
					'name': $(this).siblings('#id_name').val(),
					'num': $(this).siblings('#id_num').val(),
					'group': $(this).siblings('#id_group').val(),
					'date': year + '-' + month + '-' + day,
				},
				success: function(data){
					listgroups = ''
					for (i = 0; i < $('.delgroup').length; i++){
						 listgroups += $('.delgroup:eq(' + i + ')').val() + ','
					}
					array = listgroups.split(',')
					delete array[array.length - 1]
					
					var g = '' + gr
					$('.br:eq(' + array.indexOf(g) + ')').after('<div class=".divstud"><li \
						class="sline">' + data.name + '; ' + data.num + '; ' + data.date + '</li> \
						<button class="delstud" alt="Delete"></button><button \
					class="redstud" alt="Redact"></button><br class="brr"><button class="inp" style="display: none">' + gr + '</button> \
						<button class="idstud" style="display: none">' + data.id + '</button></div>')
					$('.delstud').click(function(){
						var it = $(this)
						$.ajax({
							url: 'http://127.0.0.1:8000/studentsAPI/' + $(this).next().next().next().next().html(),
							type: 'DELETE',
							success: function(){
								it.parent().remove()
							}
						})
					})	
					$(".redstud").click(function(){
						$(".editgr").hide()
						$(this).prev().hide()
						var value = $(this).next().next().next().html()
						redst(value)
					})
				},			
			})
		}	
	})

	$.ajax({
		url: 'http://127.0.0.1:8000/studentsAPI/',
		type: 'GET',
		dataType: 'json',
		success: function(json){
			$(".redgroup").click(function(){
				var curr_id = $(this).val()
				editgr(curr_id, json)
			})
		}
	});
			
	$.ajax({
		url: 'http://127.0.0.1:8000/studentsAPI/',
		type: 'GET',
		dataType: 'json',
		success: function(data){
			// loading list of the students
			for (x in data){
				var g = '' + data[x].group
				$('.br:eq(' + array.indexOf(g) + ')').after('<div class=".divstud"><li \
					class="sline">' + data[x].name + '; ' + data[x].num + '; ' + data[x].date + '</li> \
					<button class="inp" style="display: none">' + data[x].group + '</button> \
					<button class="idstud" style="display: none">' + data[x].id + '</button>')
			}
			$('.sline').after('<button class="delstud" \
			 alt="Delete"></button><button \
			class="redstud" alt="Redact"></button><br class="brr"></div>')
		},			
	})

	$.ajax({
		url: 'http://127.0.0.1:8000/studentsAPI/',
		type: 'GET',
		dataType: 'json',
		success: function(json){
			$('.delstud').click(function(){
				var it = $(this)
				$.ajax({
					url: 'http://127.0.0.1:8000/studentsAPI/' + $(this).next().next().next().next().html(),
					type: 'DELETE',
					success: function(){
						it.parent().remove()
						
					}
				
				})
			})	
			$(".redstud").click(function(){
				var value = $(this).next().next().next().html()
				redst(value)
			})
	}	
	});

	$('.delgroup').click(function(){
		var current
		for (i = 0; i < $('.delgroup').length; i++){
			if($('.delgroup:eq(' + i + ')').val() == $(this).val()){
				current = i
			}
		}
		var curr_id = $(this).val()
		delgr(curr_id, current)
	})
	
		}
	})
		
})