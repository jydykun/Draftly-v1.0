window.addEventListener("DOMContentLoaded", ()=>{
    
    // TinyMCE Initialization
    tinymce.init({
        selector: "#tinymce_editor",
        license_key: "gpl",
        plugins: "image save visualblocks preview help link autolink",
        toolbar: "undo redo image cancel preview help link | align fontfamily styles",
        images_upload_url: "/upload",
        link_assume_external_targets: true,
        link_context_toolbar: true
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

    const subsForm = document.querySelector("#subscribe-form");
    const message = document.querySelector("#subscribe-form-message");

    subsForm.addEventListener("submit", (e)=>{
        e.preventDefault()

        formData = new FormData(subsForm)

        fetch("/subscribe", {
            method: "POST",
            body: formData
        })
        .then(response => {
            if(!response.ok){
                return response.json()
                .then(result => {
                    message.textContent = result.errors.email[0]
                })
            }
            else {
                return response.json()
                .then(result => {
                    message.textContent = result.success
                })
            }
        })
        .catch(err => {
            console.log(err)
        })

    });

});

