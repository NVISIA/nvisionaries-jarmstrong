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

<div class="content-inset">
    <p>This application is a binary image classifier which will determine whether you belong on the light side or the dark side of tech.  Once the user takes their photo and submits it, the image is classified against our current learned data and will determine your score.  A 'faceswap' will then place your face onto a character matching your alignment.</p>
    <p>Our goal in this application was to demonstrate an end-to-end ML pipeline with convolutional, generational, and transformational steps.</p>
    <div class="full-width-img"><img src="/classifier.jpg" alt="classifier diagram showing steps and layers"></div>
    <p>The technologies used for this application included TensorFlow, AWS, PyTorch, and OpenCV.</p>
    <div class="full-width-img">
        <img class="logo" src="/Tensorflow_logo.svg.png" alt="TensorFlow logo">
        <img class="logo" src="/Pytorch_logo.png" alt="PyTorch logo">
        <img class="logo" src="/195px-OpenCV_Logo_with_text.png" alt="OpenCV logo">
    </div>
    <p>Special thanks for contributions on this application go to technical mentors Dan Christopherson and Justin Montgomery. Also to the Creative Community at nvisia for designing a UX pathway for the application user and Shauna Fowler for the UI Design.</p>
</div>