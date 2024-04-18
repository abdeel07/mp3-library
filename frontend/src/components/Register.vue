<template>
    <!-- Button trigger modal -->
    <button type="button" class="btn header__sign-in" data-bs-toggle="modal" data-bs-target="#registerModal">
      Register
    </button>
  
    <!-- Modal -->
    <div class="modal fade" id="registerModal" tabindex="-1" aria-labelledby="registerModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="registerModalLabel">Register</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="mb-3">
                <label for="usernameInput" class="form-label">Username</label>
                <input type="text" class="form-control" id="usernameInput" aria-describedby="emailHelp" v-model="formData.username"/>
              </div>
              <div class="mb-3">
                <label for="passwordInput" class="form-label">Password</label>
                <input type="password" class="form-control" id="passwordInput" v-model="formData.password"/>
              </div>
              <div class="modal-footer pb-0">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary">Register</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import axios from "axios";
    
    const formData = ref({
        username: '',
        password: ''
    });
    
    function submitForm () {
        axios.post('http://localhost:5000/register', formData.value)
        .then(response => {
            console.log(response.data);
            formData.value.username = '';
            formData.value.password = '';
            window.location.href = "/";
        })
        .catch(error => {
            console.error('Error submitting form:', error);
        });
    }
  </script>
  