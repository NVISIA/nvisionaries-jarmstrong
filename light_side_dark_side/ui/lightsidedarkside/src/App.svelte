<script>
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { faCamera } from '@fortawesome/free-solid-svg-icons';
  import { FontAwesomeIcon } from 'fontawesome-svelte';

  import { Router, Link, Route, navigate } from "svelte-routing";
  
  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  import Camera from "./routes/Camera.svelte";
  import Preview from "./routes/Preview.svelte";
  import Waiting from "./routes/Waiting.svelte";
  import Share from "./routes/Share.svelte";

  import Modal from 'svelte-simple-modal';

  library.add(faCamera);

  const backendURL = 'https://2lcxfaa5yeav5mn7sdsol4vf740zlhdx.lambda-url.us-east-2.on.aws/';

  export let url = "";

  let photoData;
  let resultData;

  /**
   * @param {string} dataToStrip
   */
  function stripURLFromData(dataToStrip) {
    return dataToStrip.substring(23);
  }
  
  async function submitPhoto () {
    const formData = new FormData();
    formData.append('photo', stripURLFromData(photoData));

    const uploadPromise = fetch(backendURL, {
      method: 'POST',
      body: formData
    });

    navigate("/waiting");

    const awaitedCall = await uploadPromise;
    const json = await awaitedCall.json();
    resultData = json;

    navigate("/share");
  };
</script>

<style>
  div {
    width: 1024px;
    margin: auto;
  }

  nav {
    width: 1024px;
    padding-top: 34px;
    padding-bottom: 34px;
    padding-left: 38px;
  }

  nav * {
    margin-right: 40px;
  }

  .link {
    color: var(--unnamed-color-ffffff);
  }

  .fa-camera-icon {
    font-size: 34px;
    margin-right: 14px;
    color: var(--icon-color);
  }

  div.dark-body {
    height: 100%;
    background-color: var(--background-color);
    min-height: 1280px;
  }

  div.divider {
    width: 100%;
    height: 10px;

    background: var(---425d93);
  }

  div.route-shim {
    background: transparent linear-gradient(0deg, #001924 0%, #00192400 100%) 0% 0% no-repeat padding-box;
    opacity: 1;
    height: 100%;
    min-height: 1280px;
  }
</style>

<svelte:head>
  <link rel="stylesheet" href="https://use.typekit.net/rbq3ono.css">
</svelte:head>

<div class="body dark-body">
  <Router {url}>
    <nav>
      <Link to="/"><span class="fa-camera-icon"><FontAwesomeIcon icon="camera" /></span><span class="link dark-h3">Home</span></Link>
      <Link to="/about"><span class="link dark-h3">About the App</span></Link>
    </nav>
    <div class="divider">&nbsp;</div>
    <div class="route-shim">
      <Route path="/"><Home /></Route>
      <Route path="/home"><Home /></Route>
      <Route path="/about"><About /></Route>
      <Route path="/camera"><Camera bind:photoData /></Route>
      <Route path="/preview"><Preview {photoData} {submitPhoto} /></Route>
      <Route path="/waiting"><Waiting /></Route>
      <Route path="/share"><Modal closeButton={false} unstyled={true}><Share bind:resultData /></Modal></Route>
    </div>
  </Router>
</div>