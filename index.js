const form = document.getElementById("form");

form.onsubmit = function(event) {
	event.preventDefault();
	formData = new FormData(form);
	xhr = new XMLHttpRequest();
	xhr.onreadstatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
		}
	xhr.open("POST", "submit.php");
	xhr.send(formData);
}
