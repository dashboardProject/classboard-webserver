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
	
	editableGrid = new EditableGrid("DemoGridJsData");
	editableGrid.load({"metadata": metadata, "data": data});
	editableGrid.renderGrid("tablecontent", "testgrid");
}


String.prototype.trim = function() {
	return this.replace(/(^\s*)|(\s*$)/gi, "");
}