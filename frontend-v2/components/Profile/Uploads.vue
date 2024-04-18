<script setup>

const musicStore = useAudioStore();

const riffClicked = useState(() => false)

const props = defineProps({
    userRiffs: Array,
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
                    <h2 class="font-bold text-2xl">Riffs</h2>
                </div>
                <RiffsModal />
            </div>

            <!-- Show UIRiffCard if userRiffs exist -->
            <template v-if="userRiffs && userRiffs.length >= 6">
                <div class="flex items-center justify-center">

                    <div class="mr-20 flex items-center justify-center" v-if="musicStore.loading" v-for="skeleton in 6"
                        :key="skeleton">
                        <UISkeletonCard />
                    </div>

                    <UIRiffCard v-for="(riff, index) in userRiffs.slice(0, 6)" :key="index"
                        class="mr-16 flex items-center justify-center" :title="riff.title" :artist="riff.artist"
                        :image-src="getBase64Image(riff.image)" :audioString="riff.mp3_file" :audioId="riff.id"
                        :riff="riff" />
                </div>
            </template>

            <!-- Show UIRiffCard without additional styling if userRiffs are less than 6 -->
            <template v-else>
                <div class="flex">

                    <div class="mr-20 flex items-center justify-center" v-if="musicStore.loading" v-for="skeleton in 6"
                        :key="skeleton">
                        <UISkeletonCard />
                    </div>

                    <UIRiffCard v-for="(riff, index) in userRiffs" :key="index" class="mr-16" :title="riff.title"
                        :artist="riff.artist" :image-src="getBase64Image(riff.image)" :audioString="riff.mp3_file"
                        :audioId="riff.id" :riff="riff" />
                </div>
            </template>

            <div class="flex flex-center mt-8">
                <div class="flex-1">
                </div>
                <NuxtLink @click="navigateTo('riffs')" class="font-bold underline link">View Riffs</NuxtLink>
            </div>

        </div>

    </div>
</template>