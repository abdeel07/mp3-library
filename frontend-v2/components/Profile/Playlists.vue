<script setup>

const playlistStore = usePlaylistStore();

const props = defineProps({
    userPlaylists: Array,
})

const getBase64Image = (base64String) => {
    return `data:image/jpeg;base64,${base64String}`;
};

</script>

<template>
    <div>
        <div class="my-4 mx-12 py-4">

            <div class="flex flex-center mb-10">
                <div class="flex-1">
                    <h2 class="font-bold text-2xl">Playlists</h2>
                </div>
                <PlaylistsModal />
            </div>

            <!-- Show UIRiffCard if userRiffs exist -->
            <template v-if="userPlaylists && userPlaylists.length >= 6">
                <div class="flex items-center justify-center">

                    <div class="mr-20 flex items-center justify-center" v-if="playlistStore.loading"
                        v-for="skeleton in 6" :key="skeleton">
                        <UISkeletonCard />
                    </div>

                    <UIPlaylistCard v-else class="mr-16" v-if="userPlaylists"
                        v-for="(playlist, index) in userPlaylists.slice(0, 6)" :key="index" :name="playlist.name"
                        :image-src="getBase64Image(playlist.image)" :playlistId="playlist.id" />
                </div>
            </template>

            <!-- Show UIRiffCard without additional styling if userRiffs are less than 6 -->
            <template v-else>
                <div class="flex">

                    <div class="mr-20 flex items-center justify-center" v-if="playlistStore.loading"
                        v-for="skeleton in 6" :key="skeleton">
                        <UISkeletonCard />
                    </div>

                    <UIPlaylistCard v-else class="mr-16" v-if="userPlaylists" v-for="(playlist, index) in userPlaylists"
                        :key="index" :name="playlist.name" :image-src="getBase64Image(playlist.image)"
                        :playlistId="playlist.id" />
                </div>
            </template>

            <div class="flex flex-center mt-8">
                <div class="flex-1">
                </div>
                <NuxtLink  @click="navigateTo('playlists')" class="font-bold underline link">View Playlists</NuxtLink>
            </div>

        </div>

    </div>
</template>

