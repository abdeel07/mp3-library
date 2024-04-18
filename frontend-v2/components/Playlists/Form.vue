<script setup>

const { $locally } = useNuxtApp();
const loggedInUserInfo = JSON.parse($locally.getItem('userData'));

const { handleSubmit } = useForm({
    initialValues: {
    user_id: loggedInUserInfo.user_id,
  },
    validationSchema: playlistSchema,
});


const onSubmit = handleSubmit(async (values, actions) => {
    console.log(values);
    actions.resetForm();
    
    const playlistData = new FormData();

    playlistData.append('user_id', values.user_id);
    playlistData.append('name', values.name);
    playlistData.append('image', values.thumbnail);

    try {
        const { data } = await useFetch(playlistRoute, {
            method: 'POST',
            body: playlistData,
        })

        if (data.value) {
            console.log(data.value);
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

            <!-- Playlist Name Field -->
            <div class="join-item py-1">
               <UIInputField name="name" labelName="Playlist Name:" placeholder="Add a name" tabindex="0"/>
             </div>
             
             <!-- Thumbnail Field -->
            <div class="join-item py-1">
               <UIFileInputField name="thumbnail" labelName="Playlist Thumbnail" filesAccepted="image/png, image/jpeg"/>
             </div>

            <!-- Submit Button -->
            <div class="py-5 w-full">
                <button type="submit" class="btn text-base btn-neutral w-full">Create Playlist</button>
            </div>

        </div>
    </form>
</template>