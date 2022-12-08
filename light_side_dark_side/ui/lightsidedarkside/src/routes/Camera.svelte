<script>
    import { navigate } from "svelte-routing";

    let width = 700; /* px */
    export let height = 816; /* px */

    let streaming = false;

    export let photoData = null;

    let video;
    let canvas;

    navigator.mediaDevices
        .getUserMedia({
            video: { facingMode: "user", width, height },
            audio: false,
        })
        .then((stream) => {
            video.srcObject = stream;
            video.play();
        })
        .catch((err) => {
            console.error(`An error occurred: ${err}`);
        });

    function ready() {
        if (!streaming) {
            height = video.videoHeight;
            width = video.videoWidth;

            video.setAttribute("width", width);
            video.setAttribute("height", height);
            canvas.setAttribute("width", width);
            canvas.setAttribute("height", height);
            streaming = true;
        }
    }

    function nextPage() {
        navigate("/preview", { replace: true });
    }

    function takepicture() {
        const context = canvas.getContext("2d");

        if (width && height) {
            canvas.width = 1024;
            canvas.height = (1024 / width) * height;
            context.drawImage(video, 0, 0, 1024, canvas.height);

            photoData = canvas.toDataURL("image/png");

            if (photoData) {
                video.pause();
                video.srcObject = null;
                streaming = false;

                nextPage();
            } else {
                console.error("An error occurred - no photo caputured");
            }
        }
    }
</script>

<div class="camera">
    <video id="video" bind:this={video} on:canplay={ready}>
        <!-- empty captions because we're displaying the user's own captured photo without audio-->
        <track kind="captions" />
    </video>
    <button class="primary" id="startbutton" on:click={takepicture}
        >Take photo</button
    >

    <!-- This canvas is invisible - used to hold the captured frame data -->
    <canvas id="canvas" bind:this={canvas} />
</div>

<style>
    video {
        display: block;
        width: 700px;
        margin: auto;
        margin-top: 185px;
    }

    button {
        display: block;
        margin: auto;
        margin-top: 185px;
        padding: 10px 15px;
    }

    canvas {
        display: none;
    }
</style>
