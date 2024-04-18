<template>
    <Header />
    <Hero />
    
    <div class="container">
        <div class="row" v-if="isLoggedIn">
            <div class="col-5">
                <Library :totalPlaylists="totalPlaylists" :totalFavorits="totalFavorits" :totalUploads="totalUploads" :playlists="playlists.data" @fetchUploads="fetchUploads" @fetchFavorits="fetchFavorits" @fetchPlaylistById="fetchPlaylistById"/> 
            </div>
            <div class="col-7">
                <List :playlists="playlists.data" :listData="data.music" :title="title" @fetchUploads="fetchUploads" @fetchFavorits="fetchFavorits" @setCurrentMusic="setCurrentMusic" @shuffle="shuffle"/>
            </div>
        </div>
        <!-- <h2 class="center_item" v-else>Try Making an Account!</h2> -->
    </div>

    <Player :queue="data.music" :current="currentMusic" />
</template>
<script setup>
    import Header from './components/Header.vue';
    import Hero from './components/Hero.vue';
    import Library from './components/Library.vue';
    import List from './components/List.vue';
    import Player from './components/Player.vue';
    import { ref, onMounted } from 'vue';

    const isLoggedIn = typeof localStorage !== 'undefined' && localStorage.getItem("user_id");

    const uploads = ref([]);
    const playlists = ref([]);
    const data = ref([]);
    const currentMusic = ref(null);

    const totalUploads = ref(0);
    const totalFavorits = ref(0);
    const totalPlaylists = ref(0);

    const title = ref("My Uploads");
    
    onMounted(async () => {
        await fetchFavorits();
        await fetchUploads();
        await fetchPlaylists();
    });

    async function fetchFavorits(){
        try {
            const response = await fetch(`http://localhost:5000/user/${localStorage.getItem("user_id")}/favorits`);
            
            if (!response.ok) {
                throw new Error('Failed to fetch playlists');
            }
            data.value = await response.json();
            title.value = "My Likes";
            console.log("Favorits: ",data.value);
            totalFavorits.value = data.value.music.length;
        } catch (error) {
            console.error('Error fetching playlists:', error);
        }
    }
    function setCurrentMusic(music){
        currentMusic.value = music;
    }
    function shuffle(){
        data.value.music = [...data.value.music].sort(() => Math.random() - 0.5);
    }
    async function fetchPlaylists(){
        try {
            const response = await fetch(`http://localhost:5000/user/${localStorage.getItem("user_id")}/playlists`);
            
            if (!response.ok) {
                throw new Error('Failed to fetch playlists');
            }
            playlists.value = await response.json();
            console.log("Playlists: ",playlists.value);
            totalPlaylists.value = playlists.value.data.length;
        } catch (error) {
            console.error('Error fetching playlists:', error);
        }
    }
    async function fetchUploads(){
        try {
            const response = await fetch(`http://localhost:5000/user/${localStorage.getItem("user_id")}/music`);
            
            if (!response.ok) {
                throw new Error('Failed to fetch uploads');
            }
            data.value = await response.json();
            title.value = "My Uploads";
            console.log("Uploads: ",data.value);
            totalUploads.value = data.value.music.length
        } catch (error) {
            console.error('Error fetching uploads:', error);
        }
    }
    async function fetchPlaylistById(playlist_id,name){
        console.log("fetch playlist by id: ",playlist_id);
        try {
            const response = await fetch(`http://localhost:5000/playlist/${playlist_id}/music`)
            
            if (!response.ok) {
                throw new Error('Failed to fetch playlist');
            }
            data.value = await response.json();
            title.value = name;
            console.log(`Playlist ${playlist_id}: ${data.value}`);
        } catch (error) {
            console.error('Error fetching playlist:', error);
        }
    }
</script>