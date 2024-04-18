<script setup>

const musicStore = useAudioStore();

musicStore.fetchUploads();

</script>

<template>
    <div class="flex flex-col h-screen">

        <ProfileUploads :userRiffs="musicStore.usersUploads" />
        <ProfilePlaylists />

        <UIMusicPlayer />
    </div>
</template>