<template>
  <div class="">
    <div class="row">
      <div class="col-md-10 "  >
        <p class="mb-3">Title: {{videodetail.title}}</p>
        <p>Description: {{videodetail.description}}</p>
        <p>Rating: {{videodetail.rating_average}}</p>
        <p>Comments: {{videodetail.comments_list}}</p>
        <p>Category: {{videodetail.category}}</p>
      </div>
    </div>
    <form id="formvideo" @submit.prevent="giveRating1" @submit="$emit('updated',videodetail)">
  <p>
    <label for="stars"> Give a Rating</label>
    <input class ="ml-2" type="text" name="stars" id="stars" v-model="stars">
  </p>
  <p>
    <label for="comments"> Comments</label>
    <input class ="ml-2" type="text" name="comments" id="comments" v-model="comments">
  </p>
  <p>
    <input class="btn-primary" type="submit" value="Submit Rating">
  </p>
</form>
    <button class="btn-sm btn-danger mt-2 mb-3" v-on:click="videoDelete(videodetail)" @click="$emit('deleted',videodetail)">Delete Video</button>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import { TokenService } from '../storage/service'

export default {
  name: 'VideoDetails',
  components: {

  },
  props: {
    videodetail: {}
  },
  data() {
    return {
    stars: '',
    comments:'',
    }
  },
  methods: {
  videoDelete(videodetail) {
    console.log(this.token)
    var postData = {
    video: this.videodetail.id,
    };
    let axiosConfig = {
      headers: {
        'Authorization': 'Token '+ this.token
      }
    };
    axios.delete(`http://127.0.0.1:8000/api/videos/${this.videodetail.id}`,axiosConfig)
    .then(res => console.log(res.data))
    .catch(err => console.log(err))
  },
  giveRating1(stars,comments) {
      this.token = TokenService.getToken()
      console.log(this.videodetail.id)
      var postData = {
        stars: this.stars,
        comments: this.comments,
      };
      let axiosConfig = {
        headers: {
          'Authorization': 'Token ' + this.token
        }
      };
      axios.post(`http://127.0.0.1:8000/api/videos/${this.videodetail.id}/rate_video/`, postData,axiosConfig)
      .then(res => console.log(res.data))
      .catch(err => console.log(err))
    }
  },
  created() {
   let token;
   this.token = TokenService.getToken();
 }
}
</script>

<style scoped>

</style>
