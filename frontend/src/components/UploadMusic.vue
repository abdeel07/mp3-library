<template>
    <!-- Button trigger modal -->
    <button type="button" class="btn header__sign-in" data-bs-toggle="modal" data-bs-target="#uploadMusicModal">
      +
    </button>

    <!-- Modal -->
    <div class="modal fade" id="uploadMusicModal" tabindex="-1" aria-labelledby="uploadMusicModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="uploadMusicModalLabel">Upload Music</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="submitForm">
                        <div class="mb-3">
                            <label for="titleInput" class="form-label">Title</label>
                            <input type="text" class="form-control" id="titleInput" v-model="formData.title"/>
                        </div>
                        <div class="mb-3">
                            <label for="artistInput" class="form-label">Artist</label>
                            <input type="text" class="form-control" id="artistInput" v-model="formData.artist"/>
                        </div>
                        <div class="mb-3">
                            <label for="imageInput" class="form-label">Image</label>
                            <input type="file" class="form-control" id="imageInput" @change="handleImageChange"/>
                        </div>
                        <div class="mb-3">
                            <label for="musicInput" class="form-label">MP3 file</label>
                            <input type="file" class="form-control" id="musicInput" @change="handleMp3FileChange"/>
                        </div>
                        <div class="modal-footer pb-0">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="submit" class="btn btn-primary">Upload</button>
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
    title: '',
    artist: '',
    image: null,
    mp3_file: null
});

const submitForm = () => {
    const data = new FormData();
    data.append('title', formData.value.title);
    data.append('artist', formData.value.artist);
    data.append('image', formData.value.image);
    data.append('mp3_file', formData.value.mp3_file);
    data.append('user_id',localStorage.getItem("user_id"));
    axios.post('http://localhost:5000/music', data) 
        .then(response => {
            console.log("Response: ",response.data);
            window.location.href = "/";
        })
        .catch(error => {
            console.error('Error submitting form:', error);
        });
}

const handleImageChange = (event) => {
    formData.value.image = event.target.files[0]; // Update image property with selected file
}

const handleMp3FileChange = (event) => {
    formData.value.mp3_file = event.target.files[0]; // Update mp3_file property with selected file
}
</script>
