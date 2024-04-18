<template>
    <!-- Button trigger modal -->
    <button type="button" class="btn header__sign-in" data-bs-toggle="modal" data-bs-target="#addPlaylistModal">
      +
    </button>

    <!-- Modal -->
    <div class="modal fade" id="addPlaylistModal" tabindex="-1" aria-labelledby="addPlaylistModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="addPlaylistModalLabel">Add Playlist</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="submitForm">
                        <div class="mb-3">
                            <label for="nameInput" class="form-label">Name</label>
                            <input type="text" class="form-control" id="nameInput" v-model="formData.name"/>
                        </div>
                        
                        <div class="mb-3">
                            <label for="imageInput" class="form-label">Image</label>
                            <input type="file" class="form-control" id="imageInput" @change="handleImageChange"/>
                        </div>
                        <div class="modal-footer pb-0">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="submit" class="btn btn-primary">Add</button>
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
        name: '',
        image: null,
    });


    const submitForm = () => {
        const data = new FormData();
        data.append('name', formData.value.name);
        data.append('image', formData.value.image);
        data.append('user_id',localStorage.getItem("user_id"));

        axios.post('http://localhost:5000/playlist', data) 
            .then(response => {
                console.log("Response: ",response.data);
                window.location.href = "/";
            })
            .catch(error => {
                console.error('Error submitting form:', error);
            });
    }

    const handleImageChange = (event) => {
        formData.value.image = event.target.files[0];
    }
</script>
