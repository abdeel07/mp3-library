import * as Yup from 'yup';

const passwordRules = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
// const validFileExtensions = { image: ['jpg', 'gif', 'png', 'jpeg', 'svg', 'webp'] };

export const registrationSchema = Yup.object({
    username: Yup.string().required('Username is required'),
    password: Yup.string().required('Password is required').min(8).matches(passwordRules, 'Password must contain one letter or number'),
    confirmPassword: Yup.string().required('Password is Required').oneOf([Yup.ref('password'), null], "Passwords must match"),
});

export const loginSchema = Yup.object({
    username: Yup.string().required('Username is required'),
    password: Yup.string().required('Password is required')
})

export const riffSchema = Yup.object().shape({
    title: Yup.string().required('Song Title is required'),
    artist: Yup.string().required('Song Artist is required'),
    thumbnail: Yup.mixed().required('Thumbnail is Required'),
    songfile: Yup.mixed().required('MP3 file is Required'),
    user_id: Yup.string().required()
})

export const playlistSchema = Yup.object().shape({
    name: Yup.string().required('Playlist Name is Required'),
    thumbnail: Yup.mixed().required('Thumbnail is Required'),
})