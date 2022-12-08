<script>
    import { navigate } from "svelte-routing";

    export let photoData;
    export let height;
    export let submitPhoto = () => {};

    function previousPage() {
        navigate("/camera", { replace: true });
    }
</script>

<div class="preview">
    <div class="preview-img">
        <img
            src={photoData}
            style="height: {height}px"
            alt="Preview"
        />
    </div>
    <div class="controls">
        <h3 class="dark-h3">You Look Marvelous!</h3>
        <p class="directions">
            Submit photo to the algorithm to continue, or go back to the camera
            to retake your photo
        </p>
        <button class="primary" on:click={submitPhoto}
            >Test My Force Alignment</button
        >
        <button class="secondary" on:click={previousPage}>Back To Camera</button
        >
    </div>
</div>

<style>
    div.preview-img {
        margin: auto;
        width: 700px;
    }

    img {
        display: block;
        width: 700px;
        margin: auto;
        margin-top: 185px;
    }

    div.controls {
        width: 700px;
        height: 243px;
        margin: auto;
        margin-top: 92px;
    }

    p.directions {
        margin-top: 40px;
        text-align: left;
        font: normal normal 300 22px/28px Mic 32 New Rounded;
        letter-spacing: 0.44px;
        color: #ffffff;
        opacity: 1;
    }

    button.primary {
        display: block;
        margin-top: 40px;
    }

    button.secondary {
        display: block;
        margin-top: 40px;
    }
</style>
