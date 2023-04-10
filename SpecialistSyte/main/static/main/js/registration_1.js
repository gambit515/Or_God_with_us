
//объявляем ссылки на получаемые данные
const myForm = document.querySelector('#form-group');
const UserInput = document.querySelector('#user');
const passwordInput = document.querySelector('#password');
const DpasswordInput = document.querySelector('#Dpassword');
const MailInput = document.querySelector('#mail');
const RadiosInput = document.querySelector('#exampleRadios1');
const msg = document.querySelector('.msg');




//запуск функции по нажатию кнопки
myForm.addEventListener('submit', onSubmit);

//проверка на соответствие паролей
function onSubmit(e){
    console.log(passwordInput.value);

    if(passwordInput.value === DpasswordInput.value){
        console.log('success');

    }else {

    e.preventDefault();
    msg.classList.add('error');
    msg.innerHTML = 'Пароль не соответствует!';
    setTimeout(()=> {
        msg.classList.remove('error');
        msg.innerHTML = '';
    }, 3000);
    }
}





