<script setup>

</script>

<template>
    <div class="px-3">
        <!-- Open the modal using ID.showModal() method -->
        <button class="btn btn-accent btn-wide text-primary-content font-bold"
            onclick="register_modal.showModal()">Register</button>
        <dialog id="register_modal" class="modal">
            <div class="modal-box">
                <form method="dialog">
                    <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
                </form>
                <div class="">
                    <h3 class="text-left font-bold text-xl">Create an account</h3>
                </div>
                <RegisterForm class="p-6" />
            </div>
        </dialog>
    </div>
</template>