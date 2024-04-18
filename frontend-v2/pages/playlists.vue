<script setup>

const audioStore = useAudioStore();
const playlistStore = usePlaylistStore();

playlistStore.fetchPlaylists();


</script>

<template>
    <div class="">
        <div class="flex flex-col items-center justify-center">
            <h1 class="text-5xl font-black p-12">Your Playlists</h1>
        </div>

        <template v-if="audioStore.selectedAudio.id != Number">
            <div>
                <div>
                    <div class="overflow-x-auto mx-64">
                        <table class="table">
                            <!-- head -->
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Playlist</th>
                                    <th>Delete Playlist</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- row 1 -->
                                <TablePlaylistsRow v-for="(playlist, index) in playlistStore.userPlaylists" :key="index"
                                    :playlist-num="index + 1" :playlist-id="playlist.id"
                                    :image-src="getBase64Image(playlist.image)" :name="playlist.name" />
                            </tbody>
                            <!-- foot -->
                            <tfoot>
                                <tr>

                                </tr>
                            </tfoot>

                        </table>
                    </div>

                </div>

                <UIMusicPlayer :sticky="true" />

            </div>
        </template>

        <template v-else>
            <div>
                <div>
                    <div class="overflow-x-auto mx-64">
                        <table class="table">
                            <!-- head -->
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Playlist</th>
                                    <th>Delete Playlist</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- row 1 -->
                                <TablePlaylistsRow v-for="(playlist, index) in playlistStore.userPlaylists" :key="index"
                                    :playlist-num="index + 1" :playlist-id="playlist.id"
                                    :image-src="getBase64Image(playlist.image)" :name="playlist.name" />
                            </tbody>
                            <!-- foot -->
                            <tfoot>
                                <tr>

                                </tr>
                            </tfoot>

                        </table>
                    </div>

                </div>

            </div>
        </template>

    </div>
</template>