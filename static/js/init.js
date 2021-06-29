$(document).ready(function () {
        
    
    $('#put-button').click(function () {
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/login',
			data: $('form').serialize(),
			type: 'PUT',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	}); 
	
	$('#delete-button').click(function () {
		$.ajax({url: "/login", method: 'DELETE', success: function(result){
			$("#div1").html(result);
		  }});
	}); 
	
	 $('#post-button').click(function () {
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/login',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	}); 
	
	
	$('#logout-button').click(function () {
		$.ajax({
			url: '/logout',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	}); 
	
	/*$('#weather-button').click(function () {
		$.ajax({
			url: '/weather',
			success: function(response){
				console.log(response);
				$('#icon').html('<img src="' + 'http://openweathermap.org/img/w/' + response['icon'] + '.png' + '"/>')
				$('#city').html('City: ' + response['city'])
				$('#description').html('Description: ' + response['description'])
				$('#temperature').html('Temperature: ' + response['temperature'] + ' F')
			},
			error: function(error){
				console.log(error);
			}
		});
	});*/ 

	
        
});

console.log("Name: Daniel Garcia");
console.log("Student #: 1022106");
console.log("To protect from sql injection: input validation, parameterized queries, stored procedures and firewall")


