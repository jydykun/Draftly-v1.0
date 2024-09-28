window.addEventListener("DOMContentLoaded", ()=>{
    function openImageModal(callback) {
        document.getElementById('imageModal').style.display = 'block';
        fetchImages(callback); // Fetch images from your server
    }
    
    function closeModal() {
        document.getElementById('imageModal').style.display = 'none';
    }
    
    function fetchImages(callback) {
        fetch('/api/images') // Replace with your endpoint
            .then(response => response.json())
            .then(data => {
                const gallery = document.getElementById('image-gallery');
                gallery.innerHTML = ''; // Clear previous images
                data.images.forEach(image => {
                    const img = document.createElement('img');
                    img.src = image.url; // Assuming the image object has a URL property
                    img.onclick = () => selectImage(image.url);
                    gallery.appendChild(img);
                    callback(img.src);
                });
            });
    }
    
    function selectImage(imageUrl) {
        tinymce.activeEditor.execCommand('mceInsertContent', false, `<img src="${imageUrl}" alt="Selected Image"/>`);
        closeModal();
    }
    
    // TinyMCE Initialization
    tinymce.init({
        selector: "#tinymce_editor",
        license_key: "gpl",
        plugins: "image save visualblocks code pagebreak nonbreaking preview",
        toolbar: "undo redo image visualblocks code pagebreak nonbreaking preview",
        images_upload_url: "/upload",
        file_picker_callback: function (callback) {
            openImageModal(callback); // Call the modal open function
        },
        visualblocks_default_state: true
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

