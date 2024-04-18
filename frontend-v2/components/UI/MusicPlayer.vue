<script setup>

const props = defineProps({
    sticky: Boolean
})

const { selectedAudio, isPlaying } = storeToRefs(useAudioStore())
const musicStore = useAudioStore();

// const audio = new Audio();

</script>

<template>
    <footer class="mt-auto bg-neutral" :class="{ 'fixed bottom-0 w-full' : props.sticky }">
        <div class="navbar">

            <div class="navbar-start">
                <div class="flex text-white">
                    <img :src="selectedAudio.image" class="justify-start h-24 w-24 m-4" />
                    <div class="flex flex-col mt-4">
                        <h4 class="text-lg font-semibold">{{ selectedAudio.title }}</h4>
                        <p class="text-sm font-light">{{ selectedAudio.artist }}</p>
                    </div>
                </div>
            </div>

            <div class="navbar-center">
                <div class="">
                    <div class="flex flex-col items-center justify-center m-4">

                        <div class="flex pb-5">
                            <button @click="musicStore.previousSong(selectedAudio.id)" class="">
                                <Icon size="2rem" name="ic:baseline-fast-rewind"
                                    class="text-white hover:text-sky-300 hover:transform hover:scale-110 transition duration-300" />
                            </button>

                            <button @click="musicStore.playAudio()" v-if="!isPlaying" class="mx-8">
                                <Icon size="3rem" name="ic:outline-play-circle-filled"
                                    class="text-white hover:text-info-content hover:transform hover:scale-110 transition duration-300" />
                            </button>
                            <button @click="musicStore.pauseAudio()" v-else class="mx-8">
                                <Icon size="3rem" name="ic:outline-pause-circle-filled"
                                    class="text-white hover:text-sky-300 hover:transform hover:scale-110 transition duration-300" />
                            </button>

                            <button @click="musicStore.nextSong(selectedAudio.id)" class="">
                                <Icon size="2rem" name="ic:baseline-fast-forward"
                                    class="text-white hover:text-sky-300 hover:transform hover:scale-110 transition duration-300" />
                            </button>
                        </div>

                        <div class="progress-container">

                            <div class="flex items-center justify-between">
                                <div class="flex items-center w-96">

                                    <span class="countdown text-white text-sm font-medium">{{formatTime(selectedAudio.currentTime) }}</span>

                                    <div class="relative flex-1 mx-4">

                                        <!-- Progress bar -->
                                        <progress
                                            class="progress progress-secondary w-full h-6 absolute top-0 left-0 appearance-none pointer-events-none"
                                            :value="selectedAudio.currentTime" :max="selectedAudio.duration"></progress>

                                        <!-- Input range -->
                                        <input type="range" min="0" :max="selectedAudio.duration"
                                            v-model="selectedAudio.currentTime" @input="musicStore.updateCurrentTime()"
                                            class="w-full h-6 opacity-0 cursor-pointer">

                                    </div>
                                    
                                    <span class="duration text-white text-sm font-medium">{{ formatTime(selectedAudio.duration) }}</span>

                                </div>
                            </div>

                        </div>


                    </div>
                </div>
            </div>

            <div class="navbar-end">
                <div class="w-48 pr-8">
                    <input type="range" min="0" max="100" v-model="selectedAudio.volume"
                        @input="musicStore.updateVolume()"
                        class="range range-secondary range-sm border border-secondary-200" />
                </div>
            </div>
        </div>
    </footer>

</template>

