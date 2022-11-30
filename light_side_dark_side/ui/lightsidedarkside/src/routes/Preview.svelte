<script>
    import { navigate } from "svelte-routing";

    export let photoData;
    export let submitPhoto = () => {};

    function previousPage() {
        navigate("/camera", { replace: true });
    }
</script>

<style>
    div.preview-img {
        margin: auto;
        width: 700px;
        height: 817px;
    }

    img {
        display: block;
        width: 700px;
        margin: auto;
        margin-top: 185px;
    }

    div.controls {
        width: 782px;
        height: 243px;
        margin: auto;
        margin-top: 185px;
    }

    p.directions {
        margin-top: 40px;
        text-align: left;
        font: normal normal 300 22px/28px Mic 32 New Rounded;
        letter-spacing: 0.44px;
        color: #FFFFFF;
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

<div class="preview">
    <div class="preview-img">
        <img src={photoData} alt="Preview" />
    </div>
    <div class="controls">
        <h3 class="dark-h3">You Look Marvelous!</h3>
        <p class="directions">Submit photo to the algorithm to continue, or go back to the camera to retake your photo</p>
        <button class="primary" on:click={submitPhoto}>Test My Force Alignment</button>
        <button class="secondary" on:click={previousPage}>Back To Camera</button>
    </div>
</div>