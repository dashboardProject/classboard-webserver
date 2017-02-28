var event_array = [];

function groupDate(now) {
	var start = now.getDate() - now.getDay() +1;
	for (var ai=0; ai<6; ai++) {
		var start_day = start + ai;
		event_array[ai] = [];
			
		for (var tj in today_event) {
			var day = today_event[tj].start.split('T')[0].split('-')[2];
			if( start_day == day ) {
				event_array[ai].push(today_event[tj]);
			}
		}
	}
}

function initDate() {
	var now = new Date();
	var temp_date = new Date();

	groupDate(now);

	if (now.getDay() != 1) {
		temp_date.setDate(now.getDate() + (1 - now.getDay()));
	}
		
	for(var ai in event_array) {
		var event_date = temp_date.getFullYear() + '-'; 
		var current_month = temp_date.getMonth() + 1,
		    current_date = temp_date.getDate();

		if (current_month < 10) {
			current_month = '0' + current_month;
		}
		if (current_date < 10) {
			current_date = '0' + current_date;
		}

		console.log(temp_date.getDate(), ai);
		event_date += current_month + '-' + current_date;
		
		// ci : class_index
		for(var ci in event_array[ai]) {
			var start_time = 'T' + event_array[ai][ci].start.split('T')[1];
			var end_time = 'T' + event_array[ai][ci].end.split('T')[1];

			event_array[ai][ci].start = event_date + start_time;
			event_array[ai][ci].end = event_date + end_time;
		}

		temp_date.setDate(temp_date.getDate() + 1);
	}

	today_event = [];	
	for( var one_i in event_array ) {
		for( var two_i in event_array[one_i] ) {
			today_event.push(event_array[one_i][two_i]);
		}
	}
	
	now_date = now.getFullYear() + '-' + (now.getMonth() + 1) + '-' + now.getDate();
}

function checkClass(){
	var now = new Date();
	var total_minutes = now.getHours() * 60 + now.getMinutes();
	var inClass = false;	
	var day = now.getDay()-1;	

	if(day < 0) {
		document.getElementById("inClass").innerHTML = "빈강의실";
		document.getElementById("className").innerHTML = "";
//		document.getElementById("professor").innerHTML = "" 
		document.getElementById("classProgress").style.width = '0%';
		return;
	}

	for (var i in event_array[day]) {
		var class_start_time = event_array[day][i].start.split('T')[1];
		var class_end_time = event_array[day][i].end.split('T')[1];

		var class_start_minutes = Number(class_start_time.split(':')[0]) * 60 +
					  Number(class_start_time.split(':')[1]);

		var class_end_minutes = Number(class_end_time.split(':')[0]) * 60 +
					Number(class_end_time.split(':')[1]);

		console.log(total_minutes);
		console.log(class_start_minutes, class_end_minutes);
		if (total_minutes > class_start_minutes && total_minutes < class_end_minutes) {
			var progress = (total_minutes - class_start_minutes) / (class_end_minutes - class_start_minutes) * 100;
			document.getElementById("inClass").innerHTML = "강의중";
			document.getElementById("className").innerHTML = event_array[day][i].title.split('\n')[0];
//			document.getElementById("professor").innerHTML = event_array[day][i].title.split('\n')[1]; 
			document.getElementById("classProgress").style.width = progress + '%';
			$('#inClass').removeClass('label-primary');
			$('#inClass').addClass('label-danger');
			inClass = true;
			break;
		} 
	}
	if(!inClass) {
		document.getElementById("inClass").innerHTML = "빈강의실";
		document.getElementById("className").innerHTML = "";
//		document.getElementById("professor").innerHTML = "" 
		document.getElementById("classProgress").style.width = '0%';
		$('#inClass').removeClass('label-danger');
		$('#inClass').addClass('label-primary');
	}
}

var onClassChecker = false;
function dpTime(){
	var now = new Date();
	date = now.getFullYear() + "년 " + (now.getMonth()+1) + "월 " + now.getDate() + "일 "; 
	hours = now.getHours();
	minutes = now.getMinutes();
	seconds = now.getSeconds();
			 
	if (hours > 12){
		hours -= 12;
		ampm = "오후 ";
	}else{
		ampm = "오전 ";
	}
	if (hours < 10){
		hours = "0" + hours;
	}
	if (minutes < 10){
		minutes = "0" + minutes;
	}
	if (seconds < 10){
		seconds = "0" + seconds;
	}

	document.getElementById("dpDate").innerHTML = date;
	document.getElementById("dpTime").innerHTML = ampm + hours + ":" + minutes + ":" + seconds;

	if(!onClassChecker && seconds == "00") {
		console.log('checkClass() start');
		setInterval("checkClass()", 60000);
		onClassChecker = true;
	}
}

