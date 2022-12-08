<div class="content-inset">
    <p>
        This application is a binary image classifier which will determine
        whether you belong on the light side or the dark side of tech. Once the
        user takes their photo and submits it, the image is classified against
        our current learned data and will determine your score. A 'faceswap'
        will then place your face onto a character matching your alignment.
    </p>
    <p>
        Our goal in this application was to demonstrate an end-to-end ML
        pipeline with convolutional, generational, and transformational steps.
    </p>
    <div class="full-width-img">
        <figure>
            <img
                src="/classifier.jpg"
                alt="classifier diagram showing steps and layers"
            />
            <figcaption>
                This is an oversimplified diagram of a convolutional classifier.
                There are a ton of diagrams I could have put here but this one
                matched the colors.
            </figcaption>
        </figure>
    </div>
    <p>
        The technologies used for this application included TensorFlow, AWS,
        PyTorch, and OpenCV.
    </p>
    <div class="full-width-img">
        <img
            class="logo"
            src="/Tensorflow_logo.svg.png"
            alt="TensorFlow logo"
        />
        <img class="logo" src="/Pytorch_logo.png" alt="PyTorch logo" />
        <img
            class="logo"
            src="/195px-OpenCV_Logo_with_text.png"
            alt="OpenCV logo"
        />
    </div>
    <p>
        Special thanks for contributions on this application go to technical
        mentors Dan Christopherson and Justin Montgomery. Also to the Creative
        Community at nvisia for designing a UX pathway for the application user
        and Shauna Fowler for the UI Design.
    </p>
    Things that went wrong:
    <ol>
        <li>
            I wanted to use Dressing In Order (DiOr), a Virtual Try-on (VTON)
            network, to do a re-dressing of the person's whole body image with
            Star Wars costumes. That didn't work because DiOr doesn't offer
            pretrained models.
        </li>
        <li>
            The faceswap is still too slow. It takes 30-60 seconds, which
            sometimes causes Amazon CloudFront's proxy to timeout.
        </li>
        <li>
            Amazon Elastic Container Services is probably the wrong tool for the
            job, here. I should have gone with a Kubernetes cluster.
        </li>
        <li>
            I should have broken the "faceswap" container into separate
            "dispatcher" container and "faceswap" container to isolate the
            GPU-bound load.
        </li>
    </ol>
    Things I learned:
    <ol>
        <li>
            There's a reason Amazon certifies people just for having knowledge
            of the product catalog.
        </li>
        <li>OpenCV is really slick to work with.</li>
        <li>
            Containerizing GPU-bound loads is easy. Finding somewhere to run
            GPU-bound containerized loads is not.
        </li>
        <li>CUDA versioning is painful to deal with.</li>
        <li>When in doubt, use more containers. One concern per container.</li>
    </ol>
</div>

<style>
    div.content-inset {
        max-width: 666px;
        margin: auto;
        margin-top: 40px;
    }

    div.full-width-img {
        background-color: white;
        max-width: 666px;
        display: flex;
        justify-content: space-around;
        margin: auto;
    }

    div.full-width-img img {
        max-width: 100%;
        display: block;
    }

    div.full-width-img img.logo {
        max-width: 200px;
        max-height: 50px;
        vertical-align: middle;
    }
</style>
