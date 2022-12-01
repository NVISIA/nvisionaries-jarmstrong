<script>
    import { navigate } from "svelte-routing";
    import { library } from "@fortawesome/fontawesome-svg-core";
    import {
        faFacebook,
        faLinkedin,
        faTwitter,
    } from "@fortawesome/free-brands-svg-icons";
    import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
    import { FontAwesomeIcon } from "fontawesome-svelte";

    import ForceMeter from "../lib/components/ForceMeter.svelte";
    import TagYourselfDialog from "../lib/components/TagYourselfDialog.svelte";
    import EnterEmailDialog from "../lib/components/EnterEmailDialog.svelte";

    library.add(faEnvelope);
    library.add(faFacebook);
    library.add(faLinkedin);
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
    function makeFile(dataUrl, filename, mimeType) {
        return fetch(dataUrl)
            .then((res) => res.arrayBuffer())
            .then((buf) => new File([buf], filename, { type: mimeType }));
    }

    async function showEmailDialog() {
        const shareData = {
            text: `I'm on the ${
                resultData.score > 0.5 ? "dark" : "light"
            } side of tech!`,
            file: await makeFile(
                addURLToData(resultData.image),
                "result.png",
                "image/png"
            ),
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
        <div class="social-links">
            <button class="social facebook" on:click={showFacebookDialog}
                ><span class="fa-icon"
                    ><FontAwesomeIcon icon={["fab", "facebook"]} /></span
                >SHARE TO FACEBOOK</button
            >
            <button class="social facebook" on:click={showLinkedInDialog}
                ><span class="fa-icon"
                    ><FontAwesomeIcon icon={["fab", "linkedin"]} /></span
                >SHARE TO LINKEDIN</button
            >
            <button class="social facebook" on:click={showTwitterDialog}
                ><span class="fa-icon"
                    ><FontAwesomeIcon icon={["fab", "twitter"]} /></span
                >SHARE TO TWITTER</button
            >
        </div>
        <hr />
        <h3 class="dark-h3">Keep My Cloak On</h3>
        <div class="email-link">
            <button class="social e-mail" on:click={showEmailDialog}
                ><span class="fa-icon"><FontAwesomeIcon icon="envelope" /></span
                >EMAIL IT TO ME</button
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

    hr {
        margin: initial;
        text-align: left;
        max-width: 300px;

        border: 1px solid #a8cce2;
        opacity: 1;
    }

    button {
        min-width: 137px;
        display: block;
    }

    button.social {
        color: #6fc7b4;
        background: transparent;
        box-shadow: none;
        font-weight: normal;
        border: none;
        margin-bottom: 40px;
    }

    button.social .fa-icon {
        font-size: 26px;
        margin-right: 20px;
        vertical-align: middle;
    }
</style>
