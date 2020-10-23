<template>
  <div class="">
    <div class="row">
      <div class="col-md-5 text-center ">
        <h4>Welcome to Youtube Rater</h4>
      </div>
      <button v-on:click="getVideos">Get my first videos</button>
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
  }
}
</script>
