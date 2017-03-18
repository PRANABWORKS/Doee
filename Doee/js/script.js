$("#button").click(function(){
    $.get("https://bilaw.al/api/v1/me.json", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
});

$("#registerForm").submit(function(e) {

    //var url = "path/to/your/script.php"; // the script where you handle the form input.

    $.ajax({
           type: "POST",
           url: "http://10.99.155.104:5000/register",
		   crossDomain : true,
           data: $("#registerForm").serialize(), // serializes the form's elements.
           success: function(data)
           {
               alert(data); // show response from the php script.
			   window.location.href = 'login.html';
           }
         });

    e.preventDefault(); // avoid to execute the actual submit of the form.
});

$("#loginForm").submit(function(e) {

    //var url = "path/to/your/script.php"; // the script where you handle the form input.

    $.ajax({
           type: "POST",
           url: "http://10.99.155.104:5000/loginEmployee",
		   crossDomain : true,
           data: $("#loginForm").serialize(), // serializes the form's elements.
           success: function(data)
           {
			   var parsed = JSON.parse(data);
               alert("Welcome " + parsed.firstname + " " + parsed.lastname); // show response from the php script.
			   window.location.href = 'login.html';
           }
         });

    e.preventDefault(); // avoid to execute the actual submit of the form.
});