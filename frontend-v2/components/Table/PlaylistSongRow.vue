<script setup>

const musicStore = useAudioStore();

const props = defineProps({
    title: String,
    artist: String,
    imageSrc: String,
    audioString: String,
    duration: Number,
    audioId: Number,
    audioNum: Number,
    playlistId: Number,
    playlistName: String,
})


const playRiff = () => {
    if (musicStore.selectedAudio.id == Number) {
        musicStore.startAudio(props.audioId);
    }

    if (musicStore.selectedAudio.id != Number) {
        musicStore.playOtherAudio(props.audioId);
    }
}

</script>

<template>
    <tr class="">
        <th class="relative">
            <div class="group">
                <span>
                    <Icon @click="playRiff" size="2rem" name="ic:outline-play-circle-filled"
                        class="text-netural hover:transform hover:scale-110 transition duration-300" />
                </span>
            </div>
        </th>
        <th>
            <span>{{ audioNum }}</span>
        </th>
        <td>
            <div class="flex items-center gap-3">
                <div class="avatar">
                    <div class="mask mask-squircle w-16 h-16">
                        <img :src="imageSrc" alt="Riff Thumbnail" />
                    </div>
                </div>
                <div>
                    <div class="font-bold">{{ title }}</div>
                    <div class="text-sm opacity-50">{{ artist }}</div>
                </div>
            </div>
        </td>
        <th>
            <TableModalDeleteRiffFromPlaylist :audio-Id="audioId" />
        </th>
    </tr>
</template>