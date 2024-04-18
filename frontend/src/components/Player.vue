<template>
    <div class="player" v-if="isLoggedIn">
        <!-- <div class="player__music">
            <div class="player__music-image">
                <img :src="getBase64Image(current?.image)"/>
                
            </div>
            <div class="player__music-content">
                <div class="player__music-title">{{ this.current?.title }}</div>
                <div class="player__music-artist">{{ current?.artist }}</div>
            </div>
            <div class="player__music-like"><img src="@/assets/images/plus.png"/></div>
        </div> -->
        <div class="player__contols">
            <div class="player__contols-btns">
                <div class="player__btn-suffle" @click="shuffle">
                    <img src="@/assets/images/shuffle.png"/>
                </div>
                <div class="player__btn-prev" @click="playPrevious">
                    <img src="@/assets/images/previous.png"/>
                </div>
                <div class="player__btn-play" @click="play" v-if="isPlaying">
                    <img src="@/assets/images/pause.png"/>
                </div>
                <div class="player__btn-play" @click="play" v-else>
                    <img src="@/assets/images/play-button.png"/>
                </div>
                <div class="player__btn-next" @click="playNext">
                    <img src="@/assets/images/next.png" />
                </div>
                <div class="player__btn-repeat" @click="repeat">
                    <img src="@/assets/images/repeat.png"/>
                </div>
            </div>
            <div class="player__contols-progress">
                <!-- <div class="player__contols-progress-time">1:22</div> -->
                <div class="player__contols-progress-bar">
                    <!-- <progress value="3" max="10"></progress> -->
                    
                    <audio ref="audioPlayer" controls></audio>
                </div>
                <!-- <div class="player__contols-progress-time-total">2:15</div> -->
            </div>
        </div>
        <!-- <div class="player__volume">
            <img src="@/assets/images/volume.png" alt="">
            <progress value="3" max="10"></progress>
            <div>{{ queue?.length }}</div>
        </div> -->
        
    </div>
</template>

<script>

export default {
  props: {
    queue: {
      type: Array
    },
    current: {
      type: Object
    }
  },
  data() {
    return {
        isPlaying: false,
        currentIndex: 0,
        isRepeatOne: false,
        isLoggedIn: typeof localStorage !== 'undefined' && localStorage.getItem("user_id")
    };
  },
  methods: {
    play() {
        if (!this.$refs.audioPlayer.paused) {
            this.$refs.audioPlayer.pause();
            this.isPlaying = false;
        } else {
            if (this.queue.length > 0) {
                if (!this.$refs.audioPlayer.src) {

                    this.$refs.audioPlayer.src = this.getBase64Audio(this.queue[this.currentIndex].mp3_file);
                }
                this.$refs.audioPlayer.play();
                this.isPlaying = true;
            }
        }
    },
    playPrevious() {
        if (this.currentIndex > 0) {
            this.currentIndex--;
            this.$refs.audioPlayer.src = this.getBase64Audio(this.queue[this.currentIndex].mp3_file);
            this.play();
        } else {
            this.currentIndex = this.queue.length - 1;
            this.$refs.audioPlayer.src = this.getBase64Audio(this.queue[this.currentIndex].mp3_file);
            this.play();
        }
    },
    playNext() {
        if (this.currentIndex < this.queue.length - 1) {
            this.currentIndex++;
            this.$refs.audioPlayer.src = this.getBase64Audio(this.queue[this.currentIndex].mp3_file);
            this.play();
        } else {
            this.currentIndex = 0;
            this.$refs.audioPlayer.src = this.getBase64Audio(this.queue[this.currentIndex].mp3_file);
            this.play();
        }
    },
    shuffle() {
        this.queue = this.queue.sort(() => Math.random() - 0.5);
    },
    repeat() {
        this.isRepeatOne = !this.isRepeatOne;
    },
    getBase64Image(base64String) {
        return `data:image/jpeg;base64,${base64String}`;
    },
    getBase64Audio(base64String) {
        return `data:audio/mp3;base64,${base64String}`;
    },
  },
  watch: {
    current(newValue, oldValue) {
      if (newValue !== oldValue) {
        // If the current prop changes, play the new current music
        for(let i=0; i < this.queue.length;i++){
            if(this.queue[i].id == this.current.id){
                this.currentIndex = i;
                break;
            }
        }
        this.play();
      }
    }
  },
  mounted() {
    // Listen for the 'ended' event of the audio element
    this.$refs.audioPlayer.addEventListener('ended', () => {
        this.playNext(); // When the current music ends, play the next one
    });
  }
};
</script>

