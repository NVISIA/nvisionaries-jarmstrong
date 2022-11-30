<script>
  import { navigate } from "svelte-routing";
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
  import { FontAwesomeIcon } from 'fontawesome-svelte';
  import { getContext } from 'svelte';

  import ForceMeter from '../lib/components/ForceMeter.svelte';
  import TagYourselfDialog from '../lib/components/TagYourselfDialog.svelte';

  library.add(faEnvelope);

  export let resultData = {
    score: 0.8,
    image: ''
  };

  let selfTag = '';

  /**
   * @param {string} dataToAugment base64 PNG data to convert to a URL
   */
  function addURLToData(dataToAugment) {
    return `data:image/png;base64,${dataToAugment}`;
  }

  function done() {
    navigate("/home", { replace: true });
  }

  const { open } = getContext('simple-modal');
  const setSelfTag = (/** @type {string} */ tag) => selfTag = tag;
  const showTagYourselfDialog = () => open(TagYourselfDialog, { setSelfTag });
</script>

<style>
    div.result-img {
        max-width: 666px;
        margin: auto;
        margin-top: 93px;
        padding: 26px;
        overflow: hidden;

        border: 1px solid #66C7B4;
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
        background-image: url('../assets/lightsaber.svg');
        filter: invert(84%) sepia(17%) saturate(537%) hue-rotate(169deg) brightness(93%) contrast(90%);
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

    div.social-links {
        min-height: 263px;
    }

    div.email-link {
        min-height: 138px;
    }
    hr {
        margin: initial;
        text-align: left;
        max-width: 300px;

        border: 1px solid #A8CCE2;
        opacity: 1;
        margin-bottom: 92px;
    }

    button {
        margin-top: 92px;
        min-width: 137px;
    }

    button.social {
        color: #6FC7B4;
        background: transparent;
        box-shadow: none;
        font-weight: normal;
    }

    button.social .fa-icon {
        font-size: 26px;
        margin-right: 20px;
        vertical-align: middle;
    }
</style>

<div class="share">
    <div class="floating-graphic left">
    </div>
    <div class="floating-graphic right">
    </div>
    <div class="result-img">
        <img src={addURLToData(resultData.image)} alt="Result" />
    </div>
    <div class="score">
        <ForceMeter score={resultData.score}></ForceMeter>
    </div>
    <div class="controls">
        <h3 class="dark-h3">Share Your Allegiance</h3>
        <div class="social-links"></div>
        <hr />
        <h3 class="dark-h3">Keep My Cloak On</h3>
        <div class="email-link">
            <button class="social e-mail" on:click={showTagYourselfDialog}><span class="fa-icon"><FontAwesomeIcon icon="envelope" /></span>EMAIL IT TO ME</button>
        </div>
        <button class="primary" on:click={done}>Done</button>
    </div>
</div>