export const usePlaylistStore = defineStore("playlist", {
  state: () => ({
    loading: Boolean,
    userPlaylists: [],
    selectedPlaylist: {},
    playlistSongs: [],
    playlistEditId: Number,
  }),

  actions: {
    async fetchPlaylists() {
      const loggedInUserInfo = JSON.parse(localStorage.getItem("userData"));

      try {
        const { data, pending, refresh } = await useFetch(
          `http://localhost:5000/user/${loggedInUserInfo.user_id}/playlists`,
          {
            server: false,
          }
        );

        this.userPlaylists = data.value.playlists;
        this.loading = pending.value;
      } catch (error) {
        console.error("Error: ", error);
        this.loading = false;
      }
    },

    async searchUserPlaylist(id) {

      const loggedInUserInfo = JSON.parse(localStorage.getItem("userData"));

      try {
        const { data, pending } = await useFetch(
          `http://localhost:5000/playlists/${loggedInUserInfo.user_id}/${id}`,
          {
            server: false,
          }
        );

        console.log(data);

        this.selectedPlaylist = data.value.playlist;
        this.loading = pending.value;

      } catch (error) {
        console.error("Error: ", error);
      }
      
    },

    async getPlaylistSongs(id) {

      try {
        const { data, pending } = await useFetch(
          `http://localhost:5000/playlist/${id}/music`,
          {
            server: false,
          }
        );

        console.log(data);

        this.playlistSongs = data.value.playlistMusic;
        this.loading = pending.value;

      } catch (error) {
        console.error("Error: ", error);
      }
      
    },

  },
});
