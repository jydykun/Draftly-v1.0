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

});
