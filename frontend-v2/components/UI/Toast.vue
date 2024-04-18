<script setup>
const props = defineProps({
    message: String,
    toastType: String,
})
</script>

<template>
    <div>
        <div class="toast">
            <div :class="toastType">
                <span>{{ message }}</span>
            </div>
        </div>
    </div>
</template>