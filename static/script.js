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

var result = {};

function final() { 
	selectElement =  
	document.querySelector('#imgUpload');
	output = selectElement.value; 
	result['effect'] = output;
	console.log(result);

    $.post('/upload-image/', result, function(response){
        if(response === 'success'){ alert('Yay!'); }
        else{ alert('Error! :('); }});
}

function getDataUrl(img)
{
   const canvas = document.createElement('canvas');
   const ctx = canvas.getContext('2d');
   canvas.height = img.naturalHeight;
   canvas.width = img.naturalWidth;
   ctx.drawImage(img, 0, 0);
   return canvas.toDataURL('image/jpeg');
}
const img = document.querySelector('#image');
img.addEventListener('load', function (event) {
   const dataUrl = getDataUrl(event.currentTarget);
   result['image'] = dataUrl;
});
