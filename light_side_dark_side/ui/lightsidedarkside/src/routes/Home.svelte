<script>
    import { navigate } from "svelte-routing";

    function nextPage() {
        navigate("/camera", { replace: true });
    }
</script>

<style>
    div.hero {
        width: 795px;
        height: 309px;
        margin: auto;
        margin-top: 300px;

        font: var(--unnamed-font-style-normal) normal var(--unnamed-font-weight-bold) var(--unnamed-font-size-60)/80px var(--unnamed-font-family-mic-32-new-rounded);
        letter-spacing: var(--unnamed-character-spacing-1-2);
        color: var(---f49e1d);
        text-align: center;
    }

    div.subhead {
        width: 768px;
        height: 74px;
        margin: auto;

        color: var(--unnamed-color-89c8ee);
        text-align: left;
    }

    div.steps {
        width: 768px;
        height: 193px;
        margin: auto;
        margin-top: 64px;
    }

    ol {
        font: var(--unnamed-font-style-normal) normal var(--unnamed-font-weight-300) 22px/var(--unnamed-line-spacing-28) var(--unnamed-font-family-mic-32-new-rounded);
        font-size: 22px;
        color: var(--unnamed-color-ffffff);
        text-align: left;

        list-style: none;
        counter-reset: science-fair-counter;
    }

    li {
        counter-increment: science-fair-counter;
        margin: 0.25rem;
        margin-top: 43px;
    }

    li::before {
        content: counter(science-fair-counter);
        background: var(---6fc7b4);
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        display: inline-block;
        line-height: 2rem;
        color: var(--background-color);
        text-align: center;
        margin-right: 1.5rem;
        font-family: var(--unnamed-font-family-mic-32-new-rounded);
        font-style: var(--unnamed-font-style-normal);
        font-weight: var(--unnamed-font-weight-bold);
        font-size: var(--unnamed-font-size-24);
        line-height: var(--unnamed-line-spacing-34);
        letter-spacing: var(--unnamed-character-spacing-0-48);
    }

    div.mainbutton {
        margin: auto;
        margin-top: 50px;
        text-align: center;
    }

    div.mainbutton button {
        margin: auto;
        margin-top: 25px;
        display: block;
        padding-top: 10px;
        padding-bottom: 10px;

        background: transparent linear-gradient(102deg, #E46528 0%, #E46528 100%) 0% 0% no-repeat padding-box;
        box-shadow: 0px 3px 6px #001924;
        border-radius: 3px;
        border: 0px;
        opacity: 1;

        font: var(--unnamed-font-style-normal) normal var(--unnamed-font-weight-bold) var(--unnamed-font-size-24) var(--unnamed-font-family-mic-32-new-rounded);
        letter-spacing: var(--unnamed-character-spacing-0-36);
        color: var(--unnamed-color-ffffff);
        text-align: center;
        font: normal normal bold 18px/28px Mic 32 New Rounded;
        letter-spacing: 0.36px;
        color: #FFFFFF;
        text-transform: capitalize;
        opacity: 1;
    }

    div.floating-graphic {
        margin-top: -240px;
        width: 420px;
        height: 420px;
        position: absolute;
        background-image: url('../assets/lightsaber.svg');
        background-repeat: no-repeat;
        filter: invert(84%) sepia(17%) saturate(537%) hue-rotate(169deg) brightness(93%) contrast(90%);
    }

    div.floating-graphic.left {
        left: -80px;
        margin-left: 100px;
        transform: rotate(8deg) scaleX(1.2);
    }

    div.floating-graphic.right {
        right: -80px;
        margin-right: 100px;
        transform: rotate(-8deg) scaleX(-1.2);
    }
</style>

<div class="home">
    <div class="floating-graphic left">
    </div>
    <div class="floating-graphic right">
    </div>
    <div class="hero">
        Are you on <br/> the DARK SIDE or the LIGHT SIDE of tech?
    </div>
    <div class="subhead h3">
        Allow our photo scanning technology to help determine which side you fall within.  
    </div>
    <div class="steps">
        <ol>
            <li>Capture your photo on the next screen</li>
            <li>The algorithm will apply background and foreground imagery depending on where your allegiance lies.</li>
            <li>Send your transformed image to yourself to share on social media!</li>
        </ol>
    </div>
    <div class="mainbutton">
        <div class="dark-accent">SEE WHICH SIDE YOU’RE ON!</div>
        <button on:click={nextPage}>Take My Photo!</button>
    </div>
</div>