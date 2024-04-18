<script setup>

const playlistStore = usePlaylistStore();

const props = defineProps({
    name: String,
    imageSrc: String,
    playlistId: Number,
})

const playPlaylist = () => {
    // if (musicStore.selectedAudio.id == Number) {
    //     musicStore.startAudio(props.audioId);
    // }  
    
    // if (musicStore.selectedAudio.id != Number) {
    //     musicStore.playOtherAudio(props.audioId);
    // }
}

const viewPlaylist = () => {
    navigateTo(`/playlist/${props.playlistId}`);
    playlistStore.searchUserPlaylist(props.playlistId);

}


</script>

<template>
    
    <div @click="viewPlaylist" class="relative mr-5 group transform transition-transform duration-600 ease-in-out hover:scale-105 hover:shadow-md cursor-pointer">

        <img class="h-56 w-56 object-cover rounded-md" :src="imageSrc" alt="Random image">
        <div
            class="absolute inset-0 bg-gray-700 opacity-0 rounded-md transition-opacity duration-300 group-hover:opacity-60">
        </div>
        <div class="absolute inset-0 flex flex-col opacity-0 transition-opacity duration-300 group-hover:opacity-100">
            <div class="flex flex-col p-4">
                <h3 class="text-2xl font-bold text-white">{{ name }}</h3>
            </div>
            <!-- <div class="p-3">
                <button @click="playRiff()" class="text-secondary">
                    <Icon size="3rem" name="ic:outline-play-circle-filled" color="bg-primary" />
                </button>
            </div> -->
        </div>
    </div>

</template>