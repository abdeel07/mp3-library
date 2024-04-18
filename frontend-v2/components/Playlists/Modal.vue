<script setup>

</script>

<template>
    <div class="px-3">
        <!-- Open the modal using ID.showModal() method -->
        <button class="btn btn-neutral text-white font-semibold" onclick="playlist_modal.showModal()">New
            Playlist</button>
        <dialog id="playlist_modal" class="modal">
            <div class="modal-box">
                <form method="dialog">
                    <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
                </form>
                <div class="">
                    <h3 class="text-left font-bold text-xl">Create a Playlist</h3>
                </div>
                <div class="flex flex-col items-center justify-center">
                    <PlaylistsForm class="p-4" />
                </div>
            </div>
        </dialog>
    </div>
</template>