<script setup>

const props = defineProps({
    isShowing: Boolean
})
    
</script>

<template>
    <div v-show="props.isShowing" class="context-menu" tabindex="0">
        <slot></slot>
    </div>
</template>