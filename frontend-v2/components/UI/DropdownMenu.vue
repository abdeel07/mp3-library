<script setup>

const doSomething = () => {
    console.log('hello');
}

const doSomethingElse = () => {
    console.log('world')
}

</script>

<template>
    <div class="absolute">
        <ul class="menu p-2 shadow bg-base-100 rounded-box w-52">
            <li><a @click="doSomething">Item 1</a></li>
            <li><a @click="doSomethingElse">Item 2</a></li>
        </ul>
    </div>
</template>