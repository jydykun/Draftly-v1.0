window.addEventListener("DOMContentLoaded", () => {
    //fetchStatus()
    //fetchCategoriesList()
});


function fetchStatus() {
    const form = document.querySelector("#add-category");

    form.addEventListener("submit", async (e)=>{
        e.preventDefault()
        const formData = new FormData(form)

        try {
            const response = await fetch("/add-category", {
                method: "POST",
                //body: formData
            });
            const data = await response.json();
            const msg = document.querySelector("#status-msg");
            const div = document.querySelector("#categories-list");
            if(!response.ok) {
                msg.textContent = data.errors.category[0]
            }
            else{
                if(data.error){
                    msg.textContent = data.error;
                }
                else{
                    msg.textContent = data.success;
                    const p = document.createElement("p");
                    p.textContent = formData.get("category");  // Get the category name from the form data
                    div.appendChild(p);
                }
            }
        }
        catch (error) {
            console.error({"An error occurred while processing the request:": error})
        }
        
    })
}

async function fetchCategoriesList() {
    const div = document.querySelector("#categories-list");
    try {
        const response = await fetch("/api/categories", {
            method: "GET",
            headers: {
                "Content-Type" : "application/json"
            }
        });

        if (!response.ok) {
            throw new Error(`Failed to fetch: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();

        data.forEach(category => {
            const p = document.createElement("p");
            p.textContent = category.category_name
            div.appendChild(p)

        })
    }
    catch (error) {
        console.error({"An error occurred while processing the request:": error})
    }
}