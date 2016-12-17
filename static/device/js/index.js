/**
 * 
 */


function showError(errorHtml) {
	$("#alertArea").removeClass('alert-error alert-info alert-success')
			.addClass('alert-error');
	$("#alertContentArea").html(errorHtml);
	$("#alertArea").show();
}

function showInfo(infoHtml) {
	$("#alertArea").removeClass('alert-error alert-info alert-success')
			.addClass('alert-info');
	$("#alertContentArea").html(infoHtml);
	$("#alertArea").show();
}

function ready() {
	var dt = new Date();
	var month = dt.getMonth()+1;
	var day = dt.getDate();
	var year = dt.getFullYear();
	var week = dt.getDay();
	
	var head = '<thead><tr><th width="6%">#</th>';
	for (var i=0; i<7; i++) {
		head += '<th width="10%">일</th>';
	}
	head += '</tr></thead>';
//    <th width="10%">일</th>\
//    <th width="10%">월</th>\
//    <th width="10%">화</th>\
//    <th width="10%">수</th>\
//    <th width="10%">목</th>\
//    <th width="10%">금</th>\
//    <th width="10%">토</th>\
//  </tr>\
//</thead>';
	
	$("#timetable").prepend(head);
}


// Specialized function for checking error responses; it's needed to work around
// bugs in the
// current version of the DevAppServer
function checkErrorResponse(rawResult) {
	// Generally, !result should never occur. It's a bug with the DevAppServer.
	// It will be fixed
	// in a forthcoming version of App Engine.
	try {
		// This is some special exception-handling code to deal with the
		// DevAppServer not
		// handling empty (void responses) from an endpoint method in App
		// Engine 1.7.5.
		var result = JSON.parse(rawResult);

		if (result.error) {
			// This is really what should happen; if there's an error, a
			// result.error object will
			// exist
			var safeErrorHtml = $('<div/>').text(result.error.message).html();
			return {
				isError : true,
				errorMessage : safeErrorHtml
			};
		} else if (result[0] && result[0].error) {
			// This is yet another hack; the DevAppServer incorrectly returns an
			// array of error
			// responses in the case where the endpoint method throws an
			// app-level
			// exception.
			// Again, this will be fixed in a forthcoming version of App Engine.
			var safeErrorHtml = $('<div/>').text(result[0].error.message)
					.html();
			return {
				isError : true,
				errorMessage : safeErrorHtml
			};
		}

		return {
			isError : false,
			data : result.result
		};
	} catch (err) {
		// This is a spurious error. Return true.
		if (rawResult
				.indexOf("Error 400 Failed to parse JSON request: Unexpected character") != -1) {
			return {
				isError : false
			};
		} else {
			if (rawResult == "") {
				// Empty result; perhaps we're disconnected?
				return {
					isError : true,
					errorMessage : "No response from server! Is it up and running?"
				};

			} else {
				// Unknown error; this shouldn't really happen
				var safeErrorHtml = $('<div/>').text(rawResult).html();
				return {
					isError : true,
					errorMessage : safeErrorHtml
				};
			}
		}
	}

}

function startCommand() {
	$(this).addClass('disabled')
	$(this).text('시작중...') 
	$.get('/start', '', function(data) {
		handleMessageResponse(data);
	});
}

function stopCommand() {
	$.get('/stop', '', function(data) {
		handleMessageResponse(data);
	});
}

function handleMessageResponse(dataRaw) {
	var result = checkErrorResponse(dataRaw);
	if (!result.isError) {
		window.location.href = "/";
//		showInfo(result.message);
	} else {
		showError(result.errorMessage);
	}
}

String.prototype.trim = function() {
	return this.replace(/(^\s*)|(\s*$)/gi, "");
}