document.addEventListener("DOMContentLoaded", function () {
    const uploadBox = document.getElementById("uploadBox");
    const fileInput = document.getElementById("fileInput");
    const filePreview = document.getElementById("filePreview");
    const fileName = document.getElementById("fileName");
    const progressBar = document.getElementById("progressBar");
    const removeFile = document.getElementById("removeFile");
    const form = document.querySelector("#uploadFileModal form");

    let progressInterval = null;
    let selectedFile = null;

    function startFakeProgress() {
        let progress = 0;
        progressBar.style.width = "0%";

        if (progressInterval) {
            clearInterval(progressInterval);
        }

        progressInterval = setInterval(() => {
            progress += 10;
            progressBar.style.width = progress + "%";

            if (progress >= 100) {
                clearInterval(progressInterval);
            }
        }, 100);
    }

    function showFilePreview(file) {
        if (!file) return;

        fileName.textContent = file.name;
        filePreview.classList.remove("d-none");
        startFakeProgress();
    }

    if (uploadBox && fileInput) {
        uploadBox.addEventListener("click", function () {
            fileInput.click();
        });
    }

    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const file = this.files[0];

            if (file) {
                selectedFile = file;

                console.log("Selected from picker:", selectedFile);
                console.log("Selected file name:", selectedFile.name);
                console.log("Selected file size:", selectedFile.size);
                console.log("Selected file type:", selectedFile.type);

                showFilePreview(file);
            } else {
                console.log("No file selected from picker");
            }
        });
    }

    if (uploadBox) {
        ["dragenter", "dragover"].forEach(function (eventName) {
            uploadBox.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                uploadBox.classList.add("border-primary", "bg-light");
            });
        });

        ["dragleave", "dragend"].forEach(function (eventName) {
            uploadBox.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                uploadBox.classList.remove("border-primary", "bg-light");
            });
        });

        uploadBox.addEventListener("drop", function (e) {
            e.preventDefault();
            e.stopPropagation();
            uploadBox.classList.remove("border-primary", "bg-light");

            const files = e.dataTransfer.files;

            if (files && files.length > 0) {
                selectedFile = files[0];

                console.log("Dropped file object:", selectedFile);
                console.log("Dropped file name:", selectedFile.name);
                console.log("Dropped file size:", selectedFile.size);
                console.log("Dropped file type:", selectedFile.type);

                showFilePreview(selectedFile);
            } else {
                console.log("No file dropped");
            }
        });
    }

    if (removeFile) {
        removeFile.addEventListener("click", function () {
            if (progressInterval) {
                clearInterval(progressInterval);
            }

            selectedFile = null;
            fileInput.value = "";
            fileName.textContent = "";
            filePreview.classList.add("d-none");
            progressBar.style.width = "0%";
            uploadBox.classList.remove("border-primary", "bg-light");

            console.log("File removed. selectedFile reset to null.");
        });
    }

    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            console.log("Form submit fired");
            console.log("selectedFile:", selectedFile);
            console.log("selectedFile name:", selectedFile ? selectedFile.name : null);

            if (!selectedFile) {
                alert("Please select a file");
                return;
            }

            const formData = new FormData(form);
            formData.set("file", selectedFile);

            fetch(form.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
                }
            })
            .then(response => response.text())
            .then(html => {
                console.log("HTML response received");
                document.open();
                document.write(html);
                document.close();
            })
            .catch(error => {
                console.error("Upload error:", error);
            });
        });
    }
});