<template>
  <img alt="Vue logo" src="./assets/logo.png" class="position-relative m-20">
      <h1 class="h1">Form Data</h1>
        <div class="p-5">
          <table class="table border border-success">
            <tr class="table border border-warning ">
              <th class="table-success">ID</th>
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
        <div class="d-flex flex-column justify-content-center w-75 m-auto p-5">
          <p> {{ email_field }}  {{username_field}} {{age_field}} {{date_field}}</p>
          <input class="my-3" v-model="email_field" type="email" placeholder="Email">
          <input class="my-3" v-model="username_field" type="text" placeholder="Username">
          <input class="my-3" v-model="age_field" type="number" placeholder="Age">
          <input class="my-3" v-model="date_field" type="date" placeholder="Date">
          <button class="btn btn-outline-primary px-5 py-2 m-auto" @click="postData"> Post </button>
        </div>
</template>

<script>

export default {
  
  name: 'MainApp',
  data() {              //Stores data variables that are used in the template
    return  {
        formData: [],
        email_field: 'aaa@gmail.com',
        username_field: 'username00',
        age_field: '32',
        date_field: '2333-23-11',
    }
  },
  methods: {
    async fetchData() { //perform an AJAX request to fetch form data
      let response = await fetch("http://127.0.0.1:8000/main/data")
      let data = await response.json()
      this.formData = data
    },
    async postData () {
      const input = {
        email : this.email_field,
        username: this.username_field,
        age: this.age_field,
        date: this.date_field,
      }
      await fetch("http://127.0.0.1:8000/main/data" , {
        method: 'POST',
        mode: 'no-cors', 
        credentials: 'same-origin',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(input),
      })
      .then((response) => response.json())
      .then((data) => {
        console.log("Data: ", data)
      })
      .catch(console.log("Error", input))
    },
  },
  mounted() {
    this.fetchData()
  }
}
</script>
