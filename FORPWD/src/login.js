function myFunction(inputElement){
		window.location.href="homepage.html";
	
}

function setFormMessage(formElement, type, message) {
	const messageELement = formElement.querySelector(".form__message");

	messageELement.textContent = message;
	messageELement.classList.remove("form__message--success", "form__message--error");
	messageELement.classList.add('form__message--$(type)');	
}
function setInputError(inputElement,message){
	inputElement.classList.add("form__input-error");
	inputElement.parentElement.querySelector(".inputErrormsg").textContent = message;
}

function clearInputError(inputElement){
	inputElement.classList.remove("form__input-error");
	inputElement.parentElement.querySelector(".inputErrormsg").textContent = "";
}


document.addEventListener("DOMContentLoaded", () => { 
	const loginForm = document.querySelector("#login");
	const createAccountForm = document.querySelector("#createAccount");

	document.querySelector("#linkCreateAccount").addEventListener("click", e => {
		e.preventDefault();
		loginForm.classList.add("form--hiden");
		createAccountForm.classList.remove("form--hiden");
	});

	document.querySelector("#linkLogin").addEventListener("click", e => {
		e.preventDefault();
		loginForm.classList.remove("form--hiden");
		createAccountForm.classList.add("form--hiden");
	});

	loginForm.addEventListener("button", e => {
		e.preventDefault();

		//Perform you AJAX/Fetch loginForm


		setFormMessage(loginForm, "error","Invalid username/password combination");
	});

	document.querySelectorAll(".form__input").forEach(inputElement => {
		inputElement.addEventListener("blur", e => {
			if(e.target.id === "signupUsername" && e.target.value.length > 0 && e.target.value.length < 8) {
				setInputError(inputElement, "Username must be at least 8 characters");
			}
		});

		inputElement.addEventListener("input", e => {
			clearInputError(inputElement);
		});
	});
});

