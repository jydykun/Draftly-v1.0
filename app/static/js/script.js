window.addEventListener("DOMContentLoaded", ()=>{
    
    // TinyMCE Initialization
    tinymce.init({
    selector: "#tinymce_editor",
    plugins: "image",
    toolbar: "image",
    images_upload_url: "{{ url_for('main.upload') }}"
    });


    const input = document.querySelector("#feature_image");
    const preview = document.querySelector("#preview-image");

    // Check elements first before adding event listeners
    // to avoid Uncaught TypeError
    if(input && preview){
        input.addEventListener("change", (e)=>{
            const file = e.target.files[0];
            const reader = new FileReader();
    
            reader.onload = ()=>{
                preview.src = reader.result;
            }
            reader.readAsDataURL(file);
        });
    }


    const menuBurger = document.querySelector("#menu-burger-icon");
    const collapse = document.querySelector("#collapse");

    // Check elements first before adding event listeners
    // to avoid Uncaught TypeError
    if(menuBurger && collapse) {
        menuBurger.addEventListener("click", ()=>{
            // Toggle the collapsible menu
            collapse.classList.toggle("hidden");
    
            // Toggle the active class to trigger the animation
            menuBurger.classList.toggle("open");
        });
    }

    // Wrap every letter in a span
    var textWrapper = document.querySelector('.ml11 .letters');
    textWrapper.innerHTML = textWrapper.textContent.replace(/([^\x00-\x80]|\w)/g, "<span class='letter'>$&</span>");

    anime.timeline({loop: false})
    .add({
        targets: '.ml11 .line',
        scaleY: [0,1],
        opacity: [0.5,1],
        easing: "easeOutExpo",
        duration: 700
    })
    .add({
        targets: '.ml11 .line',
        translateX: [0, document.querySelector('.ml11 .letters').getBoundingClientRect().width + 10],
        easing: "easeOutExpo",
        duration: 700,
        delay: 100
    }).add({
        targets: '.ml11 .letter',
        opacity: [0,1],
        easing: "easeOutExpo",
        duration: 600,
        offset: '-=775',
        delay: (el, i) => 34 * (i+1)
    }).add({
        targets: '.ml11',
        opacity: 1,
        duration: 1000,
        easing: "easeOutExpo",
        delay: 1000
    }).add({
        targets: '.ml11 .line',
        opacity: 0,
        easing: "easeOutExpo",
    })


    /* -----------------------------------------------
    /* How to use? : Check the GitHub README
    /* ----------------------------------------------- */

    /* To load a config file (particles.json) you need to host this demo (MAMP/WAMP/local)... */
    /*
    particlesJS.load('particles-js', 'particles.json', function() {
    console.log('particles.js loaded - callback');
    });
    */

    /* Otherwise just put the config content (json): */

    particlesJS('particles-js',
    
        {
        "particles": {
            "number": {
            "value": 80,
            "density": {
                "enable": true,
                "value_area": 800
            }
            },
            "color": {
            "value": "#ffffff"
            },
            "shape": {
            "type": "circle",
            "stroke": {
                "width": 0,
                "color": "#000000"
            },
            "polygon": {
                "nb_sides": 5
            },
            "image": {
                "src": "img/github.svg",
                "width": 100,
                "height": 100
            }
            },
            "opacity": {
            "value": 0.5,
            "random": false,
            "anim": {
                "enable": false,
                "speed": 1,
                "opacity_min": 0.1,
                "sync": false
            }
            },
            "size": {
            "value": 3,
            "random": true,
            "anim": {
                "enable": false,
                "speed": 40,
                "size_min": 0.1,
                "sync": false
            }
            },
            "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1
            },
            "move": {
            "enable": true,
            "speed": 6,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
                "enable": false,
                "rotateX": 600,
                "rotateY": 1200
            }
            }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": {
            "onhover": {
                "enable": true,
                "mode": "repulse"
            },
            "onclick": {
                "enable": true,
                "mode": "push"
            },
            "resize": true
            },
            "modes": {
            "grab": {
                "distance": 400,
                "line_linked": {
                "opacity": 1
                }
            },
            "bubble": {
                "distance": 400,
                "size": 40,
                "duration": 2,
                "opacity": 8,
                "speed": 3
            },
            "repulse": {
                "distance": 200,
                "duration": 0.4
            },
            "push": {
                "particles_nb": 4
            },
            "remove": {
                "particles_nb": 2
            }
            }
        },
        "retina_detect": true
        }
    
    );


});
