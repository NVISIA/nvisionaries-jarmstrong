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

    button.main {
        display: block;
        margin-top: 40px;
        padding: 5px 15px;

        width: 230px;

        background: transparent linear-gradient(98deg, #E46528 0%, #E46528 100%) 0% 0% no-repeat padding-box;
        box-shadow: 0px 3px 6px #001924;
        border-radius: 3px;
        border: none;
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

    button.secondary {
        display: block;
        margin-top: 40px;
        padding: 2px 15px;

        background: var(---003148) 0% 0% no-repeat padding-box;
        border: 2px solid var(--unnamed-color-89c8ee);
        background: #003148 0% 0% no-repeat padding-box;
        box-shadow: 0px 3px 6px #001924;
        border: 2px solid #89C8EE;
        border-radius: 3px;
        opacity: 1;

        font: var(--unnamed-font-style-normal) normal var(--unnamed-font-weight-medium) var(--unnamed-font-size-16)/var(--unnamed-line-spacing-28) var(--unnamed-font-family-mic-32-new-rounded);
        letter-spacing: var(--unnamed-character-spacing-0-32);
        color: var(--unnamed-color-ffffff);
        text-align: center;
        font: normal normal medium 16px/28px Mic 32 New Rounded;
        letter-spacing: 0.32px;
        color: #FFFFFF;
        text-transform: capitalize;
        opacity: 1;
    }
</style>

<div class="preview">
    <div class="preview-img">
        <img src={photoData} alt="Preview" />
    </div>
    <div class="controls">
        <h3 class="dark-h3">You Look Marvelous!</h3>
        <p class="directions">Submit photo to the algorithm to continue, or go back to the camera to retake your photo</p>
        <button class="main" on:click={submitPhoto}>Test My Force Alignment</button>
        <button class="secondary" on:click={previousPage}>Back To Camera</button>
    </div>
</div>