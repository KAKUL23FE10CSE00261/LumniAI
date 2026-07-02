let video = document.getElementById("video");
let canvas = document.getElementById("canvas");
let preview = document.getElementById("preview");
let captureBtn = document.getElementById("captureBtn");

let stream = null;

// Open Camera
async function startCamera() {

    try {

        stream = await navigator.mediaDevices.getUserMedia({
            video: true
        });

        video.srcObject = stream;

        video.style.display = "block";

        captureBtn.style.display = "inline-block";

    }

    catch (error) {

        alert("Unable to access camera.");

        console.error(error);

    }

}

// Capture Image
function captureImage() {

    const context = canvas.getContext("2d");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(
        video,
        0,
        0,
        canvas.width,
        canvas.height
    );

    const imageData = canvas.toDataURL("image/png");

    preview.src = imageData;
    preview.style.display = "block";

    // Stop Camera
    if (stream) {

        stream.getTracks().forEach(track => track.stop());

    }

    video.style.display = "none";
    captureBtn.style.display = "none";

}

// Preview Uploaded Image
function previewImage(event) {

    const file = event.target.files[0];

    if (!file)
        return;

    const reader = new FileReader();

    reader.onload = function(e) {

        preview.src = e.target.result;

        preview.style.display = "block";

    };

    reader.readAsDataURL(file);

}