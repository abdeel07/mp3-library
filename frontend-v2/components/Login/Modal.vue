<script setup>

</script>

<template>
    <div class="px-3">
        <!-- Open the modal using ID.showModal() method -->
        <button class="btn btn-accent btn-wide text-primary-content font-bold"
            onclick="login_modal.showModal()">Login</button>
        <dialog id="login_modal" class="modal">
            <div class="modal-box">
                <form method="dialog">
                    <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
                </form>
                <div class="">
                    <h3 class="text-left font-bold text-lg">Login</h3>
                </div>
                <LoginForm class="py-4" />
            </div>
        </dialog>
    </div>
</template>