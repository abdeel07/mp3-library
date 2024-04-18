export const loginRoute = 'http://localhost:5000/login'
export const registerRoute = 'http://localhost:5000/register'
export const musicRoute = 'http://localhost:5000/music'
export const playlistRoute = 'http://localhost:5000/playlist'

export { jwtDecode } from 'jwt-decode';

export const capitalizeFirstLetter = (string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

export const registerUser = async (data) => {

    useFetch(registerRoute, {
        method: 'POST',
        body: data
    }).then(responseData => {
        console.log(responseData);
    }).catch(error => {
        // Handle errors here
        console.error("An error occurred while registering the user:", error);
    });

}

export function convertFileToBase64(file) {
    return new Promise((resolve, reject) => {
      if (!file) {
        reject(new Error('No file provided'));
        return;
      }
  
      const reader = new FileReader();
  
      reader.onload = function(event) {
        const base64Data = event.target.result;
        resolve(base64Data);
      };
  
      reader.onerror = function(error) {
        reject(error);
      };
  
      // Convert the file to base64
      reader.readAsDataURL(file);
    });
  }
  
export const getBase64Audio = (audioFile) => {
    return `data:audio/mp3;base64,${audioFile}`;
}

export const getBase64Image = (base64String) => {
  return `data:image/jpeg;base64,${base64String}`;
};

export const formatTime = (seconds) => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.floor(seconds % 60);
  return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}
