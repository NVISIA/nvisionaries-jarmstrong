<script>
  import { library } from "@fortawesome/fontawesome-svg-core";
  import { faCamera } from "@fortawesome/free-solid-svg-icons";
  import { FontAwesomeIcon } from "fontawesome-svelte";

  import { Router, Link, Route, navigate } from "svelte-routing";

  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  import Camera from "./routes/Camera.svelte";
  import Preview from "./routes/Preview.svelte";
  import Waiting from "./routes/Waiting.svelte";
  import Share from "./routes/Share.svelte";
  import Error from "./routes/Error.svelte";

  library.add(faCamera);

  const backendURL = "https://faceswap.nvisionaries.dev.nvisia.io";
  // const backendURL = "http://faces-LoadB-643OVNWBHHJG-1ec63b91f523bcdb.elb.us-east-2.amazonaws.com";
  const eventSinkUrl = "https://edsf.itwasaday.net/api/boothEvents";
  const eventSinkAuthKey = "3a1d287e-7e57-464c-b0b5-e6595ece0b6b";

  const EVENTSINK_HEADER_NAME = "Authorization";

  export let url = "";

  let photoData;
  let resultData;
  let height;
  let error;
  let modalIsBeingDisplayed = false;

  /**
   * @param {string} data
   */
  function stripUrlFromString(data) {
    return data.substring(22);
  }

  /**
   * @param {any} resultData
   */
  async function postResultsToGeorge(resultData) {
    const headers = {
      "Content-type": "application/json",
      [EVENTSINK_HEADER_NAME]: eventSinkAuthKey,
    };

    return fetch(eventSinkUrl, {
      method: "POST",
      headers,
      body: JSON.stringify({
        messageType: "sithjedi",
        message: "photo",
        json: JSON.stringify(resultData),
      }),
    });
  }

  async function submitPhoto() {
    const file = stripUrlFromString(photoData);
    const formData = new FormData();
    formData.append("file", file);

    const uploadPromise = fetch(backendURL, {
      method: "POST",
      body: formData,
    });

    navigate("/waiting");

    try {
      const awaitedCall = await uploadPromise;

      if (awaitedCall.status !== 200) {
        error = await awaitedCall.text();
        navigate("/error");
      } else {
        const json = await awaitedCall.json();
        resultData = json;
        navigate("/share");
      }
    } catch (apiError) {
      error = apiError;
      navigate("/error");
    }

    if (resultData) {
      await postResultsToGeorge(resultData);
    }
  }
</script>

<svelte:head>
  <link rel="stylesheet" href="https://use.typekit.net/rbq3ono.css" />
</svelte:head>

<div class="body dark-body">
  {#if modalIsBeingDisplayed}
    <div class="scrim" />
  {/if}

  <Router {url}>
    <nav>
      <Link to="/"
        ><span class="fa-camera-icon"><FontAwesomeIcon icon="camera" /></span
        ><span class="link dark-h3">Home</span></Link
      >
      <Link to="/about"><span class="link dark-h3">About the App</span></Link>
    </nav>
    <div class="divider">&nbsp;</div>
    <div class="route-shim">
      <Route path="/"><Home /></Route>
      <Route path="/home"><Home /></Route>
      <Route path="/about"><About /></Route>
      <Route path="/camera"><Camera bind:photoData bind:height /></Route>
      <Route path="/preview"
        ><Preview {photoData} {submitPhoto} {height} /></Route
      >
      <Route path="/waiting"><Waiting /></Route>
      <Route path="/share"><Share bind:resultData /></Route>
      <Route path="/error"><Error {error} /></Route>
    </div>
  </Router>
</div>

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
    background: transparent linear-gradient(0deg, #001924 0%, #00192400 100%) 0%
      0% no-repeat padding-box;
    opacity: 1;
    height: 100%;
    min-height: 1280px;
  }

  div.scrim {
    background-color: black;
    opacity: 0.7;
    min-height: 1280px;
    position: absolute;
    z-index: 1;
  }
</style>
