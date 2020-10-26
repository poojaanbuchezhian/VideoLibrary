<template>
  <div class="">
    <div class="row">
      <div class="col-md-5 text-center nicefont">
        <h4>Welcome to Youtube Rater</h4>
          <p v-bind:key="video.id" v-for="video in videos">
               {{video.title}}
               <br>
               Rating: {{video.rating_average}}
               <br>
            <button class="btn-sm btn-primary mt-2 mb-3">Details</button>
          </p>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'Home',
  components: {

  },
  data() {
    return {
      videos : [],
    }
  },
  methods: {
    getVideos() {
      axios.get("http://127.0.0.1:8000/api/videos/")
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err));
    }
  },
  created() {
    this.getVideos();
    createNew: false;
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Alatsi&display=swap');
.nicefont{
  font-size:26px;
  font-family: 'Alatsi', sans-serif;
}
</style>
