<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <div>
    HELLO WORLD
      <div>
        {{form_data}}
      </div>
  </div>
</template>

<script>
export default {
  name: 'MainApp',
  data() {
    return{
        form_data : []
    }
  },
  method: {
    async fetchData() { //perform an AJAX request to fetch form data
      let response = await fetch("http://localhost:8080/main/data")
      let data = response.json()

      this.form_data = data.form_data
    }
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
