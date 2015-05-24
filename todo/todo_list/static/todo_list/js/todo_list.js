var token;
var activeListName
$(document).ready( function(){
	var activelist
	token = {
		name: "csrfmiddlewaretoken",
		value: $("[name='csrfmiddlewaretoken']")[0].value
	};
	$("#addlistform").on('submit', function(event){
		event.preventDefault();
		var formData = {};
		var inputs = this.getElementsByTagName("input");
		var name, value;
		for(var i=0;i<inputs.length-1;i++){
			formData[inputs[i].name] = inputs[i].value
		}
		var ajaxoptions = {
			type: 'POST',
			url: this.action,
			data: formData
		};
		
		$.ajax(ajaxoptions).success(function(response){
			reloadPage();
		});
	});
	$("#addtaskform").on('submit', function(event){
		event.preventDefault();
		var formData = {};//fill this
		var inputs = this.getElementsByTagName("input");
		var selects = this.getElementsByTagName("select");
		for(var i=0;i<inputs.length-1;i++){
			formData[inputs[i].name] = inputs[i].value;
			if(inputs[i].name === 'finished'){
				if(inputs[i].checked){
					formData[inputs[i].name] = true;
				}
				else{
					formData[inputs[i].name] = false;
				}
			}
		}
		for(var i=0;i<selects.length;i++){
			formData[selects[i].name] = selects[i].value;
		}
		var ajaxoptions = {
			type: 'POST',
			url: this.action,
			data: formData
		};
		$.ajax(ajaxoptions).success(function(response){
			loadList(activeListName)			
		}); 
	});
	
	
});

var loadList = function(name){
	if(!name){
		return
	}
	activeListName = name;
	sessionStorage.setItem('active', activeListName);
	$("#ActiveList").empty().append(document.createElement('p').appendChild(
		document.createTextNode("list: " + name) 
	))
	var checkbox, paragraph, text, button;	
	var data = {
		listname: name,
	};
	data[token.name] = token.value
	var ajaxoptions = {
		type: 'POST',
		url: '../getlist/',
		data: data,
	}
	$.ajax(ajaxoptions).done(function(response){;
		if(response[0].results !== "Nothing"){
			for(var i=0; i<response.length; i++){
				button = document.createElement('input');
				button.type = "button";				
				button.onclick = removeTask(response[i].id);
				button.value = "delete"
				checkbox = document.createElement('input');
				checkbox.type="checkbox";
				checkbox.name = response[i].id;
				checkbox.onclick = toggleDone;
				if(response[i].finished){
					checkbox.checked = true;
				}
				if(response[i].deadline === null){
					response[i].deadline = "No deadline."
				}
				else{
					response[i].deadline = "deadline: " + response[i].deadline
				}
				
				text = document.createTextNode(response[i].deadline + " task description:" + response[i].description);
				
				paragraph = document.createElement('p');
				paragraph.appendChild(button);
				paragraph.appendChild(checkbox)
				paragraph.appendChild(text);
				$("#ActiveList").append(paragraph);
			}
		}		
	});
	
};

var removeList = function(name){
	var data = {
		listname: name,
	};
	data[token.name] = token.value
	var ajaxoptions = {
		type: 'POST',
		url: '../removelist/',
		data: data,
	}
	$.ajax(ajaxoptions).success(function(response){
			reloadPage()			
	});
}

var removeTask = function(id){
	return function(){
		var data = {
			id: id,
		}
		data[token.name] = token.value
		var ajaxoptions = {
			type: 'POST',
			url: '../removetask/',
			data: data,
		}
		$.ajax(ajaxoptions).success(function(response){
			reloadPage();
		});
	}
}

var toggleDone = function(){
	var data = {
		id: this.name,
	};
	data[token.name] = token.value;
	var ajaxoptions = {
		type: 'POST',
		url: '../toggledone/',
		data: data,
	}

	$.ajax(ajaxoptions).error( function(e){alert("An error occured at the server, and your page may be out of sync. Please reload your page.");}) ;
};

var reloadPage= function(){
	sessionStorage.setItem('active', activeListName);
	window.location.reload();
}

window.onload = function(){
	activeListName = sessionStorage.getItem('active');
	loadList(activeListName)
}



















