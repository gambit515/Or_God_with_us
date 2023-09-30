let wrapper = document.querySelector('.wrapper')
let vacancy = document.querySelectorAll(".vacancies-item");
let isExpanded = false;
        let dynamicStyles = null;

        const itemHeight = vacancy[0].offsetHeight;

        vacancy.forEach(i => {
                i.addEventListener("click", e => {
                if(!isExpanded) {
                    document.querySelectorAll( ".vacancies-item").forEach(elem => {
                        elem.style.filter = ('blur(20px)')
                    });
                    document.querySelectorAll( ".aside-menu").forEach(elem => {
                        elem.style.filter = ('blur(20px)')
                    });
                    document.querySelectorAll( ".open-vacan").forEach(elem => {
                        elem.style.filter = ('blur(20px)')
                    });
                    i.style.filter = ('blur(0)');
                    
                    addAnimation(`@keyframes expand {
                        from {
                            height: ${itemHeight}px;
                        }
                        to {
                            height: 400px;
                        }
                    }`)
                    i.style.animationName = 'expand'
                    i.style.height = '400px';
                    i.style.transform = 'scale(1.5)'
                    i.style.backgroundColor = 'var(--blue-color)'

                    let button = document.createElement("button");
                    let buttonText = document.createTextNode("Откликнуться");
                    button.appendChild(buttonText);
                    let lastItem = i.lastChild.nextSibling;
                    button.classList.add('btn');
                    button.classList.add('response-btn');
                    i.insertBefore(button, lastItem);

                    button.addEventListener("click", responseHandler);

                    isExpanded = true;
                }
                else {
                    document.querySelectorAll('*').forEach(elem => {
                        elem.style.filter = 'blur(0)'
                    });
                    addAnimation(`@keyframes reduce {
                        from {
                            height: 400px;
                        }
                        to {
                            height: ${itemHeight}px;
                        }
                    }`)
                    i.style.animationName = 'reduce'
                    i.style.height = 'fit-content'
                    i.style.transform = 'scale(1)'
                    i.style.backgroundColor = 'var(--blue-color-op)'

                    const button = document.querySelector("button")
                    i.removeChild(button)

                    isExpanded = false;
                }
            });
            
        })

        function responseHandler() {
            window.open('./response.html', "_self");
        }

        function addAnimation(body) {
            if (!dynamicStyles) {
                dynamicStyles = document.createElement('style');
                dynamicStyles.type = 'text/css';
                document.head.appendChild(dynamicStyles);
            }

            dynamicStyles.sheet.insertRule(body, dynamicStyles.length);
        }