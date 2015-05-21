$(document).ready( function(){
	$("#addlistform").on('submit', function(event){
		event.preventDefault();
		var formData = {};//fill this
		var inputs = this.getElementsByTagName("input");
		var name, value
		for(var i=0;i<inputs.length-1;i++){
			name = inputs[i].name;
			value = inputs[i].value;
			formData[name] = value;
		}
		var ajaxoptions = {
			type: 'POST',
			url: this.action,
			data: formData
		};
		
		$.ajax(ajaxoptions).done(function(response){
			console.log(response);
		});
	});
});