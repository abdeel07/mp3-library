<script setup>

// console.log(useNuxtApp());

</script>

<template>
  <div class="hero min-h-screen">
    <div class="hero-content text-center">
      <div class="max-w-screen-lg flex flex-col items-center justify-center">
        <div class="flex justify-between">
          <h1 class="text-6xl font-bold">Welcome to RiffRoom </h1>
          <Icon name="fa6-solid:music" />
        </div>
        <p class="py-6 text-base">
          RiffRoom is a music library platform where users can upload songs,
          like their favorite songs, and create playlists for enjoyment.
        </p>
        <div class="flex">
          <RegisterModal />
          <LoginModal />
        </div>
      </div>
    </div>
  </div>
</template>
