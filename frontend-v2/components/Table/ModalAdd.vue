<script setup>

const audioStore = useAudioStore();
const playlistStore = usePlaylistStore();

const selectedPlaylist = ref(null);
const modalVisible = ref(false);

const props = defineProps({
    audioId: Number,
    playlistId: Number,
    playlistName: String,
})

const setSelectedID = () => {
    modalVisible.value = true;
    audioStore.audioEditId = props.audioId;
}

const onSubmit = async () => {
    console.log(audioStore.audioEditId);
    console.log(selectedPlaylist.value);
    modalVisible.value = false;

    try {
        const data = await $fetch(`http://localhost:5000/playlist/${selectedPlaylist.value}/${audioStore.audioEditId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        })

        return data.value;

    } catch (error) {
        console.error("Error: ", error);
    }
}


watch(selectedPlaylist, (newValue) => {
  console.log('Selected playlist ID:', newValue);
});

</script>

<template>
    <!-- The button to open modal -->
    <label @click="setSelectedID()" for="add_modal"
        class="mr-2 btn text-center btn-success btn-xs font-bold">Add</label>

    <!-- Put this part before </body> tag -->
    <input type="checkbox" id="add_modal" class="modal-toggle" v-if="modalVisible" />
    <div class="modal" role="dialog">
        <div class="modal-box">
            <form method="dialog">
                <label for="add_modal" class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</label>
            </form>
            <div class="">
                <h3 class="text-left font-bold text-lg p-4">Add Riff</h3>
            </div>
            <div class="flex flex-col items-center justify-center">
                <div>

                    <label class="form-control w-full my-4">
                        <div class="label">
                            <span class="label-text">Pick a Playlist</span>
                        </div>
                        <select v-model="selectedPlaylist" aria-placeholder="ds" class="select select-bordered">
                            <option disabled selected>Pick a Playlist</option>
                            <option v-for="(playlist, index) in playlistStore.userPlaylists":key="index" :value="playlist.id">{{playlist.name}}</option>
                        </select>
                        <div class="label">
                        </div>
                    </label>

                    <p class="p-4 text-base font-semibold">Are you sure you want to add this to the Playlist?</p>
                    <button @click="onSubmit" class="btn btn-neutral w-full hover:btn-success my-4">Add Riff</button>
                </div>
            </div>
        </div>
    </div>
</template>
