<script setup>

const audioStore = useAudioStore();

const route = useRoute();

const props = defineProps({
    audioId: Number,
})

const setSelectedID = () => {
    audioStore.audioEditId = props.audioId;

}

const onSubmit = async () => {
    console.log(audioStore.audioEditId);
    
    try {
        const data = await $fetch(`http://20.200.126.39:5000/playlist/${route.params.id}/${audioStore.audioEditId}`, {
          method: 'DELETE',
          headers: { 'Content-Type': 'application/json' },
      })
       
        location.reload()
        return data.value;

      } catch (error) {
        console.error("Error: ", error);
      }
}

</script>

<template>
    <!-- The button to open modal -->
    <label @click="setSelectedID()" for="delete_modal" class="mr-2 btn text-center btn-error btn-xs font-bold">Remove</label>

    <!-- Put this part before </body> tag -->
    <input type="checkbox" id="delete_modal" class="modal-toggle" />
    <div class="modal" role="dialog">
        <div class="modal-box">
            <form method="dialog">
                <label for="delete_modal" class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</label>
            </form>
            <div class="">
                <h3 class="text-left font-bold text-lg p-4">Remove Riff</h3>
            </div>
            <div class="flex flex-col items-center justify-center">
                <svg aria-hidden="true" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" fill="none"
                    class="h-24 w-24 text-error">
                    <path
                        d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"
                        stroke-linejoin="round" stroke-linecap="round"></path>
                </svg>
                <div>
                    <p class="p-4 text-base font-semibold">Are you sure you want to remove this Riff from the playlist?</p>
                    <button @click="onSubmit" class="btn btn-neutral w-full hover:btn-error">Remove Riff</button>
                </div>
            </div>
        </div>
    </div>
</template>
