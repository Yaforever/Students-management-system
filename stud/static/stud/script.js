$(document).ready(function(){
	$(".editstud, .redgroups").hide();
	$(".redgroup").click(function(){
		$(".redgroups, .editstud").hide();
		//show group edit form
		var redgroup = $(this).siblings("#" + this.id).show();
		redgroup.children().show();
		//set initial values to current values
		var gr = $(this).siblings("#" + 'r' + this.id).children().text();
		redgroup.children('#id_groupname').val(gr);
	});

	function date(y, m, d, dval){
		//if month is February and year is leap, then hide day 30, day 31,  and show 29
			if(m == 2 & y == 2016 | m == 2 & y == 2012 | m == 2 & y == 2008 | 
				m == 2 & y == 2004 | m == 2 & y == 2000 | m == 2 & y == 1996 | 
				m == 2 & y == 1992 | m == 2 & y == 1988 | m == 2 & y == 1984 | 
				m == 2 & y == 1980 | m == 2 & y == 1976 | m == 2 & y == 1972){
					
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

	$(".redstud").click(function(){
		$(".redgroups, .editstud").hide();
		//show student edit form
		var redstud = $(this).siblings(".editstud").show();
		var year = $(this).siblings(".editstud").children('#id_date_year');
		var month = $(this).siblings(".editstud").children('#id_date_month');
		var day = $(this).siblings(".editstud").children('#id_date_day');

		var sn = $(this).parent().siblings('#' + this.id).children('.sn').text();
		var su = $(this).parent().siblings('#' + this.id).children('.su').text();
		var sg = $(this).parent().siblings('#' + this.id).children('.sg').text();
		var sy = $(this).parent().siblings('#' + this.id).children('.sy').text();
		var sm = $(this).parent().siblings('#' + this.id).children('.sm').text();
		var sd = $(this).parent().siblings('#' + this.id).children('.sd').text();
		//set initial values to current values
		$(this).siblings(".editstud").children('#id_name').val(sn);
		$(this).siblings(".editstud").children('#id_num').val(su);
		$(this).siblings(".editstud").children('#id_group').val(sg);
		$(this).siblings(".editstud").children('#id_date_year').val(sy);
		$(this).siblings(".editstud").children('#id_date_month').val(sm);
		$(this).siblings(".editstud").children('#id_date_day').val(sd);

		var y = $(year).val();
		var m = $(month).val();
		var d = $(day).children();
		var dval = $(day);
		
		date(y, m, d, dval);

		$('#id_date_year, #id_date_month').change(function(){
			var y = $(year).val();
			var m = $(month).val();
			var d = $(day).children();
			var dval = $(day);

			date(y, m, d, dval);

		});
	});

	$('#id_date_year, #id_date_month').change(function(){
		var y = $('#id_date_year').val();
		var m = $('#id_date_month').val();
		var d = $('#id_date_day').children();
		var dval = $('#id_date_day');

		date(y, m, d, dval);

	});
});