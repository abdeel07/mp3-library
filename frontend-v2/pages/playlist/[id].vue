<script setup>

const audioStore = useAudioStore();
const playlistStore = usePlaylistStore();

const route = useRoute();

playlistStore.searchUserPlaylist(route.params.id);

if (playlistStore.selectedPlaylist != null) {
    playlistStore.getPlaylistSongs(route.params.id)
}


</script>

<template>
    <div>
        <div class="flex items-center justify-center m-4 p-4">
            <img class="h-64 w-64 mask mask-square rounded-md"
                :src="getBase64Image(playlistStore.selectedPlaylist.image)" alt="Playlist Thumbnail">
            <h1 class="text-5xl font-black p-12">{{ playlistStore.selectedPlaylist.name }}</h1>
        </div>

        <template v-if="audioStore.selectedAudio.id != Number">
            <div>
                <div class="overflow-x-auto mx-64 my-8">
                    <table class="table">
                        <!-- head -->
                        <thead>
                            <tr>
                                <th></th>
                                <th>#</th>
                                <th>Riff</th>
                                <th>Delete From Playlist</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- row 1 -->
                            <TablePlaylistSongRow v-for="(riff, index) in playlistStore.playlistSongs" :key="index"
                                :audioNum="index + 1" :audio-id="riff.id" :audio-string="getBase64Audio(riff.mp3_file)"
                                :image-src="getBase64Image(riff.image)" :title="riff.title" :artist="riff.artist" />
                        </tbody>
                        <!-- foot -->
                        <tfoot>
                            <tr>

                            </tr>
                        </tfoot>

                    </table>
                </div>

                <UIMusicPlayer :sticky="true"/>

            </div>
        </template>

        <template v-else>
            <div>
                <div class="overflow-x-auto mx-64">
                    <table class="table">
                        <!-- head -->
                        <thead>
                            <tr>
                                <th></th>
                                <th>#</th>
                                <th>Riff</th>
                                <th>Delete From Playlist</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- row 1 -->
                            <TablePlaylistSongRow v-for="(riff, index) in playlistStore.playlistSongs" :key="index"
                                :audioNum="index + 1" :audio-id="riff.id" :audio-string="getBase64Audio(riff.mp3_file)"
                                :image-src="getBase64Image(riff.image)" :title="riff.title" :artist="riff.artist" />
                        </tbody>
                        <!-- foot -->
                        <tfoot>
                            <tr>

                            </tr>
                        </tfoot>

                    </table>
                </div>

            </div>
        </template>

    </div>
</template>