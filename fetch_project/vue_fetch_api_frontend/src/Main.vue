<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <div>
      <h1>Form Data</h1>
      <div>
        <div>{{formData}}</div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'MainApp',
  data() {
    return  {
        formData: [],
    }
  },
  methods: {
    async fetchData() { //perform an AJAX request to fetch form data
      let response = await fetch("http://127.0.0.1:8000/main/data")
      let data = await response.json()
      //console.log(data, "OK")
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
