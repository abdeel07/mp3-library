<script setup>
const audioStore = useAudioStore();
const playlistStore = usePlaylistStore();

audioStore.fetchUploads();
playlistStore.fetchPlaylists();


</script>

<template>
    <div class="">
        <div class="flex flex-col items-center justify-center">
            <h1 class="text-5xl font-black p-12">Your Riffs</h1>
        </div>

        <template v-if="audioStore.selectedAudio.id != Number">
            <div>
                <div class="overflow-x-auto mx-64">
                    <table class="table">
                        <!-- head -->
                        <thead>
                            <tr>
                                <th></th>
                                <th>#</th>
                                <th>Riff</th>
                                <th>Add to Playlist</th>
                                <th>Delete Riff</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- row 1 -->
                            <TableRiffsRow v-for="(riff, index) in audioStore.usersUploads" :key="index"
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

                <UIMusicPlayer :sticky="true" />

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
                                <th>Add Riff</th>
                                <th>Delete Riff</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- row 1 -->
                            <TableRiffsRow v-for="(riff, index) in audioStore.usersUploads" :key="index"
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