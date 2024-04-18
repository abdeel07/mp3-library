<template>
    <button class="btn header__sign-in" @click.prevent="logout">
        Logout
    </button>
</template>

<script setup>
    function logout(){
        localStorage.removeItem("user_id");
        window.location.href = "/";
    }
</script>