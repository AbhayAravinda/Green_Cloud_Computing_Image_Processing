function readURL(input) 
{
	if (input.files && input.files[0]) 
	{
		var reader = new FileReader();

		reader.onload = function (e) 
		{
			$('#image')
			.attr('src', e.target.result);
		};
		reader.readAsDataURL(input.files[0]);
	}
	var x = document.getElementById("image");
	x.style.display = "block";

	var y = document.getElementById("para");
	y.style.display="none";
}
