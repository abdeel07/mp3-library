<template>
    <div class="list">
      <div class="list__header">
        <div class="list__header-title">{{ title }}</div>
        <div class="list__header-controls">
          <div class="control play" @click="setCurrentMusic(listData[0])"><img src="@/assets/images/play.png" /></div>
          <div class="control shuffle" @click="shuffle"><img src="@/assets/images/shuffle.png" /></div>
          <!-- <div class="control download"><img src="@/assets/images/download.png" /></div> -->
        </div>
      </div>
      <div class="list__items">
        <div class="list__item" v-for="(item, index) in listData" :key="index" @click="setCurrentMusic(item)">
          <div class="list__item-id">{{ index + 1 }}</div>
          <div class="list__item-image">
            <img :src="getBase64Image(item.image)" alt="">
          </div>
          <div class="list__item-like">
            <img src="@/assets/images/heart.png" v-if="item.like" @click="handleDisLike(item.id,item.like)"/>
            <img src="@/assets/images/heart_empty.png" v-else @click="handleLike(item.id,item.like)" />
          </div>
          <div class="list__item-title">{{ item.title }}</div>
          <div class="list__item-artist">{{ item.artist }}</div>
          <div class="list__item-add-list">
            <img src="@/assets/images/add-list.png" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"/>
            <div class="dropdown">
              <ul class="dropdown-menu">
                <li v-for="(playlist,index) in playlists" :key="index" class="dropdown-item" @click="addMusicToPlaylist(item.id,playlist.id)">
                  {{ playlist.name }}
                </li>
              </ul>
            </div>
          </div>
          <div class="list__item-delete-music">
            <img src="@/assets/images/trash.png" @click="deleteMusic(item.id)"/>
          </div>

        </div>
      </div>
    </div>
</template>
  
<script setup>
    import { defineProps } from 'vue';
    import axios from 'axios';
    const emit = defineEmits(['fetchFavorits','fetchUploads','setCurrentMusic','shuffle']);

    function getBase64Image(base64String) {
        return `data:image/jpeg;base64,${base64String}`;
    };

    function getBase64Audio(base64String) {
        return `data:audio/mp3;base64,${base64String}`;
    }
    const deleteMusic =  async (id) =>{
        console.log("delete:",id);
        axios.delete(`http://localhost:5000/music/${id}`)
        .then((response)=>{
            window.location.href = "/";
        })
        .catch (error=> {
            console.error('Error deleting music:', error);
        });
    }
    function addMusicToPlaylist(music_id,playlist_id){
      console.log(`Add Music ${music_id} to the Playlist: ${playlist_id}`);
      try {
            axios.post(`http://localhost:5000/playlist/${playlist_id}/add_music`,{"music_id":music_id})
            .then((response)=>{
              window.location.href = "/";
            })
            .catch(err=>console.log(err))
            
        } catch (error) {
            console.error('Error adding music to playlist:', error);
      }
    }

    async function handleDisLike(id){
      console.log(`Dislike the music ${id}`);
      try {
            const response = await fetch(`http://localhost:5000/music/${id}/remove_fav`,{method:"POST"});
            
            if (!response.ok) {
                throw new Error('Failed to dislike the music');
            }
            window.location.href = "/";
        } catch (error) {
            console.error('Error disliking the music:', error);
      }
    }

    async function handleLike(id){
      try {
            const response = await fetch(`http://localhost:5000/music/${id}/add_fav`,{method:"POST"});
            
            if (!response.ok) {
                throw new Error('Failed to like the music');
            }
            window.location.href = "/";
        } catch (error) {
            console.error('Error liking the music:', error);
      }
    }

    const props = defineProps({
        listData: {
          type: Array,
        },
        title: {
          type: String,
        },
        playlists:{
            type: Array,
        }
    });
    
    function setCurrentMusic(music){
      emit("setCurrentMusic",music);
    }

    function shuffle(){
      emit("shuffle");
    }
    
</script>
  