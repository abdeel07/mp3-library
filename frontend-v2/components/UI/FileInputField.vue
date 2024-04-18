<script setup>

const props = defineProps({
    name: String,
    labelName: String,
    filesAccepted: String,
})

const { errorMessage, value } = useField(() => props.name);


const handleFileChange = (event) => {
    value.value = event.target.files[0];
};

</script>

<template>
    <div>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">{{ labelName }}</span>
            </div>
            <input type="file" @change="handleFileChange" :accept="filesAccepted" class="file-input file-input-bordered w-full max-w-xs" />
            <div v-if="errorMessage != undefined" class="label">
                <span class="label-text-alt text-error">{{ capitalizeFirstLetter(errorMessage) }}</span>
            </div>
        </label>
    </div>
</template>