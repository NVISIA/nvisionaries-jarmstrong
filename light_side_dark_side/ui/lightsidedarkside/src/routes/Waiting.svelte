<style>
    div.waiting {
        width: 380px;
        margin: auto;
        margin-top: 380px;
        text-align: center;
    }

    h3.dark-h3 {
        font: normal normal 300 30px/40px Mic 32 New Rounded;
        letter-spacing: 0.6px;
        color: #89C8EE;
        text-transform: capitalize;
        opacity: 1;
        margin-bottom: -80px;
    }

    .meter {
        width: 380px;
        height: 380px;
        background-color: transparent;
    }

    .meter-bg {
        width: 380px;
        height: 380px;
        background-color: transparent;
        background-image: url('../assets/lightsaber.svg');
        background-repeat: no-repeat;
        transform: rotate(45deg);
        filter: invert(84%) sepia(17%) saturate(537%) hue-rotate(169deg) brightness(93%) contrast(90%);
    }

    .meter > span.fill {
        display: block;
        height: 18px;
        width: 312px;
        border-top-right-radius: 9px;
        border-bottom-right-radius: 9px;
        border-top-left-radius: 3px;
        border-bottom-left-radius: 3px;
        background-color: #003148;
        opacity: 1;
        position: relative;
        top: -199px;
        left: 140px;
        z-index: 1;
    }

    .meter > span.meter {
        display: block;
        height: 14px;
        max-width: 310px;
        min-width: 0px;
        width: 310px;
        border-top-right-radius: 9px;
        border-bottom-right-radius: 9px;
        border-top-left-radius: 3px;
        border-bottom-left-radius: 3px;
        background-color: #A9CDE3;
        opacity: 1;
        position: relative;
        top: -215px;
        left: 140px;
        z-index: 1;
        margin-left: 0px;

        animation-name: expand;
        animation-duration: 2s;
        animation-iteration-count: infinite;
        transform-origin: 0%;
    }

    @keyframes expand {
        0% {
            transform: scaleX(0)
        }
        100% {
            transform: scaleX(1)
        }
    }

    p.further-delay-msg {
        opacity: 0%;
        position: relative;
        width: 315px;
        height: 25px;
        text-align: center;
        margin: auto;
        font-size: 22px;
        
        animation-name: appear;
        animation-duration: 2s;
        animation-delay: 10s;
        animation-iteration-count: infinite;
    }

    @keyframes appear {
        0% {
            opacity: 0%
        }
        50% {
            opacity: 100%;
        }
        100% {
            opacity: 0%;
        }
    }
</style>

<div class="waiting">
    <h3 class="dark-h3">Analyzing Your Interior</h3>
    <div class="meter">
        <div class="meter-bg"></div>
        <span class="fill"></span>
        <span class="meter"></span>
    </div>
    <p class="further-delay-msg dark-body">The Force Is Strong with this one</p>
</div>