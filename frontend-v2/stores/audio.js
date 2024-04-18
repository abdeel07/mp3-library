export const useAudioStore = defineStore("audio", {
  state: () => ({
    usersUploads: [],
    loading: Boolean,
    selectedAudio: {
      artist: "",
      title: "",
      id: Number,
      image: "",
      audioFile: null,
      duration: Number,
      currentTime: 0,
      volume: 100,
    },
    isPlaying: false,
    toBeDeleted: false,
    audioEditId: Number,
  }),

  actions: {
    async fetchUploads() {
      const loggedInUserInfo = JSON.parse(localStorage.getItem("userData"));

      try {
        const { data, pending, refresh } = await useFetch(`http://localhost:5000/user/${loggedInUserInfo.user_id}/music`, {
          server: false,
        });

        this.usersUploads = data.value.music;
        this.loading = pending.value;

      } catch (error) {
        console.error("Error: ", error);
        this.loading = false;
      }
    },

    setSelectedAudio(audioID) {
      this.selectedAudio = audioID;
    },

    searchForSelectedAudio(id) {
      for (let i = 0; i < this.usersUploads.length; i++) {
        if (this.usersUploads[i].id === id) {
          this.selectedAudio.artist = this.usersUploads[i].artist;
          this.selectedAudio.title = this.usersUploads[i].title;
          this.selectedAudio.id = this.usersUploads[i].id;
          this.selectedAudio.image = getBase64Image(this.usersUploads[i].image);
          this.selectedAudio.audioFile = new Audio(
            getBase64Audio(this.usersUploads[i].mp3_file)
          );

          this.selectedAudio.audioFile.addEventListener(
            "loadedmetadata",
            () => {
              this.selectedAudio.duration =
                this.selectedAudio.audioFile.duration;
            }
          );

         if (this.isPlaying) {
           this.selectedAudio.audioFile.addEventListener("timeupdate", () => {
             this.selectedAudio.currentTime =
               this.selectedAudio.audioFile.currentTime;
           });
         }

          
          break;
        }
      }
      return null; // If no object with the provided ID is found
    },

    nextSong(songID) {
      for (let i = 0; i < this.usersUploads.length; i++) {
        if (this.usersUploads[i].id === songID) {
          if (i < this.usersUploads.length - 1) {
            this.stopAudio();
            this.playOtherAudio(this.usersUploads[i + 1].id);
          }
          break;
        }
      }
    },

    previousSong(songID) {
      for (let i = 0; i < this.usersUploads.length; i++) {
        if (this.usersUploads[i].id === songID) {
          if (i > 0) {
            this.playOtherAudio(this.usersUploads[i - 1].id);
          }
          break;
        }
      }
    },

    togglePlay() {
      this.isPlaying = !this.isPlaying;
      if (this.isPlaying) {
        this.selectedAudio.audioFile.play();
      } else {
        this.selectedAudio.audioFile.pause();
      }
    },

    stopAudio() {
      if (this.isPlaying) {
        this.isPlaying = false;
        this.selectedAudio.audioFile.pause();
        this.selectedAudio.audioFile.currentTime = 0; // Reset the audio to the beginning
      }
    },

    updateVolume() {
      this.selectedAudio.audioFile.volume = this.selectedAudio.volume / 100;
    },

    updateCurrentTime() {
      this.selectedAudio.audioFile.currentTime = this.selectedAudio.currentTime;
    },

    startAudio(songID) {
      this.isPlaying = true;
      this.searchForSelectedAudio(songID);
      this.selectedAudio.audioFile.play();
    },

    playOtherAudio(songID) {
      this.stopAudio();
      this.isPlaying = true;
      this.searchForSelectedAudio(songID);
      this.updateVolume()
      this.selectedAudio.audioFile.play();
    },

    playAudio() {
      this.isPlaying = true;
      this.selectedAudio.audioFile.play();
    },

    pauseAudio() {
      this.isPlaying = false;
      this.selectedAudio.audioFile.pause();
    },
  },
});
