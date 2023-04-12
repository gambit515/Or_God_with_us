const urlParams = new URLSearchParams(window.location.search);
			console.log(window.location.href)
					const animationParam = urlParams.get('animation');
			
					console.log(animationParam)
			// Если значение параметра `myParam` равно `myValue`, то выполняем скрипт
			if (animationParam === '1') {
				
				// Находим заголовок и абзац
				const title = document.querySelector('#animated-element');
				console.log(title)
				
				setTimeout(function() {
    // Изменяем стили элементов
    title.style.opacity = 1;
    title.style.transform = 'translateY(0)';
   
  }, 500);
		  
}