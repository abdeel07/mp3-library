<script setup>

import { useField } from 'vee-validate';

const props = defineProps({
    name: String,
    placeholder: String,
    type: String,
    labelName: String,
})

const { handleChange, value, handleBlur, errorMessage, meta } = useField(() => props.name);



const validationListeners = {
  blur: evt => handleBlur(evt, true),
  change: handleChange,
  input: evt => handleChange(evt, !!errorMessage.value),
};

</script>

<template>
    <div>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">{{ labelName }}</span>
            </div>
            <input :type="type || 'text'" :value="value" v-on="validationListeners" class="input input-bordered w-full max-w-xs"
                :class="{ 'input-success': meta.touched && meta.valid, 'input-error': meta.dirty, 'input-error': meta.touched && !meta.valid }"
                @input="handleChange" @change="handleChange" @blur="handleBlur" :placeholder="placeholder"/>
            <div v-if="errorMessage != undefined" class="label">
                <span class="label-text-alt text-error">{{ capitalizeFirstLetter(errorMessage) }}</span>
            </div>
        </label>
    </div>
</template>
