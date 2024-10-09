window.addEventListener("DOMContentLoaded", modalGallery);

async function modalGallery(){
    const triggerBtn = document.querySelector("#trigger-modal");
    const closeBtn = document.querySelector("#close-modal");
    triggerBtn.addEventListener("click", openImageModal);
    closeBtn.addEventListener("click", closeModal);

    function openImageModal() {
        document.querySelector("#modal").style.display = "block";
        fetchImages(); // Fetch images from the server
    }
    
    function closeModal() {
        document.querySelector("#modal").style.display = "none";
    }

    async function fetchImages() {
        try {
            const response = await fetch("/api/images", {
                method: "GET",
                headers: {
                    "Content-Type" : "application/json"
                }
            });

            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.status} - ${response.statusText}`);
            }

            const data = await response.json();
            const gallery = document.querySelector("#modal-gallery");
            gallery.innerHTML = ""; // Clear previous images

            data.images.forEach(image => {
                const imgContainer = document.createElement("div");
                const img = document.createElement("img");
                const fileInput = document.querySelector("#replace_image_picker");
                const imgFilename = document.querySelector("#image-filename");
                const imgPreview = document.querySelector("#image-preview");
                const filename = image.url.split('/').pop();
                
                //Styling using Tailwind
                imgContainer.className = "h-40 flex items-center overflow-hidden";
                img.className = "w-full h-full object-cover";
                img.src = image.url; //Store the URL here from the API

                img.addEventListener("click", ()=>{
                    imgPreview.src = "" // Clear the previous URL
                    fileInput.value = filename; // Set the hidden input value with the filename
                    imgFilename.textContent = fileInput.value;
                    const text = imgFilename.textContent
                    imgPreview.src = `/images/${text}`

                    //console.log(imgFilename)
                    //console.log(fileInput)
                    //console.log(imgPreview.src)

                    closeModal();
                })

                imgContainer.appendChild(img);
                gallery.appendChild(imgContainer);
            })
        }
        catch (error) {
            console.error({"An error occurred while processing the request:": error})
        }
    }
}