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



//Hotkeys
document.addEventListener('keydown', function(event){
	key = event.key;
	drop_down = document.getElementById("id_option");
	file_upload = document.getElementById("myFile");
	submit_button = document.getElementById("submitButton");

	if(key=="1") drop_down.value=("grayscale");
	else if(key=="2") drop_down.value=("histogram");
	else if(key=="3") drop_down.value=("gaussian_blur");
	else if(key=="4") drop_down.value=("brightness_increase");
	else if(key=="5") drop_down.value=("brightness_decrease");
	else if(key=="6") drop_down.value=("color_inversion");
	else if(key=="7") drop_down.value=("negative_image");
	else if(key=="8") drop_down.value=("sepia");
	else if(key=="9") drop_down.value=("clahe");

	else if(key=="Insert") file_upload.click();
	else if(key=="S" || key=="s") submit_button.click();
});