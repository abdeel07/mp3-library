// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  routeRules: {
    '/': {prerender: true},
    '/profile': {ssr: false},
    '/riffs': {ssr: false},
    '/playlist/*': {ssr: false},
    '/playlists': {ssr: false},
  },
  alias: {
    pinia: "/node_modules/@pinia/nuxt/node_modules/pinia/dist/pinia.mjs"
  },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/color-mode', '@vee-validate/nuxt', '@pinia/nuxt', 'nuxt-icon', '@vueuse/nuxt', '@vueuse/motion/nuxt'],

  colorMode: {
    preference: 'retro', // default theme
    dataValue: 'theme', // activate data-theme in <html> tag
    fallback: 'light',
    classSuffix: '',
  },
});
