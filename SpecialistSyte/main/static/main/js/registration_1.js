
//объявляем ссылки на получаемые данные
const myForm = document.querySelector('#form-group');
const UserInput = document.querySelector('#user_psevdomin');
const passwordInput = document.querySelector('#password');
const DpasswordInput = document.querySelector('#Dpassword');
const MailInput = document.querySelector('#mail');
const RadiosInput1 = document.querySelector('#exampleRadios1');
const RadiosInput2 = document.querySelector('#exampleRadios2');
const BirthDayInput = document.querySelector('#BirthDay');
const msg = document.querySelector('.msg');


console.log(UserInput);
console.log(passwordInput);
console.log(DpasswordInput);
console.log(MailInput);
console.log(RadiosInput1);
console.log(RadiosInput2);
console.log(BirthDayInput);
console.log(msg);


//Общий код проверки всех полей:

//запуск функции по нажатию кнопки
myForm.addEventListener('submit', onSubmit);


function onSubmit(e){
    
  // e.preventDefault();

    if(UserInput.value === ""){
        e.preventDefault();
        msg.classList.add('error');
        msg.innerHTML = 'Не введено поле \"имя пользователя\"!';
        setTimeout(()=> {
            msg.classList.remove('error');
            msg.innerHTML = '';
        }, 3000);
        
    }else if (passwordInput.value === "" || DpasswordInput.value === "") {
    e.preventDefault();
    msg.classList.add('error');
    msg.innerHTML = 'Поля c паролями не должны быть пустыми!';
    setTimeout(() => {
        msg.classList.remove('error');
        msg.innerHTML = '';
    }, 3000);
    } else if (passwordInput.value !== DpasswordInput.value) {
    e.preventDefault();
    msg.classList.add('error');
    msg.innerHTML = 'Пароли не совпадают!';
    setTimeout(() => {
        msg.classList.remove('error');
        msg.innerHTML = '';
    }, 3000);
    } else if(MailInput.value === ""){
        e.preventDefault();
        msg.classList.add('error');
        msg.innerHTML = 'Не введено поле \"E-mail\"!';
        setTimeout(()=> {
            msg.classList.remove('error');
            msg.innerHTML = '';
        }, 3000);
    }else if(BirthDayInput.value === ""){
        e.preventDefault();
        msg.classList.add('error');
        msg.innerHTML = 'Не введено поле \"Дата рождения\"!';
        setTimeout(()=> {
            msg.classList.remove('error');
            msg.innerHTML = '';
        }, 3000);
       
    } else {
        console.log(UserInput.value);
        console.log(passwordInput.value);
        console.log(DpasswordInput.value);
        console.log(MailInput.value);

        if(RadiosInput1.checked){
            console.log(RadiosInput1.value);
        }else {
            console.log(RadiosInput2.value); 
        }
        console.log(BirthDayInput.value);
    } 
}