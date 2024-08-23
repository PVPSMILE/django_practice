const regForms = document.forms.regForm;

const username = regForms.username;
const email = regForms.email;
const phone = regForms.phone;
const password = regForms.password;

console.log(username.value, phone.value, password.value);

username.addEventListener("input", (event) => {

    const lengthError = document.querySelector('.name-length-error')
    const alphabetError = document.querySelector('.name-alphabet-error')
    if (username.value.length > 3) {
        lengthError.style.display = 'none';
    } else {
        lengthError.style.display = 'block';
    }

    if (/^[a-zA-Z0-9]+$/.test(username.value)) {
        alphabetError.style.display = 'none';
    }else{
        alphabetError.style.display = 'block';
    }
});


email.addEventListener("input", (e) => {

    const chechValidEmail = email.value.split('@')
    const mailAlphabetError= document.querySelector('.mail-alphabet-error');
    
    if (/^[a-z0-9]+$/.test(chechValidEmail[0])){
        mailAlphabetError.style.display = 'none';
    
    } else {
        mailAlphabetError.style.display = 'block';
    }

    const dogValidError = document.querySelector('.dog-error')

    if (email.value.includes("@")){
        const mailValidError = document.querySelector('.incorect-mail')
        console.log(email.value.split('@'))

        if (chechValidEmail[1].length >=7){
            if (chechValidEmail[1] == 'gmail.com' || chechValidEmail[1] == 'ukr.net' ){
                mailValidError.style.display = 'none';
            }
            else {
                mailValidError.style.display = 'block';
            }
            dogValidError.style.display = 'none';
        }
    }
    else {
        dogValidError.style.display = 'block';
    }
    
})
phone.addEventListener('input', (event) => {
    const phoneError = document.querySelector('.phone-contryCode-error');
    const firstThreeChars = phone.value.substring(0, 3);
    if (phone.value.lenght > 3) 
        if (['093', '095', '096', '097', '098'].includes(firstThreeChars)) {
            phoneError.style.display = 'none';
        } else {
            phoneError.style.display = 'block';
        }

    
    
    console.log(firstThreeChars);
});

password.addEventListener("input", (e) => {
    const passwordLengthError = document.querySelector('.password-length-error');
    const passwordDigitError = document.querySelector('.password-digit-error');
    const passwordUppercaseError = document.querySelector('.password-uppercase-error');
    const passwordLowercaseError = document.querySelector('.password-lowercase-error');
    const passwordPunctuationError = document.querySelector('.password-punctuation-error');

    // Проверка длины пароля
    if (password.value.length >= 8) {
        passwordLengthError.style.display = 'none';
    } else {
        passwordLengthError.style.display = 'block';
    }

    // Проверка на наличие цифры
    if (/\d/.test(password.value)) {
        passwordDigitError.style.display = 'none';
    } else {
        passwordDigitError.style.display = 'block';
    }

    // Проверка на наличие заглавной буквы
    if (/[A-Z]/.test(password.value)) {
        passwordUppercaseError.style.display = 'none';
    } else {
        passwordUppercaseError.style.display = 'block';
    }

    // Проверка на наличие строчной буквы
    if (/[a-z]/.test(password.value)) {
        passwordLowercaseError.style.display = 'none';
    } else {
        passwordLowercaseError.style.display = 'block';
    }

    // Проверка на наличие знака пунктуации
    if (/[.,?\/#!$%\^&\*;:{}=\-_`~()]/.test(password.value)) {
        passwordPunctuationError.style.display = 'none';
    } else {
        passwordPunctuationError.style.display = 'block';
    }
});