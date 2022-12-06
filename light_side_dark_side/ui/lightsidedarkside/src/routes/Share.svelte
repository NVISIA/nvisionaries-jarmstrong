<script>
    import { navigate } from "svelte-routing";
    import { library } from "@fortawesome/fontawesome-svg-core";
    import {
        faLinkedin,
        faTwitter,
        faFacebook,
    } from "@fortawesome/free-brands-svg-icons";
    import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
    import { FontAwesomeIcon } from "fontawesome-svelte";

    import ForceMeter from "../lib/components/ForceMeter.svelte";
    import TagYourselfDialog from "../lib/components/TagYourselfDialog.svelte";
    import EnterEmailDialog from "../lib/components/EnterEmailDialog.svelte";

    library.add(faEnvelope);
    library.add(faLinkedin);
    library.add(faFacebook);
    library.add(faTwitter);

    export let resultData = {
        score: 0.8,
        image: "",
    };

    /**
     * @param {string} dataToAugment base64 PNG data to convert to a URL
     */
    function addURLToData(dataToAugment) {
        return `data:image/png;base64,${dataToAugment}`;
    }

    function done() {
        navigate("/home", { replace: true });
    }

    /**
     * @param {RequestInfo | URL} dataUrl
     * @param {string} filename
     * @param {any} mimeType
     */
    async function makeFile(dataUrl, filename, mimeType) {
        const res = await fetch(dataUrl);
        const buf = await res.arrayBuffer();
        return new File([buf], filename, { type: mimeType });
    }

    async function showShareDialog() {
        const shareData = {
            text: `I'm on the ${
                resultData.score > 0.5 ? "dark" : "light"
            } side of tech! #nvisia #techshowcase2022`,
            files: [await makeFile(
                addURLToData(resultData.image),
                "result.png",
                "image/png"
            )],
        };

        await navigator.share(shareData);
    }
</script>

<div class="share">
    <div class="floating-graphic left" />
    <div class="floating-graphic right" />
    <div class="result-img">
        <img src={addURLToData(resultData.image)} alt="Result" />
    </div>
    <div class="score">
        <ForceMeter score={resultData.score} />
    </div>
    <div class="controls">
        <h3 class="dark-h3">Share Your Allegiance</h3>
        <span class="fa-icon"><FontAwesomeIcon icon="envelope" /></span><span
            class="fa-icon"><FontAwesomeIcon icon={["fab", "facebook"]} /></span
        ><span class="fa-icon"
            ><FontAwesomeIcon icon={["fab", "twitter"]} /></span
        ><span class="fa-icon"
            ><FontAwesomeIcon icon={["fab", "linkedin"]} /></span
        >
        <div class="email-link">
            <p>Click the SHARE button below to share your result on social media or via email. Don't forget to tag yourself! (This usually takes the form of an @ and your username.)</p>
            <button class="secondary" on:click={showShareDialog}
                >SHARE</button
            >
        </div>
        <button class="primary" on:click={done}>Done</button>
    </div>
</div>

<style>
    div.result-img {
        max-width: 666px;
        margin: auto;
        margin-top: 93px;
        padding: 26px;
        overflow: hidden;

        border: 1px solid #66c7b4;
        border-radius: 3px;
        opacity: 1;
    }

    img {
        margin: auto;
        display: block;
        min-height: 410px;
    }

    div.floating-graphic {
        width: 465px;
        height: 465px;
        position: absolute;
        background-image: url("../assets/lightsaber.svg");
        filter: invert(84%) sepia(17%) saturate(537%) hue-rotate(169deg)
            brightness(93%) contrast(90%);
    }

    div.floating-graphic.right {
        right: 0px;
        transform: scaleX(-1);
    }

    div.score {
        width: 666px;
        margin: auto;
        margin-top: 92px;
    }

    div.controls {
        width: 666px;
        margin: auto;
        margin-top: 92px;
    }

    button {
        min-width: 137px;
        display: block;
    }

    button.secondary {
        margin-bottom: 20px;
    }

    .fa-icon {
        font-size: 26px;
        margin-right: 20px;
        vertical-align: middle;
    }

    div.email-link {
        margin-top: 20px;
    }

    h3 {
        margin-bottom: 4px;
    }
</style>
