<template>
    <div class="header">
        <div class="container">
            <div class="header__container">
                <div class="header__logo">RiffRoom</div>
                <div class="header__profile">
                    <div class="d-flex">
                        <div class="header__profile-image"></div>
                        <div class="header__profile-username"></div>
                    </div>
                </div>
                <div class="header__sign">
                    <template v-if="isLoggedIn">
                        <Logout />
                    </template>
                    <template v-else>
                        <Login />
                        <Register />
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import Login from "./Login.vue";
    import Register from "./Register.vue";
    import Logout from "./Logout.vue";

    const isLoggedIn = typeof localStorage !== 'undefined' && localStorage.getItem("user_id");
</script>
