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
                    document.querySelectorAll( ".search").forEach(elem => {
                        elem.style.filter = ('blur(20px)')
                    });
                    i.style.filter = ('blur(0)');
                    
                    i.style.animationName = 'expand'
                    i.style.height = 'auto';
                    i.style.transform = 'scale(1.5)'
                    i.style.backgroundColor = 'var(--blue-color)'

                    let more = document.querySelectorAll('.vacancies-item > .more');
                    i.querySelectorAll('.more').forEach(item => {
                        item.style.visibility = 'visible'
                    })

                    isExpanded = true;
                }
                else {
                    document.querySelectorAll('*').forEach(elem => {
                        elem.style.filter = 'blur(0)'
                    });
                    
                    i.style.animationName = 'reduce'
                    i.style.height = 'fit-content'
                    i.style.transform = 'scale(1)'
                    i.style.backgroundColor = 'var(--blue-color-op)'

                    i.querySelectorAll('.more').forEach(item => {
                        item.style.visibility = 'collapse'
                    })

                    isExpanded = false;
                }
            });
            
        })

        function addAnimation(body) {
            if (!dynamicStyles) {
                dynamicStyles = document.createElement('style');
                dynamicStyles.type = 'text/css';
                document.head.appendChild(dynamicStyles);
            }

            dynamicStyles.sheet.insertRule(body, dynamicStyles.length);
        }