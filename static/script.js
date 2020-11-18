//TODO: Try to get rid of jQuery

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
	result['process'] = output;
	console.log(result);

 
	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
 	const request = new Request(
	    '/upload_image',
	    {headers: {'X-CSRFToken': csrftoken}}
	);
	fetch(request, {
	    method: 'POST',
	    mode: 'same-origin',  // Do not send CSRF token to another domain.
	    body: JSON.stringify(result)
	}).then(function(response) {
	    return response.json()
	}).then(function(json) {
		processed_image_url = json.processed_image_url
		// TODO: Instead of redirecting, choose what you want to do
		window.location = processed_image_url
	})


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
   result['base64_image'] = dataUrl;
});
