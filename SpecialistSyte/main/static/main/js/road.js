/*

var loginButton = document.getElementById("login");

if (loginButton) { // Проверяем, что кнопка с id="login" существует на странице
  loginButton.addEventListener('click', onSubmit);
}

function onSubmit(e){
  e.preventDefault(); // Отменяем стандартное поведение ссылки
  
  var url = window.location.href; // Получаем текущий URL
  if (url.includes('localhost')) { // Проверяем, что сайт находится на localhost
    window.location.href = 'registration.html?animation=1'; //этот костыль нет... (потом скрипт закину в JS)
  } else { // Если сайт не находится на localhost, то используем полный URL
    window.location.href = 'http://127.0.0.1:8000/registration/?animation=1'; //этот костыль работает
  }
}

*/