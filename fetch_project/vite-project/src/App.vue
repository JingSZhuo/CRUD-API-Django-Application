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
            <tr v-for="(data, id_element) in formData['forms_dictionary']" :key="id_element">
              <td>{{data.id}}</td>
              <td>{{data.email}}</td>
              <td>{{data.username}}</td>
              <td>{{data.age}}</td>
              <td>{{data.date_posted}}</td>
              <td> <button class="btn btn-outline-danger px-3 py-2 m-auto" @click="deleteData(data.id)" >Delete</button> </td>
            </tr>
          </table>
        </div>
        <div class="d-flex flex-column justify-content-center w-75 m-auto p-5">
          <p>{{id_field}} {{ email_field }}  {{username_field}} {{age_field}} {{date_field}}</p>
          <input class="my-3" v-model="id_field" type="number" placeholder="ID">
          <input class="my-3" v-model="email_field" type="email" placeholder="Email">
          <input class="my-3" v-model="username_field" type="text" placeholder="Username">
          <input class="my-3" v-model="age_field" type="number" placeholder="Age">
          <input class="my-3" v-model="date_field" type="date" placeholder="Date">
          <div class="d-flex felx-row justify-content-center">
            <button class="btn btn-outline-primary px-5 py-2 m-auto" @click="postData"> Post </button>
            <button class="btn btn-outline-success px-5 py-2 m-auto" @click="putData(id_field, email_field, username_field, age_field, date_field)"> Edit </button>
          </div>
        </div>
</template>

<script>

export default {
  
  name: 'MainApp',
  data() {              //Stores data variables that are used in the template
    return  {
        formData: [],
        id_field: '',
        email_field: '',
        username_field: '',
        age_field: '',
        date_field: '',
    }
  },
  methods: {

    //function performs an AJAX request to fetch form data 

    async fetchData() {
      let response = await fetch("http://127.0.0.1:8000/main/data")    //Request object
      let data = await response.json()
      this.formData = data
    },

    //function sends a request object (POST Method) with the data to the JsonResponse page.
    //The form_api function receives the request (via parameters) and reads the body property for the data
    //Then appends the data to the database.
    //Finally returns a JsonResponse with the new DB 

    async postData () {
      const user_input = {
        email : this.email_field,
        username: this.username_field,
        age: this.age_field,
        date: this.date_field,
      }
      await fetch("http://127.0.0.1:8000/main/data" , {    //Request object
        method: 'POST',
        // mode: 'cors', 
        // credentials: 'same-origin',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user_input),
      })
      .then((response) => response.json())
      this.fetchData()      //Post new dataset after post request
    },

    //function gets user input via parameters and then sends request object (PUT method) with the body to the page
    //form_api function gets the ID of the row that requires updating and then returns a JsonResponse

    async putData (id, email, username, age, date) {

      const updated_data = {
        id_edit: id,
        updated_email : email,
        updated_username: username,
        updated_age: age,
        updated_date: date,
      }

      await fetch("http://127.0.0.1:8000/main/data" , {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updated_data),
      })
      .then((response) => (response.json()))
      .then(this.fetchData())
    },

    //sends a DELETE method to the form_api function view 
    //Identifies the ID to delete the row

    async deleteData (id_element) {
      const idObdj = {
        id: id_element
      }

      console.log("ID: ", id_element)
      await fetch("http://127.0.0.1:8000/main/data", {
        method: 'DELETE',
        headers: {
          'Content-Type' : 'application/json', 
        },
        body: JSON.stringify(idObdj),
      })
      .then((response) => response.json())
      .then(this.fetchData())
    }
  },
  mounted() {
    this.fetchData()
  }
}
</script>
