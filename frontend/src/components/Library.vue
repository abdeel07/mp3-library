<template>
    <div class="library">
        <div class="library__header">
            <div class="library__header-title">Library</div>
            <!-- <div class="library__header-add"><img src="assets/images/plus.png"/></div> -->
        </div>
        <div class="library__list">
            <div class="library__list-item active mb-2" @click="callFetchUploads">
                <div class="library__list-item-image"><img src="@/assets/images/upload.png"/></div>
                <div class="library__list-item-content">
                    <div class="library__list-item-title">Uploads</div>
                    <div class="library__list-item-subtitle">Total • {{ totalUploads }} songs</div>
                </div>
                <div class="library__list-item-addPlaylist">
                    <UploadMusic />
                </div>
            </div>
            <div class="library__list-item active mb-2" @click="callFetchFavorits">
                <div class="library__list-item-image"><img src="@/assets/images/heart.png"/></div>
                <div class="library__list-item-content">
                    <div class="library__list-item-title">Likes</div>
                    <div class="library__list-item-subtitle">Total • {{ totalFavorits }} songs</div>
                </div>
            </div>
            <div class="library__list-item mb-2">
                <div class="library__list-item-image"><img src="@/assets/images/playlist.png"/></div>
                <div class="library__list-item-content">
                    <div class="library__list-item-title">Playlists</div>
                    <div class="library__list-item-subtitle">Total • {{ totalPlaylists }} playlists</div>
                </div>
                <div class="library__list-item-addPlaylist">
                    <AddPlaylist />
                </div>
            </div>
            <div class="sub__list ml-5">
                <div class="library__list-item active mb-2" v-for="(playlist,index) in playlists" :key="index" @click="callFetchPlaylistById(playlist.id,playlist.name)">
                    <div class="library__list-item-image"><img :src="getBase64Image(playlist.image)" class="playlist-img"/></div>
                    <div class="library__list-item-content d-flex align-items-center justify-content-between">
                  
                        <div class="library__list-item-title">{{ playlist.name }}</div>
                        <img src="@/assets/images/trash.png" @click="deletePlaylist(playlist.id)"/>
                        <!-- <div class="library__list-item-subtitle">Total • * songs</div> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import UploadMusic from './UploadMusic.vue';
    import AddPlaylist from './AddPlaylist.vue';
    import axios from 'axios';

    const emit = defineEmits(['fetchFavorits','fetchUploads','fetchPlaylistById']);

    const callFetchFavorits = () =>{
        emit("fetchFavorits");
    }
    const callFetchUploads = () =>{
        emit("fetchUploads");
    }

    const deletePlaylist =  async (id) =>{
        console.log("delete:",id);
        axios.delete(`http://localhost:5000/playlist/${id}`)
        .then((response)=>{
            window.location.href = "/";
        })
        .catch (error=> {
            console.error('Error fetching playlists:', error);
        });
    }

    const callFetchPlaylistById = (playlist_id,name) =>{
        emit("fetchPlaylistById",playlist_id,name)
    }
    function getBase64Image(base64String) {
        return `data:image/jpeg;base64,${base64String}`;
    };

    const props = defineProps({
        playlists:{
            type: Array,
        },
        totalUploads:{
            type:Number
        },
        totalFavorits:{
            type:Number
        },
        totalPlaylists:{
            type:Number
        }
    })
</script>