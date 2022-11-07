<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <div>
      <h1>Form Data</h1>
      <div>
        <!-- <div>{{formData}}</div> -->
        <!-- <button @click="fetchData">Load Table</button> -->
        <div>
          <table class="position-relative left-100 top-200">
            <tr>
              <th>ID</th>
              <th>Email</th>
              <th>Username</th>
              <th>Age</th>
              <th>Date Posted</th>
            </tr>
            <tr v-for="(data, id) in formData['forms_dictionary']" :key="id">
              <td>{{data.id}}</td>
              <td>{{data.email}}</td>
              <td>{{data.username}}</td>
              <td>{{data.age}}</td>
              <td>{{data.date_posted}}</td>
            </tr>
          </table>
        </div>
      </div>
  </div>
</template>

<script>

export default {
  name: 'MainApp',
  data() {       //Stores data variables
    return  {
        formData: [],
    }
  },
  methods: {
    async fetchData() { //perform an AJAX request to fetch form data
      let response = await fetch("http://127.0.0.1:8000/main/data")
      let data = await response.json()
      this.formData = data
      
    },
  },
  mounted() {
    this.fetchData()
  }
}
</script>

<style>
#app {            /*Found in public folder */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
