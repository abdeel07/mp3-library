<script setup>
import Form from '../Login/Form.vue';


const { $locally } = useNuxtApp();
const loggedInUserInfo = JSON.parse($locally.getItem('userData'));
const musicStore = useAudioStore();

const { handleSubmit } = useForm({
    initialValues: {
    user_id: loggedInUserInfo.user_id,
  },
    validationSchema: riffSchema,
});


const onSubmit = handleSubmit(async (values, actions) => {
    console.log(values);
    actions.resetForm();
    
    const riffData = new FormData();

    riffData.append('user_id', values.user_id);
    riffData.append('title', values.title);
    riffData.append('artist', values.artist);
    riffData.append('image', values.thumbnail);
    riffData.append('mp3_file', values.songfile);

    try {
        const { data } = await useFetch(musicRoute, {
            method: 'POST',
            body: riffData,
        })

        if (data.value) {
            console.log(data.value);
            refreshNuxtData(musicStore.usersUploads);
        }
    } catch (error) {
        console.error('Error: ', error);
    }

    location.reload();

});

    
</script>

<template>
    <form @submit="onSubmit">
        <div class="join join-vertical">

            <!-- Title Field -->
            <div class="join-item py-1">
               <UIInputField name="title" labelName="Song Title:" placeholder="Add a title" tabindex="0"/>
             </div>
             
             <!-- Artist Field -->
            <div class="join-item py-1">
               <UIInputField name="artist" labelName="Song Artist:" placeholder="Add an artist" />
             </div>

             <!-- Thumbnail Field -->
            <div class="join-item py-1">
               <UIFileInputField name="thumbnail" labelName="Song Thumbnail" filesAccepted="image/png, image/jpeg"/>
             </div>

             <!-- MP3 Field -->
             <div class="join-item py-1">
               <UIFileInputField name="songfile" labelName="Song File" filesAccepted="audio/*"/>
             </div>

            <!-- Submit Button -->
            <div class="py-5 w-full">
                <button type="submit" class="btn text-base btn-neutral w-full">Upload Riff</button>
            </div>

        </div>
    </form>
</template>