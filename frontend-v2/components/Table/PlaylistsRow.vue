<script setup>

const props = defineProps({
    name: String,
    imageSrc: String,
    playlistId: Number,
    playlistNum: Number,
})

const playlistPath = `playlist/${props.playlistId}`

</script>

<template>
    <tr class="">
        <th>
            <span>{{ playlistNum }}</span>
        </th>
        <td>
            <div class="flex items-center gap-3">
                <div class="avatar">
                    <div class="mask mask-squircle w-16 h-16">
                        <img :src="imageSrc" alt="Riff Thumbnail" />
                    </div>
                </div>
                <div>
                    <div class="font-bold"><NuxtLink :to="playlistPath" class="font-bold link no-underline">{{ name }}</NuxtLink></div>
                </div>
            </div>
        </td>
        <td>
            <TableModalDeletePlaylist :playlist-id="playlistId" />
        </td>
    </tr>
</template>