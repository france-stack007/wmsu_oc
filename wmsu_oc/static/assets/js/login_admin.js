$(document).ready(function()
{

	
	
	$("#frmLogin_administrator").submit(function()
	{
		
		//Remove all the class add the messagebox classes and start fading
		$("#login-indicator-msg").addClass('login-msg-process').text('Validating...').fadeIn(1000);
		$("#indicator-msg").addClass('indicator-msg');
		//Check the "username" if exists or not from ajax
		$.post("login-process.php",{ email_add:$('#email_add').val(),pass_word:$('#pass_word').val()} ,function(data)
        {
		  if(data=='yes') //if correct login detail
		  {
		  	$("#login-indicator-msg").fadeTo(200,0.1,function()  { //start fading the messagebox
			  	//Add message and change the class of the box and start fading
			  	$(this).html('Logging in...').addClass('login-msg-valid').fadeTo(900,1,
              	function() { 
			  		document.location='vendor.php';
			  	});			  
			});
		  } else {
			$("#login-indicator-msg").fadeTo(2000,0.1,function() { //start fading the messagebox
				$("#login-indicator-msg").removeClass()
			  	//Add message and change the class of the box and start fading
			  	$(this).html('<img src="/onlinecanteen/images/icon/warning-alt-1.svg" width="50px" height="50px"> &nbsp;&nbsp;&nbsp; <strong> Login Failed!</strong>').addClass('login-msg-error').fadeTo(900,1);
				$("#indicator-msg").removeClass('indicator-msg');
			});		
          }
	
        });		
		
 		return false; //Not to post the form physically
	});

});