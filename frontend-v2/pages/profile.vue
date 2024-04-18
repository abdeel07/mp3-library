<script setup>

const musicStore = useAudioStore();
const playlistStore = usePlaylistStore();

if (musicStore.usersUploads.length === 0) {
    musicStore.fetchUploads();
}

if (playlistStore.userPlaylists.length === 0) {
    playlistStore.fetchPlaylists();
}


</script>

<template>
    <template v-if="musicStore.selectedAudio.id != Number">
        <div class="flex flex-col h-screen">
            <ProfileUploads :userRiffs="musicStore.usersUploads" />
            <ProfilePlaylists class="pb-32" :userPlaylists="playlistStore.userPlaylists" />
            <UIMusicPlayer :sticky="true" />
        </div>
    </template>

    <template v-else>
        <div class="flex flex-col h-screen">
            <ProfileUploads :userRiffs="musicStore.usersUploads" />
            <ProfilePlaylists :userPlaylists="playlistStore.userPlaylists" />
        </div>
    </template>
</template>
