<script>
    import { navigate } from "svelte-routing";

    let width = 700; /* px */
    let height = 816; /* px */

    let streaming = false;

    export let photoData = null;

    let video;
    let canvas;

    navigator.mediaDevices
        .getUserMedia({ video: { facingMode: "user" }, audio: false })
        .then(stream => {
            video.srcObject = stream;
            video.play();
        })
        .catch(err => {
            console.error(`An error occurred: ${err}`);
        });

    function ready() {
        if (!streaming) {
            height = (video.videoHeight / video.videoWidth) * width;

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
                nextPage();
            } else {
                console.error("An error occurred - no photo caputured");
            }
        }
    }
</script>

<style>
    video {
        display: block;
        width: 700px;
        height: 817px;
        margin: auto;
        margin-top: 185px;
    }

    button {
        display: block;
        margin: auto;
        margin-top: 185px;
        padding: 10px 15px;

        background: transparent linear-gradient(102deg, #E46528 0%, #E46528 100%) 0% 0% no-repeat padding-box;
        box-shadow: 0px 3px 6px #001924;
        border-radius: 3px;
        border: 0px;
        opacity: 1;

        font: var(--unnamed-font-style-normal) normal var(--unnamed-font-weight-bold) var(--unnamed-font-size-18)/var(--unnamed-line-spacing-28) var(--unnamed-font-family-mic-32-new-rounded);
        letter-spacing: var(--unnamed-character-spacing-0-36);
        color: var(--unnamed-color-ffffff);
        text-align: center;
        font: normal normal bold 18px/28px Mic 32 New Rounded;
        letter-spacing: 0.36px;
        color: #FFFFFF;
        text-transform: capitalize;
        opacity: 1;
    }

    canvas {
        display: none;
    }
</style>

<div class="camera">
    <video id="video" bind:this={video} on:canplay={ready}>
        <!-- empty captions because we're displaying the user's own captured photo without audio-->
        <track kind="captions" />
    </video>
    <button id="startbutton" on:click={takepicture}>Take photo</button>

    <!-- This canvas is invisible - used to hold the captured frame data -->
    <canvas id="canvas" bind:this={canvas}></canvas>
</div>