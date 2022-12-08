<script>
    import { navigate } from "svelte-routing";

    export let error;

    function goHome() {
        navigate("/home", { replace: true });
    }
</script>

<div class="share">
    <h3 class="dark-h3">There is a great disturbance in the Force</h3>
    <div class="floating-graphic left" />
    <div class="floating-graphic right" />
    <div class="result-img">
        <img src="/jarjar.jpg" alt="Jar Jar Binks" />
    </div>
    <div class="score">
        <p>An error occurred. This was how the message ran: {error}</p>
    </div>
    <div class="controls">
        <button class="primary" on:click={goHome}>Done</button>
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
        width: 666px;
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

    h3 {
        margin-bottom: 4px;
        text-align: center;
    }
</style>
